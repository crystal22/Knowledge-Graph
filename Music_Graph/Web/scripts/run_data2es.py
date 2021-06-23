# coding:utf-8
import sys
sys.path.append('../')
from lib.data2es import Craw2es,Carango2es
from lib.config import CORPUS_GRAPH_BASE,VERTEX_GRAPH_BASE,\
    ES_INDEX_BASE,ES_RAW_INDEX_BASE
from lib.logger import logger

if __name__ == '__main__':
    CORPUS_GRAPH_NAME = CORPUS_GRAPH_BASE.format(sys.argv[1])
    VERTEX_GRAPH_NAME = VERTEX_GRAPH_BASE.format(sys.argv[1])
    ES_INDEX = ES_INDEX_BASE.format(sys.argv[1])
    ES_RAW_INDEX = ES_RAW_INDEX_BASE.format(sys.argv[1])

    logger.info('---------------------------DATA2ES---------------------------')
    logger.info('KB图谱id：\t{}'.format(sys.argv[1]))
    logger.info('KB ES索引：\t{}'.format(ES_INDEX))
    logger.info('基础ES索引：\t{}'.format(ES_RAW_INDEX))
    logger.info('正在导入{}.'.format(CORPUS_GRAPH_NAME))
    arango2es = Carango2es(graph_id=sys.argv[1])
    es_actions = arango2es.get_aql_result(vertex_graph_name=VERTEX_GRAPH_NAME,
                                          corpus_graph_name=CORPUS_GRAPH_NAME,
                                          es_index=ES_INDEX)
    arango2es.data2es(es_actions)
    raw2es = Craw2es()
    raw2es.run(corpus_graph_name=CORPUS_GRAPH_NAME,es_raw_index=ES_RAW_INDEX)
    logger.info('导入完成.')
    logger.info('-------------------------------------------------------------')