# coding:utf-8
import sys
sys.path.append('../')
sys.path.append('../lib')
from app import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)