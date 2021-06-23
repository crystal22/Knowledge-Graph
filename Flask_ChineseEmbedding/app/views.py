# coding:utf-8
import datetime
from app import app
from app import logger
from app import music_model,wv_from_text
from lib.utils import *
from flask import request, render_template, jsonify


@app.route('/')
@app.route('/index',methods=['GET'])
def index():
    content = md2html('./app/static/index.md')
    return render_template('index.html',content = content)
#
@app.route('/api/similar_general/<word>',methods=['POST'])
def api_similar_general(word):
    if request.method == 'POST':
        logger.info('{} API输入：{}'.format(datetime.datetime.now(),word))
        wv_from_text.init_sims(replace=True)
        if word in wv_from_text.wv.vocab.keys():
            vec = wv_from_text[word]
            result = wv_from_text.most_similar(positive=[vec], topn=10)
        else:
            result = '没有结果'
        return jsonify({"type":"general", "keywords": word, "most similar": result})

@app.route('/similar_general',methods=['POST','GET'])
def similar_general():
    if request.method == 'GET':
        return render_template('similar_general.html', type='api')
    else:
        user_input = request.form.get('keywords')
        logger.info('{} 网页输入：{}'.format(datetime.datetime.now(), user_input))
        # init_sims：使得模型的存储更加高效
        wv_from_text.init_sims(replace=True)
        # vocab.keys：词向量表
        if user_input in wv_from_text.wv.vocab.keys():
            vec = wv_from_text[user_input]
            # 找到前n个最相似的词。正词对相似性有正面贡献，负词对相似性有负面影响。
            result = wv_from_text.most_similar(positive=[vec], topn=10)
        else:
            result = '没有结果'
        return render_template('similar_general.html',user_input=user_input,result=result)

@app.route('/api/similar_music/<word>',methods=['POST'])
def api_similar_music(word):
    if request.method == 'POST':
        logger.info('{} API输入：{}'.format(datetime.datetime.now(),word))
        wv_from_text.init_sims(replace=True)
        try:
            result = music_model.wv.most_similar(positive=[word], topn=10)
        except:
            result = '没有结果'
        return jsonify({"type":"music", "keywords": word, "most similar": result})

@app.route('/similar_music',methods=['POST','GET'])
def similar_music():
    if request.method == 'GET':
        return render_template('similar_music.html', type='api')
    else:
        user_input = request.form.get('keywords')
        logger.info('{} 网页输入：{}'.format(datetime.datetime.now(), user_input))
        # init_sims：使得模型的存储更加高效
        wv_from_text.init_sims(replace=True)
        try:
            result = music_model.wv.most_similar(positive=[user_input], topn=10)
        except:
            result = '没有结果'
        return render_template('similar_music.html',user_input=user_input,result=result)
