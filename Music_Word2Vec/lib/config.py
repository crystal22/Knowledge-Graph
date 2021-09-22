# coding=utf-8
# BASE DIR
BASE_DIR = '//'

# MySQL
MYSQL_HOST = YOUR_HOST
MYSQL_USERNAME = YOUR_USERNAME
MYSQL_PASSWORD = YOUR_PASSWORD
MYSQL_DATABASE = YOUR_DATABASE
MYSQL_PORT = 3306

# ArangoDB
ARANGODB_HTTP_SERVER = YOUR_HTTP_SERVER
ARANGODB_TCP_SERVER = YOUR_TCP_SERVER
ARANGODB_USER_NAME = YOUR_USERNAME
ARANGODB_PASSWORD = YOUR_PASSWORD
ARANGODB_DATABASE = YOUR_DATABASE

BASE_NAME = 'neteasemusic'
CORPUS_NAME = 'corpus_{}'.format(BASE_NAME)
VERTEX_NAME = 'vertex_{}'.format(BASE_NAME)
EDGE_NAME = 'edge_{}'.format(BASE_NAME)
GRAPH_NAME = 'graph_{}'.format(BASE_NAME)
VERTEX_COLLECTION = 'vertex_{}/'.format(BASE_NAME)

# WORD EMBEDDING API
WORD_EMBEDDING_API = 'http:/ip:port/api/similar/'

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

