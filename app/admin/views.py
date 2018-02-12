#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/11 22:54'


from . import admin


@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin</h1>"
