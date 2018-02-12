#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'MFC'
__time__ = '18/2/11 22:54'

import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:yanxi76543210@127.0.0.1/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


class User(db.Model):
    """
    会员
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)   # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))                # 密码
    email = db.Column(db.String(100), unique=True)   # 邮箱
    phone = db.Column(db.String(11), unique=True)    # 手机号码
    info = db.Column(db.Text)                        # 个性简介
    face = db.Column(db.String(255), unique=True)    # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)    # 唯一标志符
    userlogs = db.relationship('Userlog', backref='User')   # 会员日志外键关系关联

    def __repr__(self):
        return "<User %r>" % self.name


class Userlog(db.Model):
    """
    会员登录日志
    """
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)    # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # 所属会员  外键
    ip = db.Column(db.String(100))    # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)    # 登录时间

    def __repr__(self):
        return "<Userlog %r>" % self.id



