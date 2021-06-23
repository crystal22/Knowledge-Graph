# coding:utf-8
import sys
sys.path.append('../')
sys.path.append('./')
from arango import ArangoClient
from Web.lib.config import *
from collections import defaultdict
from Web.lib.keywords import CKeywords
import requests
import jieba
import jieba.posseg as pseg
import jieba.analyse
jieba.analyse.set_stop_words(STOPWORDS_FILEPATH)
jieba.load_userdict(USERDICT_FILEPATH)

class CArangoSearch:
    def __init__(self):
        client = ArangoClient()
        self.db = client.db(ARANGODB_DATABASE,
                            username=ARANGODB_USER_NAME,
                            password=ARANGODB_PASSWORD)
        self.similar_topk = 15
        self.similar_single_topk = 3
        self.recommendation_topk = 50
        self.type = 'neteasemusic'
        self.keywords = CKeywords()

    def get_aql_result(self, aql_query):
        result = self.db.aql.execute(aql_query)
        return result

    def search_music(self,keywords_list,type,with_weight=True):
        result_dict = defaultdict(list)
        if type == 'simple':
            aql_base = '''
                for c in vertex_{}
                    filter (like(lower(c.name),'%{}%') or like(lower(c.lyric_keywords),'%{}%') 
                    or like(lower(c.comment_keywords),'%{}%')) and c.type == '歌曲名称'
                    sort c.rank desc
                    limit 50
                    return distinct [c.mysql_id, c.name, c.rank]
            '''
        elif type == 'graph':
            aql_base = '''
                for c in vertex_{}
                    filter like(lower(c.name),'%{}%') or like(lower(c.lyric_keywords),'%{}%') 
                    or like(lower(c.desc_keywords),'%{}%') or like(lower(c.comment_keywords),'%{}%')
                    for v in 0..1 any c edge_{}
                        filter v.type == '歌曲名称'
                        sort v.rank desc
                        limit 50
                        return distinct [v.mysql_id, v.name, v.rank]
            '''
        else:
            return 0
        # print(keywords_dict)

        for n,keywords in enumerate(keywords_list):
            aql_query = aql_base.format(self.type,keywords[0],keywords[0],keywords[0],keywords[0],self.type)
            result_list = [i for i in self.get_aql_result(aql_query)]
            # print('*',keywords, result_list)
            weight = (len(keywords_list)-n)*0.1
            for i in result_list:
                id  = i[0]
                name = id + '：'+ i[1]
                rank = i[2]
                if name not in result_dict:
                    result_dict[name] = [1,rank] if not with_weight else [keywords[1]*weight,rank]
                else:
                    result_dict[name][0] += 1 if not with_weight else keywords[1]*weight
            else:
                pass
        print(result_dict)
        result_dict = sorted(result_dict.items(), key = lambda d:(d[1][0],d[1][1]), reverse = True)
        return result_dict

    def search_similar(self, keywords, topK, type):
        if type == 'general':
            r = requests.post(GENERAL_EMBEDDING_API+keywords)
            res = r.json()['most similar'] if not r.json()['most similar'] == '没有结果' else []
        elif type == 'music':
            r = requests.post(MUSIC_EMBEDDING_API+keywords)
            res = r.json()['most similar'] if not r.json()['most similar'] == '没有结果' else []
        else:
            res = []
        return res[:topK]

    def get_search_result(self, keywords, topK, type):
        similar_dict = {}
        keywords = keywords[:topK]
        for c in keywords:
            similar_words_general = self.search_similar(keywords=c, topK=self.similar_single_topk, type='general')
            similar_words_music = self.search_similar(keywords=c, topK=self.similar_single_topk, type='music')
            similar_words = similar_words_general + similar_words_music
            for sw in similar_words:
                # print(sw)
                if sw[0] not in similar_dict:
                    similar_dict[sw[0]] = sw[1]
                else:
                    if similar_dict[sw[0]] < sw[1]:
                        similar_dict[sw[0]] = sw[1]
        similar_list = sorted(similar_dict.items(), key=lambda d: d[1], reverse=True)[:self.similar_topk]
        # print(similar_list)
        music_recommendation = self.search_music(keywords_list=similar_list, with_weight=True, type=type)
        # print('*' * 30, '{}-result'.format(type), '*' * 30)
        # print(len(music_recommendation), music_recommendation)
        # for i in music_recommendation:
        #     print(i)
        #     print(i[0],i[1][0]*0.1+i[1][1]*10**6)
        music_recommendation_no_weight = [i[0] for i in music_recommendation[:self.recommendation_topk]]
        return music_recommendation_no_weight

    def get_keywords(self,document):
        return self.keywords.get_keywords(document)

if __name__ == '__main__':
    csearch = CArangoSearch()
    # document = '人们看到一大群人在舞台上走来走去.一群人站在舞台上.人群欢呼.又是一年国庆，你还记得去年的大阅兵吗？15秒重温超燃瞬间！每一秒都是骄傲与自豪。'
    # document = '男人们继续互相打球，最后把球打回来.穿黑衬衫的人再次出现.男人们继续打球.【NBA】这或许是你看到过最燃的篮球混剪'
    document = '你的篮球梦还在吗'
    keywords = csearch.get_keywords(document)
    # keywords = ['骄傲','阅兵','人群','自豪','国庆']
    res = csearch.get_search_result(keywords, topK=5, type='graph')[:10]
    print('-'*50)
    print(keywords)
    for i,n in enumerate(res):
        print(i+1,n)





