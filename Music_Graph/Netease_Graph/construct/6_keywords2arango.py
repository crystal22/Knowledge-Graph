# coding=utf-8
from Netease_Graph.lib.config import *
import json
import hashlib
from arango import ArangoClient

class CKeywords2arango:
    def __init__(self):
        client = ArangoClient()
        self.db = client.db(ARANGODB_DATABASE,
                            username=ARANGODB_USER_NAME,
                            password=ARANGODB_PASSWORD)
        self.file_desc_keywords = RESULT_DESC_KEYWORDS_PATH
        self.file_comment_keywords = RESULT_COMMENT_KEYWORDS_PATH
        self.file_lyric_keywords = RESULT_LYRIC_KEYWORDS_PATH
        self.vertex = VERTEX_NAME

    def get_aql_result(self, aql_query):
        result = self.db.aql.execute(aql_query)
        return result

    def get_hash(self,s):
        md5 = hashlib.md5()
        md5.update(s.encode('utf-8'))
        ret = md5.hexdigest()
        return ret

    def update_playlist_keywords(self):
        with open(self.file_desc_keywords,encoding='utf8') as f:
            content = f.readlines()

        for i in content:
            line = i.strip('\n').split('\t')
            key = 'playlist-'+line[0]
            hash_key = self.get_hash(key)
            print(line[0])
            print(line[1])
            value = json.loads(line[1])
            print(value)
            update_query = '{'+'desc_keywords:{}'.format(value)+'}'
            print(update_query)
            aql_query = "update '{}' with {} in {}".format(hash_key,update_query,self.vertex)
            self.get_aql_result(aql_query)

    def update_lyric_keywords(self):
        with open(self.file_lyric_keywords,encoding='utf8') as f:
            content = f.readlines()

        for i in content:
            line = i.strip('\n').split('\t')
            key = 'music-'+line[0]
            hash_key = self.get_hash(key)
            value = json.loads(line[1])
            update_query = '{'+'lyric_keywords:{}'.format(value)+'}'
            aql_query = "update '{}' with {} in {}".format(hash_key,update_query,self.vertex)
            try:
                self.get_aql_result(aql_query)
            except Exception as e:
                print('Error: ',aql_query,e)
                break

    def update_comment_keywords(self):
        with open(self.file_comment_keywords,encoding='utf8') as f:
            content = f.readlines()

        for i in content:
            line = i.strip('\n').split('\t')
            key = 'music-'+line[0]
            hash_key = self.get_hash(key)
            value = json.loads(line[1])
            update_query = '{'+'comment_keywords:{}'.format(value)+'}'
            aql_query = "update '{}' with {} in {}".format(hash_key,update_query,self.vertex)
            self.get_aql_result(aql_query)


if __name__ == '__main__':
    ckeywords2arango = CKeywords2arango()
    ckeywords2arango.update_playlist_keywords()
    ckeywords2arango.update_comment_keywords()
    ckeywords2arango.update_lyric_keywords()
