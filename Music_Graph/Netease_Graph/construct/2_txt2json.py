# coding=utf-8
import pymysql
import os
import json
from Netease_Graph.lib.config import *
import hashlib

class CTxt2json:
    def __init__(self):
        with open(PLAYLIST_DICT_JSONPATH,encoding='utf8') as f:
            self.playlist_name_dict = json.load(f)

    def get_hash(self,s):
        md5 = hashlib.md5()
        md5.update(s.encode('utf-8'))
        ret = md5.hexdigest()
        return ret

    def get_edge_dict(self,_from, _to, edgeType, fromValue, toValue):
        edge_dic = {}
        edge_dic['_from'] = _from
        edge_dic['_to'] = _to
        edge_dic['Classification'] = 'RELATION'
        edge_dic['edgeType'] = edgeType
        edge_dic['fromValue'] = fromValue
        edge_dic['toValue'] = toValue
        return edge_dic

    def get_entity_dict(self,vertexValue, vertexID, entityType):
        vertex_dic = {}
        vertex_dic['classification'] = 'ENTITY'
        id_hash = self.get_hash(vertexID)
        vertex_dic['_key'] = id_hash
        vertex_dic['name'] = vertexValue
        vertex_dic['type'] = entityType
        vertex_dic['mysql_id'] = vertexID
        return vertex_dic

    def write_to_file(self,data,filepath):
        with open(filepath, 'w', encoding='utf8') as f:
            f.writelines(list(set(data)))

    def arango_playlist_json(self):
        vertex_output = list()
        edge_output = list()
        with open(ARANGO_PLAYLIST_FILEPATH, encoding='utf-8') as f:
            content = f.readlines()
            print(len(set(content)))

        for i,line in enumerate(content):
            try:
                playlist_id,playlist_name,playlist_tag,playlist_pubtime,\
                playlist_desc,playlist_fav_count=line.split('\t')
            except:
                print('Error' + ''.join(line.split('\t')))
                continue

            # playlist_id 歌单id
            # playlist_name 歌单名称
            # playlist_tag 歌单标签
            # playlist_pubtime 发布时间
            # playlist_desc 歌单描述
            # playlist_fav_count 点赞数

            playlist_vertex_dic = self.get_entity_dict(vertexValue=playlist_name,vertexID='playlist-'+playlist_id,entityType='歌单名称')
            playlist_vertex_dic['pubtime'] = playlist_pubtime
            playlist_vertex_dic['description'] = playlist_desc
            playlist_vertex_dic['fav_count'] = playlist_fav_count.strip('\n')
            vertex_output.append(str(playlist_vertex_dic) + '\n')

            tag_name_list = playlist_tag.split(',')
            for i in range(len(tag_name_list)):
                tag_name = tag_name_list[i]
                if tag_name:
                    tag_vertex_dic = self.get_entity_dict(vertexValue=tag_name, vertexID='tag-'+ tag_name, entityType='歌单标签')
                    vertex_output.append(str(tag_vertex_dic) + '\n')
                    tag_edge_dic = self.get_edge_dict(_from=VERTEX_COLLECTION + playlist_vertex_dic['_key'],
                                             _to=VERTEX_COLLECTION + tag_vertex_dic['_key'],
                                             edgeType='分类标签为',
                                             fromValue=playlist_vertex_dic['name'],
                                             toValue=tag_vertex_dic['name'])

                    edge_output.append(str(tag_edge_dic) + '\n')

        self.write_to_file(vertex_output,RESULT_PLAYLIST_VERTEXPATH)
        self.write_to_file(edge_output,RESULT_PLAYLIST_EDGEPATH)

    def arango_music_json(self):
        music_vertex_output = list()
        music_edge_output = list()
        artist_vertex_output = list()
        artist_edge_output = list()
        album_vertex_output = list()
        album_edge_output = list()
        album_artist_edge_output = list()

        with open(ARANGO_MUSIC_FILEPATH, encoding='utf8') as f:
            content = f.readlines()

        for line in content:
            try:
                music_id, playlist_ids, music_name, artist_name, album_name = line.strip().split('\t')
            except:
                print(line.strip().split('\t'))
                continue

            # music_id 歌曲id
            # playlist_id 歌单id
            # music_name 歌曲名称
            # playlist_name 歌单名称
            # artist_name 歌手名称
            # album_name 专辑名称

            music_vertex_dic = self.get_entity_dict(vertexValue=music_name, vertexID='music-' + music_id,
                                                    entityType='歌曲名称')
            music_vertex_dic['artist'] = artist_name
            music_vertex_dic['album'] = album_name

            artist_vertex_dic = self.get_entity_dict(vertexValue=artist_name, vertexID='artist-' + artist_name,
                                                    entityType='歌手名称')

            album_vertex_dic = self.get_entity_dict(vertexValue=album_name, vertexID='album-' + album_name,
                                                    entityType='专辑名称')


            artist_edge_dic = self.get_edge_dict(_from=VERTEX_COLLECTION + music_vertex_dic['_key'],
                                              _to=VERTEX_COLLECTION + artist_vertex_dic['_key'],
                                              edgeType='演唱者是',
                                              fromValue=music_vertex_dic['name'],
                                              toValue=artist_vertex_dic['name'])

            album_edge_dic = self.get_edge_dict(_from=VERTEX_COLLECTION + music_vertex_dic['_key'],
                                              _to=VERTEX_COLLECTION + album_vertex_dic['_key'],
                                              edgeType='属于专辑',
                                              fromValue=music_vertex_dic['name'],
                                              toValue=album_vertex_dic['name'])

            album_artist_edge_dic = self.get_edge_dict(_from=VERTEX_COLLECTION + album_vertex_dic['_key'],
                                              _to=VERTEX_COLLECTION + artist_vertex_dic['_key'],
                                              edgeType='属于歌手',
                                              fromValue=album_vertex_dic['name'],
                                              toValue=artist_vertex_dic['name'])


            music_vertex_output.append(str(music_vertex_dic) + '\n')
            album_vertex_output.append(str(album_vertex_dic) + '\n')
            artist_vertex_output.append(str(artist_vertex_dic) + '\n')
            artist_edge_output.append(str(artist_edge_dic) + '\n')
            album_edge_output.append(str(album_edge_dic) + '\n')
            album_artist_edge_output.append(str(album_artist_edge_dic) + '\n')

            playlist_ids = playlist_ids.split(',')
            for playlist_id in playlist_ids:
                playlist_name = self.playlist_name_dict[playlist_id]
                playlist_vertex_dic = self.get_entity_dict(vertexValue=playlist_name,
                                                           vertexID='playlist-' + playlist_id,
                                                           entityType='歌单名称')

                music_edge_dic = self.get_edge_dict(_from=VERTEX_COLLECTION + playlist_vertex_dic['_key'],
                                         _to=VERTEX_COLLECTION + music_vertex_dic['_key'],
                                         edgeType='包含歌曲',
                                         fromValue=playlist_vertex_dic['name'],
                                         toValue=music_vertex_dic['name'])

                music_edge_output.append(str(music_edge_dic) + '\n')

        self.write_to_file(music_vertex_output, RESULT_MUSIC_VERTEXPATH)
        self.write_to_file(music_edge_output, RESULT_MUSIC_EDGEPATH)
        self.write_to_file(artist_vertex_output, RESULT_ARTIST_VERTEXPATH)
        self.write_to_file(artist_edge_output, RESULT_ARTIST_EDGEPATH)
        self.write_to_file(album_vertex_output, RESULT_ALBUM_VERTEXPATH)
        self.write_to_file(album_edge_output, RESULT_ALBUM_EDGEPATH)
        self.write_to_file(album_artist_edge_output, RESULT_ALBUM_ARTIST_EDGEPATH)

if __name__ == '__main__':
    ctxt2json = CTxt2json()
    ctxt2json.arango_playlist_json()
    ctxt2json.arango_music_json()
