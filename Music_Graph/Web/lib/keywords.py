# coding=utf-8
import sys
sys.path.append('../lib/')

import re
import jieba
import jieba.analyse
import jieba.posseg as pseg
from hanziconv import HanziConv
from collections import Counter
from Web.lib.config import *
from pyhanlp import *
from collections import defaultdict

jieba.analyse.set_stop_words(STOPWORDS_FILEPATH)
jieba.load_userdict(USERDICT_FILEPATH)

class CKeywords:
    def __init__(self):
        self.topK = 5
        self.allow_pos = QUERY_ALLOW_POS
        self.stopwords = set()
        content = open(STOPWORDS_FILEPATH, 'rb').read().decode('utf-8')
        for line in content.splitlines():
            self.stopwords.add(line)

    def get_tfidf_keywords(self, document,withWeight=True):
        res = jieba.analyse.extract_tags(document, withWeight=withWeight, topK=self.topK, allowPOS=self.allow_pos)
        return res

    def get_textank_keywords(self, document,withWeight=True):
        res = jieba.analyse.textrank(document, withWeight=withWeight, topK=self.topK, allowPOS=self.allow_pos)
        return res

    def get_syntactic_keyowords(self, document, is_pos_strict=False):
        key_phrase = []
        vob_phrase = [] # 动宾关系
        att_phrase = []

        tree = HanLP.parseDependency(document)
        for word in tree.iterator():
            # print(word)
            if word.DEPREL == '定中关系' and word.POSTAG in SYNTACTIC_POS and word.HEAD.POSTAG in SYNTACTIC_POS:
                if word.POSTAG in SYNTACTIC_BOTTOM_POS:
                    att_phrase.append(word.LEMMA)
                if word.HEAD.POSTAG in SYNTACTIC_TOP_POS:
                    att_phrase.append(word.HEAD.LEMMA)
            if word.DEPREL == '动宾关系' and word.POSTAG in SYNTACTIC_POS and word.HEAD.POSTAG in SYNTACTIC_POS:
                if word.POSTAG in SYNTACTIC_BOTTOM_POS:
                    vob_phrase.append(word.LEMMA)
                if word.HEAD.POSTAG in SYNTACTIC_TOP_POS:
                    vob_phrase.append(word.HEAD.LEMMA)

        att_phrase = [phrase for phrase in att_phrase if len(phrase) > 1 and phrase not in self.stopwords]
        vob_phrase = [phrase for phrase in vob_phrase if len(phrase) > 1 and phrase not in self.stopwords]
        key_phrase.extend(att_phrase+vob_phrase)
        key_phrase = list(set(key_phrase))
        return key_phrase

    def get_keywords(self,document):
        document = ''.join(re.findall('[\u4e00-\u9fa5a-zA-Z]+', document))
        res = defaultdict(int)
        textrank_keywords = self.get_textank_keywords(document, withWeight=False)
        tfidf_keywords = self.get_tfidf_keywords(document, withWeight=False)
        syntactic_keywords = self.get_syntactic_keyowords(document, is_pos_strict=True)
        for tk in textrank_keywords:
            if tk in syntactic_keywords:
                res[tk] +=3
                syntactic_keywords.remove(tk)
            else:
                res[tk] += 1

        for tk in tfidf_keywords:
            if tk in syntactic_keywords:
                res[tk] +=3
                syntactic_keywords.remove(tk)
            else:
                res[tk] += 1

        for sk in syntactic_keywords:
            res[sk] += 1

        res = sorted(res.items(), key=lambda d: d[1], reverse=True)
        return [i[0] for i in res][:self.topK]

    def get_clean_document(self,document):
        document = HanziConv.toSimplified(document)
        document = ''.join(re.findall('[\u4e00-\u9fa5]+', document))
        return document