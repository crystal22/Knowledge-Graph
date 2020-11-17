# coding=utf-8
# BASE DIR
BASE_DIR = '//'

# MySQL
MYSQL_HOST = '39.96.35.2'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'netease'
MYSQL_PORT = 3306

# ArangoDB
ARANGODB_HTTP_SERVER = 'http://127.0.0.1:8529/'
ARANGODB_TCP_SERVER = 'tcp://127.0.0.1:8529/'
ARANGODB_USER_NAME = 'root'
ARANGODB_PASSWORD = 'tiktok05'
ARANGODB_DATABASE = 'music'

BASE_NAME = 'neteasemusic'
CORPUS_NAME = 'corpus_{}'.format(BASE_NAME)
VERTEX_NAME = 'vertex_{}'.format(BASE_NAME)
EDGE_NAME = 'edge_{}'.format(BASE_NAME)
GRAPH_NAME = 'graph_{}'.format(BASE_NAME)
VERTEX_COLLECTION = 'vertex_{}/'.format(BASE_NAME)

# WORD EMBEDDING API
WORD_EMBEDDING_API = 'http://39.96.35.2:5024/api/similar/'

# CUTWORDS
POS_DICT = {
    'an':'名形词',
    'i':'成语',
    'j':'简称略语',
    'n':'名词',
    'nr':'人名',
    'nrfg':'古近代人名',
    'nrt':'音译人名',
    'ns':'地名',
    'nt':'机构团体',
    'nz':'其他专名',
    'vn':'动词'
}

