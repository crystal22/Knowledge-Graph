# coding=utf-8
import re
import jieba
import jieba.analyse
from hanziconv import HanziConv
from collections import Counter
from Netease_Graph.lib.config import *
from pyhanlp import *
import json
import hashlib
from arango import ArangoClient

jieba.analyse.set_stop_words(STOPWORDS_FILEPATH)
jieba.load_userdict(USERDICT_FILEPATH)

class CKeywords2json:
    def __init__(self):
        self.topK = 3
        self.allow_pos = ALLOW_POS

    def get_tfidf_keywords(self, document):
        res = jieba.analyse.extract_tags(document, withWeight=True, topK=self.topK, allowPOS=self.allow_pos)
        return res

    def get_textank_keywords(self, document):
        res = jieba.analyse.textrank(document, withWeight=True, topK=self.topK, allowPOS=self.allow_pos)
        return res

    def get_topk(self, document):
        seg_list = jieba.cut(document)
        c = Counter()
        for i in seg_list:
            if len(i) > 1 and i != '\r\n':
                c[i] += 1
        return c.most_common(self.topK)

    def print_keywords(self, document, tfidf_keywords, textrank_keywords,is_print=False):
        if is_print == True:
            print('-' * 50)
            print(len(document), document)
            print('tfidf', tfidf_keywords)
            print('textrank', textrank_keywords)
            print('-' * 50)

    def get_keywords(self,input_file,output_file):
        with open(input_file, encoding='utf8') as f:
            content = f.readlines()

        res = []
        for index, c in enumerate(content):
            c = HanziConv.toSimplified(c)
            if len(c) < 20:
                self.topK = 1
            elif len(c) < 50 and len(c) > 20:
                self.topK = 2
            elif len(c) < 200 and len(c) > 50:
                self.topK = 3
            else:
                self.topK = 4

            id = c.split('\t')[0]
            text = c.split('\t')[1].strip('\n')
            document = ''.join(re.findall('[\u4e00-\u9fa5]+', text))
            tfidf_keywords = self.get_tfidf_keywords(document)
            textrank_keywords = self.get_textank_keywords(document)
            # self.print_keywords(document = document,
            #                     tfidf_keywords = tfidf_keywords,
            #                     textrank_keywords = textrank_keywords,
            #                     is_print=True)
            keywords_res = {}
            for i in tfidf_keywords:
                keywords_res[i[0]] = [i[1],0]

            for i in textrank_keywords:
                if i[0] in keywords_res:
                    keywords_res[i[0]][1] = i[1]
                else:
                    keywords_res[i[0]] = [0,i[1]]

            if keywords_res:
                res.append('{}\t{}\n'.format(id, json.dumps(keywords_res,ensure_ascii=False)))

            if index % 100 == 0:
                print('{}/{}'.format(index, len(content)))

        with open(output_file, 'w', encoding='utf8') as f:
            f.writelines(res)

if __name__ == '__main__':
    ckeywords2json = CKeywords2json()
    ckeywords2json.get_keywords(input_file=LYRIC_FILEPATH,output_file=RESULT_LYRIC_KEYWORDS_PATH)
    ckeywords2json.get_keywords(input_file=COMMENT_FILEPATH,output_file=RESULT_COMMENT_KEYWORDS_PATH)
    ckeywords2json.get_keywords(input_file=PLAYLIST_DESC_FILEPATH,output_file=RESULT_DESC_KEYWORDS_PATH)

