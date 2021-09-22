# coding=utf-8
import os

# BASE DIR
BASE_DIR = 'D:/Graduate/Music_Graph/Netease_Graph/'

# MySQL
# MYSQL_HOST = YOUR_HOST
# MYSQL_USERNAME = YOUR_USERNAME
# MYSQL_PASSWORD = YOUR_PASSWORD
# MYSQL_DATABASE = YOUR_DATABASE
# MYSQL_PORT = 3306

# LOCAL MYSQL
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
WORD_EMBEDDING_API = 'http://ip:port/api/similar/'

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
MUSIC_DICT_JSONPATH = os.path.join(BASE_DIR,'data/dict/music_dict.json')
ALBUM_DICT_JSONPATH = os.path.join(BASE_DIR,'data/dict/album_dict.json')
USERDICT_FILEPATH = os.path.join(BASE_DIR,'data/dict/userdict.txt')
ARANGO_PLAYLIST_FILEPATH = os.path.join(BASE_DIR,'data/raw/arango_playlist.txt')
ARANGO_MUSIC_FILEPATH = os.path.join(BASE_DIR,'data/raw/arango_music.txt')
MUSIC_NAME_FILEPATH = os.path.join(BASE_DIR,'data/raw/music_name.txt')
ALBUM_NAME_FILEPATH = os.path.join(BASE_DIR,'data/raw/album_name.txt')
PLAYLIST_DESC_FILEPATH = os.path.join(BASE_DIR,'data/raw/playlist_desc.txt')
PLAYLIST_NAME_FILEPATH = os.path.join(BASE_DIR,'data/raw/playlist_name.txt')
LYRIC_FILEPATH = os.path.join(BASE_DIR,'data/raw/lyric.txt')
COMMENT_FILEPATH = os.path.join(BASE_DIR,'data/raw/comment.txt')

# ARANGO RESULT DIRECTORY os.path.join(BASE_DIR,'')
RESULT_PLAYLIST_VERTEXPATH = os.path.join(BASE_DIR,'res/graph/playlist/vertex_playlist.json')
RESULT_PLAYLIST_EDGEPATH = os.path.join(BASE_DIR,'res/graph/playlist/edge_playlist.json')
RESULT_MUSIC_VERTEXPATH = os.path.join(BASE_DIR,'res/graph/playlist/vertex_music.json')
RESULT_MUSIC_EDGEPATH = os.path.join(BASE_DIR,'res/graph/playlist/edge_music.json')
RESULT_ARTIST_VERTEXPATH = os.path.join(BASE_DIR,'res/graph/playlist/vertex_artist.json')
RESULT_ARTIST_EDGEPATH = os.path.join(BASE_DIR,'res/graph/playlist/edge_artist.json')
RESULT_ALBUM_VERTEXPATH = os.path.join(BASE_DIR,'res/graph/playlist/vertex_album.json')
RESULT_ALBUM_EDGEPATH = os.path.join(BASE_DIR,'res/graph/playlist/edge_album.json')
RESULT_ALBUM_ARTIST_EDGEPATH = os.path.join(BASE_DIR,'res/graph/playlist/edge_album_artist.json')

RESULT_ALBUM_NAME_VERTEXPATH = os.path.join(BASE_DIR,'res/graph/ner/vertex_album_name.json')
RESULT_ALBUM_NAME_EDGEPATH = os.path.join(BASE_DIR,'res/graph/ner/edge_album_name.json')
RESULT_PLAYLIST_NAME_VERTEXPATH = os.path.join(BASE_DIR,'res/graph/ner/vertex_playlist_name.json')
RESULT_PLAYLIST_NAME_EDGEPATH = os.path.join(BASE_DIR,'res/graph/ner/edge_playlist_name.json')
RESULT_MUSIC_NAME_VERTEXPATH = os.path.join(BASE_DIR,'res/graph/ner/vertex_music_name.json')
RESULT_MUSIC_NAME_EDGEPATH = os.path.join(BASE_DIR,'res/graph/ner/edge_music_name.json')
RESULT_PLAYLIST_DESC_VERTEXPATH = os.path.join(BASE_DIR,'res/graph/ner/vertex_playlist_desc.json')
RESULT_PLAYLIST_DESC_EDGEPATH = os.path.join(BASE_DIR,'res/graph/ner/edge_playlist_desc.json')

# KEYWORDS RESULT DIRECTORY
RESULT_COMMENT_KEYWORDS_PATH = os.path.join(BASE_DIR,'res/keywords/keywords_comment.txt')
RESULT_LYRIC_KEYWORDS_PATH = os.path.join(BASE_DIR,'res/keywords/keywords_lyric.txt')
RESULT_DESC_KEYWORDS_PATH = os.path.join(BASE_DIR,'res/keywords/keywords_playlist_desc.txt')

# NER RESULT DIRECTORY
RESULT_ALBUM_NAME_NER_PATH = os.path.join(BASE_DIR,'res/ner/ner_album_name.txt')
RESULT_MUSIC_NAME_NER_PATH = os.path.join(BASE_DIR,'res/ner/ner_music_name.txt')
RESULT_PLAYLIST_DESC_NER_PATH = os.path.join(BASE_DIR,'res/ner/ner_playlist_desc.txt')
RESULT_PLAYLIST_NAME_NER_PATH = os.path.join(BASE_DIR,'res/ner/ner_playlist_name.txt')



