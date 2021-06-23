# coding:utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from Web.lib.search import CArangoSearch
from Web.lib.graph import CSubGraphSearch

app = Flask(__name__)
bootstrap=Bootstrap(app)
csearch = CArangoSearch()
csubsearch = CSubGraphSearch()

from app import views
