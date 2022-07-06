# -*- coding: utf-8 -*-
# @Time : 2022/7/6 16:29
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : urls.py
# @Project : DataStructureManagementSystem
from django.urls import path
from Teachers.views import StudentInfoOperation


app_name = "Teachers"
urlpatterns = [
    path('', StudentInfoOperation.getStuInfo, name='list'),
]
