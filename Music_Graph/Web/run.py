# coding:utf-8
import sys
sys.path.append('../')
sys.path.append('./')
sys.path.append('../lib')
from Web.app import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5030, debug=True)
