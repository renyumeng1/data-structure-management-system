# -*- coding: utf-8 -*-
# @Time : 2022/7/6 19:06
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : urls.py
# @Project : DataStructureManagementSystem

from django.urls import path, include
import Questions

urlpatterns = [
    path('api/question/get/all/info/', include('Teachers.urls', namespace="Questions"))
]
