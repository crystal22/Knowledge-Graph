import json
from arango import ArangoClient
from Netease_Graph.lib.config import *

# Initialize the ArangoDB client.
class CJson2arango:
    def __init__(self):
        client = ArangoClient()
        self.db = client.db(ARANGODB_DATABASE, username=ARANGODB_USER_NAME, password=ARANGODB_PASSWORD)

    def edge_collections(self):
        if self.db.has_graph(GRAPH_NAME):
            graph = self.db.graph(GRAPH_NAME)
        else:
            graph = self.db.create_graph(GRAPH_NAME)

        if graph.has_edge_definition(EDGE_NAME):
            edge = graph.edge_collection(EDGE_NAME)
        else:
            edge = graph.create_edge_definition(
                edge_collection=EDGE_NAME,
                from_vertex_collections=[VERTEX_NAME],
                to_vertex_collections=[VERTEX_NAME]
            )

        with open(self.edge_filepath, encoding='utf8') as f:
            content = f.readlines()

        for line in content:
            # if '位于' in line:
            print(line)
            try:
                edge.insert(eval(line))
            except Exception as e:
                print(line)
                print(e)
                pass

    def vertex_collections(self):
        if self.db.has_graph(GRAPH_NAME):
            graph = self.db.graph(GRAPH_NAME)
        else:
            print(GRAPH_NAME)
            graph = self.db.create_graph(GRAPH_NAME)

        if graph.has_vertex_collection(VERTEX_NAME):
            vertex = graph.vertex_collection(VERTEX_NAME)
        else:
            vertex = graph.create_vertex_collection(VERTEX_NAME)

        with open(self.vertex_filepath, encoding='utf8') as f:
            content = f.readlines()

        length = len(content)
        for i, line in enumerate(content):
            try:
                vertex.insert(eval(line))
            except Exception as e:
                print(line)
                print(e)
                pass
            if i % 10000 == 0:
                print('{}/{}'.format(i, length))

    def construct(self,vertex_filepath,edge_filepath,type='all'):
        self.vertex_filepath = vertex_filepath
        self.edge_filepath = edge_filepath
        if type == 'all':
            self.vertex_collections()
            self.edge_collections()
        elif type == 'vertex':
            self.vertex_collections()
        elif type == 'edge':
            self.edge_collections()
        else:
            return None

    def run(self):
        self.construct(vertex_filepath=RESULT_PLAYLIST_VERTEXPATH,edge_filepath=RESULT_PLAYLIST_EDGEPATH)
        self.construct(vertex_filepath=RESULT_MUSIC_VERTEXPATH, edge_filepath=RESULT_MUSIC_EDGEPATH)
        self.construct(vertex_filepath=RESULT_ARTIST_VERTEXPATH, edge_filepath=RESULT_ARTIST_EDGEPATH)
        self.construct(vertex_filepath=RESULT_ALBUM_VERTEXPATH, edge_filepath=RESULT_ALBUM_EDGEPATH)
        self.construct(vertex_filepath=None, edge_filepath=RESULT_ALBUM_ARTIST_EDGEPATH,type='edge')
        self.construct(vertex_filepath=RESULT_ALBUM_NAME_VERTEXPATH, edge_filepath=RESULT_ALBUM_NAME_EDGEPATH)
        self.construct(vertex_filepath=RESULT_PLAYLIST_NAME_VERTEXPATH, edge_filepath=RESULT_PLAYLIST_NAME_EDGEPATH)
        self.construct(vertex_filepath=RESULT_MUSIC_NAME_VERTEXPATH, edge_filepath=RESULT_MUSIC_NAME_EDGEPATH)
        self.construct(vertex_filepath=RESULT_PLAYLIST_DESC_VERTEXPATH, edge_filepath=RESULT_PLAYLIST_DESC_EDGEPATH)

if __name__ == '__main__':
    cjson2arango = CJson2arango()
    cjson2arango.run()

