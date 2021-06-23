# coding:utf-8
import sys
sys.path.append('../')
sys.path.append('./')
from arango import ArangoClient
from Web.lib.config import *
from collections import defaultdict

class CSubGraphSearch:
    def __init__(self):
        client = ArangoClient()
        self.db = client.db(ARANGODB_DATABASE,
                            username=ARANGODB_USER_NAME,
                            password=ARANGODB_PASSWORD)
        self.type = 'neteasemusic'

    def get_aql_result(self, aql_query):
        result = self.db.aql.execute(aql_query)
        return result

    def search(self,value):
        echarts_data = []
        echarts_link = []
        # 二级节点
        aql_base_2 = '''
            for c in vertex_{}
            filter c.name == '{}'
            for v in 2..2 any c edge_{}
            for e in edge_{}
                filter (e.fromValue == v.name) and e.type != '{}'
                limit 50
                return distinct e
        '''
        aql_query_2 = aql_base_2.format(self.type, value, self.type, self.type, '分类标签为')

        # 一级节点
        aql_base_1 = '''
            for e in edge_{}
                filter e.fromValue == '{}' or e.toValue == '{}'
                limit 50
                return distinct e
        '''
        aql_query_1 = aql_base_1.format(self.type, value, value)

        result_list_1 = [i for i in self.get_aql_result(aql_query_1)]
        result_list_2 = [i for i in self.get_aql_result(aql_query_2)]

        overlap = []

        for i in result_list_1:
            tmp_data = {}
            tmp_data['name'] = i['fromValue']
            tmp_data['des'] = ''
            tmp_data['simbolSize'] = 100 if i['fromValue'] == value else 50
            tmp_data['category'] = 0 if i['fromValue'] == value else 1
            if tmp_data['name'] not in overlap:
                echarts_data.append(tmp_data)
                overlap.append(tmp_data['name'])

            tmp_data = {}
            tmp_data['name'] = i['toValue']
            tmp_data['des'] = ''
            tmp_data['simbolSize'] = 100 if i['toValue'] == value else 50
            tmp_data['category'] = 0 if i['toValue'] == value else 1
            if tmp_data['name'] not in overlap:
                echarts_data.append(tmp_data)
                overlap.append(tmp_data['name'])

            tmp_link = {}
            tmp_link['target'] = i['toValue']
            tmp_link['source'] = i['fromValue']
            tmp_link['name'] = i['edgeType']

            ts_item = [tmp_link['target'],tmp_link['source']]

            if ts_item not in overlap:
                echarts_link.append(tmp_link)
                overlap.append([tmp_link['target'], tmp_link['source']])
                overlap.append([tmp_link['source'],tmp_link['target']])

        for i in result_list_2:
            tmp_data = {}
            tmp_data['name'] = i['fromValue']
            tmp_data['des'] = ''
            tmp_data['simbolSize'] = 100 if i['fromValue'] == value else 50
            tmp_data['category'] = 2
            if tmp_data['name'] not in overlap:
                echarts_data.append(tmp_data)
                overlap.append(tmp_data['name'])

            tmp_data = {}
            tmp_data['name'] = i['toValue']
            tmp_data['des'] = ''
            tmp_data['simbolSize'] = 100 if i['toValue'] == value else 50
            tmp_data['category'] = 2 if i['toValue'] == value else 3
            if tmp_data['name'] not in overlap:
                echarts_data.append(tmp_data)
                overlap.append(tmp_data['name'])

            tmp_link = {}
            tmp_link['target'] = i['toValue']
            tmp_link['source'] = i['fromValue']
            tmp_link['name'] = i['edgeType']

            ts_item = [tmp_link['target'],tmp_link['source']]

            if ts_item not in overlap:
                echarts_link.append(tmp_link)
                overlap.append([tmp_link['target'], tmp_link['source']])
                overlap.append([tmp_link['source'],tmp_link['target']])

        return echarts_data,echarts_link


if __name__ == '__main__':
    csubsearch = CSubGraphSearch()
    print(csubsearch.search('中华人民共和国国歌'))
