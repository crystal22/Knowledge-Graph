# coding=utf-8
import os

# BASE DIR
BASE_DIR = 'D:/Graduate/Music_Graph/Web/'
# BASE_DIR = '/mnt/Music_Graph/Web/'

# MySQL
MYSQL_HOST = ''
MYSQL_USERNAME = ''
MYSQL_PASSWORD = ''
MYSQL_DATABASE = ''
MYSQL_PORT = 3306

# ArangoDB
ARANGODB_HTTP_SERVER = 'http://127.0.0.1:8529/'
ARANGODB_TCP_SERVER = 'tcp://127.0.0.1:8529/'
ARANGODB_USER_NAME = ''
ARANGODB_PASSWORD = ''
ARANGODB_DATABASE = ''

BASE_NAME = 'neteasemusic'
CORPUS_NAME = 'corpus_{}'.format(BASE_NAME)
VERTEX_NAME = 'vertex_{}'.format(BASE_NAME)
EDGE_NAME = 'edge_{}'.format(BASE_NAME)
GRAPH_NAME = 'graph_{}'.format(BASE_NAME)
VERTEX_COLLECTION = 'vertex_{}/'.format(BASE_NAME)

# WORD EMBEDDING API
GENERAL_EMBEDDING_API = 'http://ip:port/api/similar_general/'
MUSIC_EMBEDDING_API = 'http://ip:port/api/similar_music/'

# CUTWORDS
POS_DICT = {
    'an': '名形词',
    'i': '成语',
    'j': '简称略语',
    'n': '名词',
    'nr': '人名',
    'nrfg': '古近代人名',
    'nrt': '音译人名',
    'ns': '地名',
    'nt': '机构团体',
    'nz': '其他专名',
    'vn': '名动词',
    't': '时间词'
}

ALLOW_POS = ('ns', 'n', 'vn', 'a', 'an', 'i', 'j', 'nr', 'nrfg', 'nrt', 'ns', 'nt', 'nz', 't')
QUERY_ALLOW_POS = ('ns', 'n', 'vn', 'a', 'an', 'i', 'j', 'nr', 'nrfg', 'nrt', 'ns', 'nt', 'nz')
SYNTACTIC_BOTTOM_POS = ('n', 'an', 'vn', 'a', 'nt')
SYNTACTIC_TOP_POS = ('n', 'an', 'vn', 'a', 'nt')
SYNTACTIC_POS = ('n', 'an', 'vn', 'v', 'a', 'nt')

# DIRECTORY
STOPWORDS_FILEPATH = os.path.join(BASE_DIR,'data/stopwords/stopwords.txt')
PLAYLIST_DICT_TXTPATH = os.path.join(BASE_DIR,'data/dict/playlist_dict.txt')
PLAYLIST_DICT_JSONPATH = os.path.join(BASE_DIR,'data/dict/playlist_dict.json')
USERDICT_FILEPATH = os.path.join(BASE_DIR,'data/dict/userdict.txt')


WEIGHT_DICT = {
    0: 1.0,
    1: 0.8,
    2: 0.8,
    3: 0.6,
    4: 0.6,
    5: 0.6,
    6: 0.4,
    7: 0.4,
    8: 0.2,
    9: 0.2
}

# CAPTION DIR
CAPTION_DIR = '/mnt/DenseVideoCaption/test/results/'
VIDEO_DIR = '/mnt/DenseVideoCaption/test/'
DISPLAY_DIR = 'app/static/upload/'
FEATURES_DIR = '/mnt/DenseVideoCaption/test/features/'
SHELL_RUN_FEATURES_PATH = '/mnt/DenseVideoCaption/run_features.sh'
SHELL_RUN_CAPTIONS_PATH = '/mnt/DenseVideoCaption/run_captions.sh'

# TRANS API
APPID = ''
SECRETKEY = ''
URL = '/api/trans/vip/translate'
FROMLANG = 'en'
TOLANG = 'zh'

