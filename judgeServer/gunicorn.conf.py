# -*- coding: utf-8 -*-
# @Time : 2022/7/15 2:39
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : gunicorn.conf.py.py
# @Project : DataStructureManagementSystem
workers = 20
worker_class = "gevent"
bind = "0.0.0.0:4000"
