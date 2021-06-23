# coding:utf-8
# 原始视频获取dense video caption，翻译
# input: 原始视频路径、视频描述，保存到/mnt/DenseVideoCaption/test/目录下
# output：分段视频描述/整合视频描述

import sys
sys.path.append('../lib/')

import os
import json
import time
import subprocess
import http.client
import hashlib
import urllib
import random
from Web.lib.config import *
# from config import *

def get_video_hash_name(s):
    # s = s + str(time.time())
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    ret = str(md5.hexdigest()) + '.mp4'
    return ret

def baidu_api(sentence):
    salt = random.randint(32768, 65536)
    sign = APPID + sentence + str(salt) + SECRETKEY
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = URL + '?appid=' + APPID + '&q=' + urllib.parse.quote(
        sentence) + '&from=' + FROMLANG + '&to=' + TOLANG + '&salt=' + str(
        salt) + '&sign=' + sign

    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', url)
    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)
    if httpClient:
        httpClient.close()
    return result['trans_result'][0]['dst']

def get_caption_split(input, trans):
    # input: json file
    # output: json file
    if trans == 'True':
        caption = ''
        output = []
        for line in input:
            if 'fourth' in line['sentence']:
                sentence = line['sentence'].replace('fourth', 'forth') + '\\n'
            elif 'ball' in line['sentence']:
                sentence = line['sentence'].replace('ball', 'basketball') + '\\n'
            else:
                sentence = line['sentence'] + '\\n'
            caption += sentence
        trans_sentence = [i.strip('。') for i in baidu_api(caption).split('\\n') if len(i)>1]

        # for i in input:
        #     print(i)
        #
        # for i in trans_sentence:
        #     print(i)


        for i,line in enumerate(input):
            tmp = {}
            tmp['start'] = line['start']
            tmp['end'] = line['end']
            tmp['sentence'] = trans_sentence[i]
            output.append(tmp)
    else:
        output = input
    return output

def get_caption_combine(input):
    caption = ''
    for line in input:
        sentence = line['sentence'] + '.'
        caption += sentence
    return caption

def get_caption_json(video_name):
    caption_name = '{}.json'.format(os.path.splitext(video_name)[0])
    caption_trans_name = '{}_zh.json'.format(os.path.splitext(video_name)[0])
    features_name = '{}_vggish.npy'.format(os.path.splitext(video_name)[0])
    features_path = FEATURES_DIR + features_name
    caption_path = CAPTION_DIR + caption_name
    caption_trans_path = CAPTION_DIR + caption_trans_name
    if not os.path.exists(features_path):
        print('正在生成{}的视频特征文件.'.format(video_name))
        subprocess.call(['/bin/bash',SHELL_RUN_FEATURES_PATH,video_name])
    print('视频特征文件的路径为：{}'.format(features_path))
    print('视频描述文件的路径为：{}'.format(caption_path))
    if not os.path.exists(caption_path):
        print('正在生成{}的视频描述文件.'.format(video_name))
        subprocess.call(['/bin/bash', SHELL_RUN_CAPTIONS_PATH, video_name])

    with open(caption_path,encoding='utf-8') as f:
        content = json.load(f)
    translated = get_caption_split(content,trans='True')[:5]
    with open(caption_trans_path,'w',encoding='utf-8') as f:
        json.dump(translated,f,ensure_ascii=False)
    print('视频{}的视频描述内容为：\n【{}】'.format(video_name, translated))
    return translated


if __name__ == '__main__':
    caption_path = 'D:/Graduate/Music_Graph/Web/app/static/caption/1.json'
    caption_tras_path = 'D:/Graduate/Music_Graph/Web/app/static/caption/1_zh.json'
    with open(caption_path,encoding='utf-8') as f:
        content = json.load(f)

    translated = get_caption_split(content,trans='True')[:5]

    with open(caption_tras_path,'w',encoding='utf-8') as f:
        json.dump(translated,f,ensure_ascii=False)

    captions = get_caption_combine(translated[:3])


















