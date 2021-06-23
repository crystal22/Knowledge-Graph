# coding:utf-8
import sys

sys.path.append('../')
import os
import shutil
import datetime
import json
from Web.app import app, csearch, csubsearch
# from app import app, csearch, csubsearch
from Web.lib.captions import *
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        desc = request.form.get('desc')
        video_name = get_video_hash_name(desc)
        # file.save(VIDEO_DIR + video_name)
        # shutil.copy(VIDEO_DIR + video_name,DISPLAY_DIR + video_name)
        # caption_list = get_caption_json(video_name)
        # caption = get_caption_combine(caption_list[:3])
        keywords_desc = csearch.get_keywords(desc)[:3]
        # keywords_caption = csearch.get_keywords(caption)[:(5-len(keywords_desc))]
        # keywords = keywords_desc + keywords_caption


        caption_list = caption = ''
        keywords = ['阅兵']
        print('关键词提取结果：{}'.format(keywords))
        music = csearch.get_search_result(keywords_desc, topK=5, type='graph')
        return render_template('display.html',
                               video_name=video_name,
                               caption_list=caption_list,
                               caption=caption,
                               desc=desc,
                               keywords=keywords,
                               music=music[:10])
    else:
        return render_template('upload.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    desc = 'test'
    video_name = 'test'
    caption_list = {'start':'1','end':'1','sentence':'test'}
    caption = ['test']
    keywords = ['test','test']
    print('关键词提取结果：{}'.format(keywords))
    music = ['test']
    return render_template('display.html',
                           video_name=video_name,
                           caption_list=caption_list,
                           caption=caption,
                           desc=desc,
                           keywords=keywords,
                           music=music[:10])


@app.route('/graph/<music_name>', methods=['GET', 'POST'])
def graph(music_name):
    target = music_name.split('：')[-1]
    print(target)
    data, links = csubsearch.search(target)
    print(data)
    print(links)
    return render_template('graph.html', data=json.dumps(data),
                           link=json.dumps(links))


@app.route('/en_graph', methods=['GET', 'POST'])
def en_home():
    # 0..2
    data = [{'name': 'The National Anthem', 'des': '', 'simbolSize': 100, 'category': 0},
            {'name': 'Military Band of the Chinese People\'s Liberation Army', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Praise to Motherland', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': '70s', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': '80s', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': '90s', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'In The Field Of Hope', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Spring Festival Overture', 'des': '', 'simbolSize': 50, 'category': 1},
            # {'name': 'Welcome March', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Three Rules of Discipline and Eight Points for Attention', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Socialism Is Great', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'China', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'China Radio Choir', 'des': '', 'simbolSize': 50, 'category': 1},
            # {'name': 'Shu Pu', 'des': '', 'simbolSize': 50, 'category': 1},
            # {'name': 'Muting Zhang', 'des': '', 'simbolSize': 50, 'category': 1},
            # {'name': 'Jia Lei', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Liyuan Peng', 'des': '', 'simbolSize': 50, 'category': 1},
            # {'name': 'Ye Zhang', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'China\'s Golden Melody', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'I\'m Going to Year 2000[Collector\'s Edition]', 'des': '', 'simbolSize': 50, 'category': 1},
            # {'name': 'The Road To Revival', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'The Military Band of People', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'I\'m Going to Year 2000', 'des': '', 'simbolSize': 50, 'category': 1},
            # {'name': 'China 1980\'s', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'National anthem of the People\'s Republic of China', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Eyes on the Stars', 'des': '', 'simbolSize': 50, 'category': 1},
            # {'name': 'Muting Zhang\'s Piano Album', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Katioucha', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'The Stirring Soviet Military', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Glorous Return in Triumph', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'China\'s Military March', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Classic Red Songs about China', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Glorous History', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'People\'s Navy Marching Forward', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Volksmarine', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'March of the Volunteers', 'des': '', 'simbolSize': 50, 'category': 1},
            {'name': 'Red East Chorus', 'des': '', 'simbolSize': 50, 'category': 1}
            ]
    links = [{'target': 'Military Band of the Chinese People\'s Liberation Army', 'source': 'The National Anthem', 'name': 'sung by'},
             {'target': 'Praise to Motherland', 'source': 'The National Anthem', 'name': 'belongs to'},
             {'target': '70s', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has tag'},
             {'target': '80s', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has tag'},
             {'target': '90s', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has tag'},
             {'target': 'In The Field Of Hope', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has song'},
             {'target': 'Spring Festival Overture', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has song'},
             # {'target': 'Welcome March', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has song'},
             {'target': 'Three Rules of Discipline and Eight Points for Attention', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has song'},
             {'target': 'Socialism Is Great', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has song'},
             {'target': 'China', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has named entity'},
             # {'target': 'Military Band of the Chinese People\'s Liberation Army', 'source': 'Military Band of the Chinese People\'s Liberation Army', 'name': 'has named entity'},
             {'target': 'China Radio Choir', 'source': 'In The Field Of Hope', 'name': 'sung by'},
             # {'target': 'Shu Pu', 'source': 'In The Field Of Hope', 'name': 'sung by'},
             # {'target': 'Muting Zhang', 'source': 'In The Field Of Hope', 'name': 'sung by'},
             # {'target': 'Jia Lei', 'source': 'In The Field Of Hope', 'name': 'sung by'},
             {'target': 'Liyuan Peng', 'source': 'In The Field Of Hope', 'name': 'sung by'},
             # {'target': 'Ye Zhang', 'source': 'In The Field Of Hope', 'name': 'sung by'},
             {'target': 'China\'s Golden Melody', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             {'target': 'I\'m Going to Year 2000[Collector\'s Edition]', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             # {'target': 'The Road To Revival', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             {'target': 'The Military Band of People', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             {'target': 'I\'m Going to Year 2000', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             # {'target': 'China 1980\'s', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             {'target': 'National anthem of the People\'s Republic of China', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             {'target': 'Praise to Motherland', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             {'target': 'Eyes on the Stars', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             # {'target': 'Muting Zhang\'s Piano Album', 'source': 'In The Field Of Hope', 'name': 'belongs to album'},
             {'target': 'Katioucha', 'source': 'Katioucha', 'name': 'has named entity'},
             {'target': 'Military Band of the Chinese People\'s Liberation Army', 'source': 'Katioucha', 'name': 'sung by'},
             {'target': 'The Stirring Soviet Military', 'source': 'Katioucha', 'name': 'belongs to album'},
             {'target': 'Military Band of the Chinese People\'s Liberation Army', 'source': 'Glorous Return in Triumph', 'name': 'sung by'},
             {'target': 'China\'s Military March', 'source': 'Glorous Return in Triumph', 'name': 'belongs to album'},
             {'target': 'Classic Red Songs about China', 'source': 'Glorous Return in Triumph', 'name': 'belongs to album'},
             {'target': 'Glorous History', 'source': 'Glorous Return in Triumph', 'name': 'belongs to album'},
             {'target': 'Volksmarine', 'source': 'People\'s Navy Marching Forward', 'name': 'has named entity'},
             {'target': 'Military Band of the Chinese People\'s Liberation Army', 'source': 'People\'s Navy Marching Forward', 'name': 'sung by'},
             {'target': 'Praise to Motherland', 'source': 'People\'s Navy Marching Forward', 'name': 'belongs to album'},
             {'target': 'China\'s Military March', 'source': 'People\'s Navy Marching Forward', 'name': 'belongs to album'},
             {'target': 'Military Band of the Chinese People\'s Liberation Army', 'source': 'March of the Volunteers', 'name': 'sung by'},
             {'target': 'Red East Chorus', 'source': 'March of the Volunteers', 'name': 'sung by'}
    ]

    # # 0..1
    # data = [
    #         {'name': 'The National Anthem', 'des': '', 'simbolSize': 100, 'category': 0},
    #         {'name': 'Battle Hymn of the Military', 'des': '', 'simbolSize': 50, 'category': 1},
    #         {'name': 'Jinfan Folk Orchestra', 'des': '', 'simbolSize': 50, 'category': 1},
    #         {'name': 'The 70th anniversary of the victory of the Chinese People\'s War', 'des': '', 'simbolSize': 50, 'category': 1},
    #         {'name': 'Military Band of the Chinese People\'s Liberation Army', 'des': '', 'simbolSize': 50, 'category': 1},
    #         {'name': 'Praise to Motherland', 'des': '', 'simbolSize': 50, 'category': 1}]
    #
    #
    # links = [
    #         {'target': 'The National Anthem', 'source': 'Battle Hymn of the Military', 'name': 'has song'},
    #         {'target': 'The National Anthem', 'source': 'Jinfan Folk Orchestra', 'name': 'has song'},
    #         {'target': 'The National Anthem', 'source': 'The 70th anniversary of the victory of the Chinese People\'s War', 'name': 'has song'},
    #         {'target': 'Military Band of the Chinese People\'s Liberation Army', 'source': 'The National Anthem', 'name': 'sung by'},
    #         {'target': 'Praise to Motherland', 'source': 'The National Anthem', 'name': 'belongs to album'}]
    return render_template('en_graph.html', data=json.dumps(data),
                           link=json.dumps(links))

@app.route('/music', methods=['GET', 'POST'])
def music():
    return render_template('music.html')

