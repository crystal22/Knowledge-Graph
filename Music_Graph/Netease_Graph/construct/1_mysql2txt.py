# coding=utf-8
import pymysql
import os
import sys
import json
sys.path.append('../lib/')
from Netease_Graph.lib.config import *

class CDatafromMySQL:
    def __init__(self):
        self.mysql = pymysql.connect(host=MYSQL_HOST,
                                     user=MYSQL_USERNAME,
                                     passwd=MYSQL_PASSWORD,
                                     db=MYSQL_DATABASE,
                                     port=MYSQL_PORT)
        self.cursor = self.mysql.cursor()

    def playlist_from_mysql(self):
        '''
        获取arango_playlist.txt文件
        :return:
        '''
        self.cursor.execute('''
        UPDATE playlist SET playlist_desc = REPLACE(REPLACE(REPLACE(playlist_desc,
         CHAR(10), ' '), CHAR(13), ' '), CHAR(9), ' ');''')
        self.mysql.commit()
        self.cursor.execute('''
        select playlist_id, playlist_name, playlist_tag, playlist_pubtime,
        playlist_desc, playlist_fav_count from playlist into outfile '{}' '''.format(ARANGO_PLAYLIST_FILEPATH))
        self.mysql.commit()

    def music_from_mysql(self):
        '''
        获取arango_music.txt文件
        :return:
        '''
        self.cursor.execute('''
        select music_id, playlist_id, music_name, artist_name, album_name from music into outfile '{}' '''.format(ARANGO_MUSIC_FILEPATH))
        self.mysql.commit()

    def comment_from_mysql(self):
        self.cursor.execute('''
        UPDATE comment SET comment_content = REPLACE(REPLACE(REPLACE(comment_content,
         CHAR(10), ' '), CHAR(13), ' '), CHAR(9), ' ');''')
        self.mysql.commit()
        self.cursor.execute('''
        select music_id, group_concat(comment_content) from comment group by music_id into outfile '{}' '''.format(COMMENT_FILEPATH))
        self.mysql.commit()

    def lyric_from_mysql(self):
        self.cursor.execute('''
        UPDATE lyric SET lyric = REPLACE(REPLACE(REPLACE(lyric,
         CHAR(10), ' '), CHAR(13), ' '), CHAR(9), ' ');''')
        self.mysql.commit()
        self.cursor.execute('''
        select music_id, lyric from lyric into outfile '{}' '''.format(LYRIC_FILEPATH))
        self.mysql.commit()

    def music_name_from_mysql(self):
        self.cursor.execute('''
        select music_id, music_name from music into outfile '{}' '''.format(MUSIC_NAME_FILEPATH))
        self.mysql.commit()

    def album_name_from_mysql(self):
        self.cursor.execute('''
        select music_id, album_name from music into outfile '{}' '''.format(ALBUM_NAME_FILEPATH))
        self.mysql.commit()

    def playlist_name_from_mysql(self):
        self.cursor.execute('''
        select playlist_id, playlist_name from playlist into outfile '{}' '''.format(PLAYLIST_NAME_FILEPATH))
        self.mysql.commit()

    def playlist_desc_from_mysql(self):
        self.cursor.execute('''
        UPDATE playlist SET playlist_desc = REPLACE(REPLACE(REPLACE(playlist_desc,
         CHAR(10), ' '), CHAR(13), ' '), CHAR(9), ' ');''')
        self.mysql.commit()
        self.cursor.execute('''
        select playlist_id, playlist_desc from playlist into outfile '{}' '''.format(PLAYLIST_DESC_FILEPATH))
        self.mysql.commit()

    def playlist_txt_from_mysql(self):
        self.cursor.execute('''
        select playlist_id,playlist_name from playlist into outfile '{}' '''.format(PLAYLIST_DICT_TXTPATH))
        self.mysql.commit()

    def playlist_dict_from_txt(self):
        res = {}
        with open(PLAYLIST_DICT_TXTPATH, encoding='utf8') as f:
            content = f.readlines()
            for c in content:
                key, value = c.split('\t')
                res[key] = value.strip()

        with open(PLAYLIST_DICT_JSONPATH,'w',encoding='utf8') as f:
            json.dump(res,f,indent=4,ensure_ascii=False)

    def music_dict_from_txt(self):
        res = {}
        with open(MUSIC_NAME_FILEPATH, encoding='utf8') as f:
            content = f.readlines()
            for c in content:
                key, value = c.split('\t')
                res[key] = value.strip()

        with open(MUSIC_DICT_JSONPATH,'w',encoding='utf8') as f:
            json.dump(res,f,indent=4,ensure_ascii=False)

    def album_dict_from_txt(self):
        res = {}
        with open(ALBUM_NAME_FILEPATH, encoding='utf8') as f:
            content = f.readlines()
            for c in content:
                key, value = c.split('\t')
                res[key] = value.strip()

        with open(ALBUM_DICT_JSONPATH,'w',encoding='utf8') as f:
            json.dump(res,f,indent=4,ensure_ascii=False)

    def get_data_for_arango(self):
        self.playlist_from_mysql()
        self.music_from_mysql()
        self.playlist_txt_from_mysql()
        self.playlist_dict_from_txt()

    def get_data_for_keywords_extraction(self):
        self.playlist_desc_from_mysql()
        self.playlist_name_from_mysql()
        self.lyric_from_mysql()
        self.comment_from_mysql()
        self.music_name_from_mysql()
        self.album_name_from_mysql()

    def get_data_for_ner(self):
        self.music_dict_from_txt()
        self.album_dict_from_txt()

if __name__ == '__main__':
    cDatafromMySQL = CDatafromMySQL()
    cDatafromMySQL.get_data_for_arango()
    cDatafromMySQL.get_data_for_keywords_extraction()
    cDatafromMySQL.get_data_for_ner()
    cDatafromMySQL.cursor.close()
    cDatafromMySQL.mysql.close()
