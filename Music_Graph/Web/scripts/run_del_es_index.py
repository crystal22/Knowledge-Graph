# coding:utf-8
import sys
sys.path.append('../')
from lib.del_es_index import CesIndexDel

if __name__ == '__main__':
    es_index_del = CesIndexDel()
    es_index_del.run(index_name=sys.argv[1])
