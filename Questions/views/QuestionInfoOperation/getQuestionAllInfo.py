# -*- coding: utf-8 -*-
# @Time : 2022/7/12 17:36
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : getQuestionAllInfo.py
# @Project : DataStructureManagementSystem
import os
from typing import Union, Dict, Optional
from django.http import JsonResponse, Http404
from utils.SQL.runMYSQL import SQLOperation
from utils.pagination import pagination


def getQuestionAllInfo(request):
    # 获取题目信息
    if request.method == "GET":
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "../allSql/questionSQL/getQuestionAllInfo.sql")
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
