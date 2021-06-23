# coding:utf-8
import sys
sys.path.append('../')
from lib.data2es import CarangoDownload
from lib.config import CORPUS_GRAPH_BASE,VERTEX_GRAPH_BASE
from lib.logger import logger

if __name__ == '__main__':
    CORPUS_GRAPH_NAME = CORPUS_GRAPH_BASE.format(sys.argv[1])
    VERTEX_GRAPH_NAME = VERTEX_GRAPH_BASE.format(sys.argv[1])
    logger.info('--------------------------DOWNLOAD--------------------------')
    logger.info('KB图谱id：    {}'.format(sys.argv[1]))
    logger.info('正在下载{}.'.format(CORPUS_GRAPH_NAME))
    download = CarangoDownload()
    file_path = download.run(CORPUS_GRAPH_NAME)
    logger.info('-------------------------------------------------------------')