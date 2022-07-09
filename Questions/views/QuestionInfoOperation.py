# -*- coding: utf-8 -*-
# @Time : 2022/7/6 18:43
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : QuestionInfoOperation.py
# @Project : DataStructureManagementSystem
from typing import Union, Dict, Optional

from utils.SQL.runMYSQL import SQLOperation
from django.http import JsonResponse, Http404
import os

from utils.pagination import pagination


def getQuestionAllInfo(request):
    # 获取题目信息
    if request.method == "GET":
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "./allSql/getQuestionAllInfo.sql")
        sql = SQLOperation.load_sql(file_path)
        if sql is None:
            return Http404
        all_operation: Union[JsonResponse, Dict[str, Optional[str]]] = pagination(request, sql)
        if type(all_operation) is not dict:
            return all_operation
        sql = all_operation['sql']
        exist_page = all_operation['exist_page']
        query_dict = SQLOperation().deal_sql_result(sql, "id", "ques_name", "ques_category", "ques_detail",
                                                    "total_finish")
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


def addQuestionInfo(request):
    # 增添一道新的题目
    if request.method == "POST":
        pass
