# -*- coding: utf-8 -*-
# @Time : 2022/7/8 16:24
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : ClassInfoOperation.py
# @Project : DataStructureManagementSystem
import os
from utils.pagination import pagination
from utils.SQL.runMYSQL import SQLOperation
from django.http import JsonResponse, Http404


def getClassInfo(request):
    if request.method == "GET":
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "allSql/classSQL/getClassInfo.sql")
        sql = SQLOperation().load_sql(file_path)
        if sql is None:
            return Http404
        all_operation = pagination(request, sql)
        if type(all_operation) is not dict:
            return all_operation
        sql = all_operation['sql']
        exist_page = all_operation['exist_page']
        query_dict = SQLOperation().deal_sql_result(sql, "id", "class_name", "teacher_name")
        if exist_page is None:
            return JsonResponse({
                'status': True,
                'data': query_dict
            })
        return JsonResponse({
            'status': True,
            'page': exist_page,
            'data': query_dict
        })