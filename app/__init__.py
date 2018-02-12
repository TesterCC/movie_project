#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/11 22:52'


from flask import Flask

# 创建app对象，用app对象去注册蓝图blueprint
app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)    # url_prefix="/"
app.register_blueprint(admin_blueprint, url_prefix="/admin")

