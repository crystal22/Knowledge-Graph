# coding=utf-8
import hanlp
import jieba.analyse
import re
from hanziconv import HanziConv
import json
from Netease_Graph.lib.config import *
import hashlib

jieba.analyse.set_stop_words(STOPWORDS_FILEPATH)
jieba.load_userdict(USERDICT_FILEPATH)


class CNer:
    def __init__(self):
        self.recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)

    def ner(self, document):
        document = ''.join(re.findall('[\u4e00-\u9fa5a-zA-Z]+', document))
        res = [HanziConv.toSimplified(i[0] + '|' + i[1]) for i in self.recognizer([list(document)])[0] if
               len(i[0]) > 1 and not i[0].islower()]
        return res

    def single_ner(self, input_filepath, output_filepath):
        with open(input_filepath, encoding='utf8') as f:
            content = f.readlines()

        res = []
        for i, c in enumerate(content):
            try:
                id = c.split('\t')[0]
                document = c.split('\t')[1].strip('\n')
                ner_res = set(self.ner(document))
                for n in ner_res:
                    res.append('{}\t{}\n'.format(id, n))
            except Exception as e:
                print(e)

            if i % 100 == 0:
                print('{}/{}'.format(i, len(content)))

        with open(output_filepath, 'w', encoding='utf8') as f:
            f.writelines(res)

    def get_ner(self):
        # self.single_ner(input_filepath=ALBUM_NAME_FILEPATH,output_filepath=RESULT_ALBUM_NAME_NER_PATH)
        self.single_ner(input_filepath=MUSIC_NAME_FILEPATH, output_filepath=RESULT_MUSIC_NAME_NER_PATH)
        self.single_ner(input_filepath=PLAYLIST_DESC_FILEPATH, output_filepath=RESULT_PLAYLIST_DESC_NER_PATH)
        self.single_ner(input_filepath=PLAYLIST_NAME_FILEPATH, output_filepath=RESULT_PLAYLIST_NAME_NER_PATH)

class CNer2json:
    def __init__(self):
        with open(PLAYLIST_DICT_JSONPATH, encoding='utf8') as f:
            self.playlist_name_dict = json.load(f)
        with open(MUSIC_DICT_JSONPATH, encoding='utf8') as f:
            self.music_name_dict = json.load(f)
        with open(ALBUM_DICT_JSONPATH, encoding='utf8') as f:
            self.album_name_dict = json.load(f)

    def get_hash(self, s):
        md5 = hashlib.md5()
        md5.update(s.encode('utf-8'))
        ret = md5.hexdigest()
        return ret

    def get_edge_dict(self, _from, _to, edgeType, fromValue, toValue):
        edge_dic = {}
        edge_dic['_from'] = _from
        edge_dic['_to'] = _to
        edge_dic['Classification'] = 'RELATION'
        edge_dic['edgeType'] = edgeType
        edge_dic['fromValue'] = fromValue
        edge_dic['toValue'] = toValue
        return edge_dic

    def get_entity_dict(self, vertexValue, vertexID, entityType):
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

    def read_from_file(self,filepath):
        with open(filepath, encoding='utf-8') as f:
            content = f.readlines()
        return content

    def arango_playlist_json(self,input_file,output_vertex_file,output_edge_file):
        vertex_output = list()
        edge_output = list()

        content = self.read_from_file(input_file)

        for i, line in enumerate(content):
            playlist_id, ner = line.strip('\n').split('\t')
            playlist_name = self.playlist_name_dict[playlist_id]
            ner_name, ner_type = ner.split('|')
            vertex_dic = self.get_entity_dict(vertexValue=ner_name, vertexID='ner-' + ner_name, entityType='命名实体')
            vertex_dic['ner_type'] = ner_type
            vertex_output.append(str(vertex_dic) + '\n')

            id_hash = self.get_hash('playlist-' + playlist_id)
            edge_dic = self.get_edge_dict(_from=VERTEX_COLLECTION + id_hash,
                                          _to=VERTEX_COLLECTION + vertex_dic['_key'],
                                          edgeType='包含实体',
                                          fromValue=playlist_name,
                                          toValue=vertex_dic['name'])

            print(edge_dic)
            edge_output.append(str(edge_dic) + '\n')

        self.write_to_file(vertex_output,output_vertex_file)
        self.write_to_file(edge_output,output_edge_file)

    def arango_music_json(self):
        vertex_output = list()
        edge_output = list()

        content = self.read_from_file(RESULT_MUSIC_NAME_NER_PATH)

        for i, line in enumerate(content):
            try:
                id, ner = line.strip('\n').split('\t')
                music_name = self.music_name_dict[id]
                ner_name, ner_type = ner.split('|')
            except Exception as e:
                print('Error: ',line, e)

            vertex_dic = self.get_entity_dict(vertexValue=ner_name, vertexID='ner-' + ner_name, entityType='命名实体')
            vertex_dic['ner_type'] = ner_type
            vertex_output.append(str(vertex_dic) + '\n')

            id_hash = self.get_hash('music-' + id)
            edge_dic = self.get_edge_dict(_from=VERTEX_COLLECTION + id_hash,
                                          _to=VERTEX_COLLECTION + vertex_dic['_key'],
                                          edgeType='包含实体',
                                          fromValue=music_name,
                                          toValue=vertex_dic['name'])

            print(edge_dic)
            edge_output.append(str(edge_dic) + '\n')



        self.write_to_file(vertex_output,RESULT_MUSIC_NAME_VERTEXPATH)
        self.write_to_file(edge_output, RESULT_MUSIC_NAME_EDGEPATH)


    def arango_album_json(self):
        vertex_output = list()
        edge_output = list()

        content = self.read_from_file(RESULT_ALBUM_NAME_NER_PATH)

        for i, line in enumerate(content):
            try:
                id, ner = line.strip('\n').split('\t')
                ner_name, ner_type = ner.split('|')
                album_name = self.album_name_dict[id]
            except Exception as e:
                print('Error: ',line, e)
            vertex_dic = self.get_entity_dict(vertexValue=ner_name, vertexID='ner-' + ner_name, entityType='命名实体')
            vertex_dic['ner_type'] = ner_type
            vertex_output.append(str(vertex_dic) + '\n')

            id_hash = self.get_hash('album-' + album_name)
            edge_dic = self.get_edge_dict(_from=VERTEX_COLLECTION + id_hash,
                                          _to=VERTEX_COLLECTION + vertex_dic['_key'],
                                          edgeType='包含实体',
                                          fromValue=album_name,
                                          toValue=vertex_dic['name'])

            print(edge_dic)
            edge_output.append(str(edge_dic) + '\n')

        self.write_to_file(vertex_output,RESULT_ALBUM_NAME_VERTEXPATH)
        self.write_to_file(edge_output, RESULT_ALBUM_NAME_EDGEPATH)

if __name__ == '__main__':
    cner = CNer()
    cner.get_ner()
    cner2json = CNer2json()
    cner2json.arango_playlist_json(input_file=RESULT_PLAYLIST_NAME_NER_PATH,
                                   output_vertex_file=RESULT_PLAYLIST_NAME_VERTEXPATH,
                                   output_edge_file=RESULT_PLAYLIST_NAME_EDGEPATH)
    cner2json.arango_playlist_json(input_file=RESULT_PLAYLIST_DESC_NER_PATH,
                                   output_vertex_file=RESULT_PLAYLIST_DESC_VERTEXPATH,
                                   output_edge_file=RESULT_PLAYLIST_DESC_EDGEPATH)
    cner2json.arango_music_json()
    cner2json.arango_album_json()

