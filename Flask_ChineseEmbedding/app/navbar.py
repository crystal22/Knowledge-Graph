# coding:utf-8
from flask_nav import Nav
from flask_nav.elements import *

nav = Nav()

nav.register_element('top',
                     Navbar(
                         'Chinese Embedding',
                         View('使用文档', 'index'),
                         View('通用相近词', 'similar_general'),
                         View('音乐相近词', 'similar_music'),
                     ))
