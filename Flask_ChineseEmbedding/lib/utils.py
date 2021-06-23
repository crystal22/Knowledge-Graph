# coding:utf-8
from flask import Markup
import markdown

def md2html(filename):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.tables',
            'markdown.extensions.toc']
    with open(filename, 'r',encoding='utf-8') as f:
        mdcontent = f.read()
    html = markdown.markdown(mdcontent, extensions=exts)
    content = Markup(html)
    return content