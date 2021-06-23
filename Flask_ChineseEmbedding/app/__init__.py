# coding:utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from app.navbar import nav
from gensim.models import KeyedVectors
from lib.config import *
import logging
from gensim.models import word2vec

app = Flask(__name__)
bootstrap=Bootstrap(app)
nav.init_app(app)
print('正在加载通用模型...')
wv_from_text = KeyedVectors.load_word2vec_format(GENERAL_MODEL_FILE, binary=False) # 加载时间比较长
print('通用模型加载完毕！')
print('正在加载音乐模型...')
music_model = word2vec.Word2Vec.load(MUSIC_MODEL_FILE)
print('音乐模型加载完毕！')

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler(os.path.join(BASE_DIR,'log/flask.log'))
handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

from app import views

