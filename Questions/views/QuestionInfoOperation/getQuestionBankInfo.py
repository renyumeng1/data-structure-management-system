# -*- coding: utf-8 -*-
# @Time : 2022/7/15 19:10
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : getQuestionBankInfo.py
# @Project : DataStructureManagementSystem
from typing import Union, Dict, Optional

from django.http import JsonResponse
from utils.SQL.runMYSQL import SQLOperation
from utils.pagination import pagination


def getQuestionBank(request):
    if request.method == "GET":
        sql = f"""
        select id,ques_name
        from Questions_questionbank;
        """
        all_operation: Union[JsonResponse, Dict[str, Optional[str]]] = pagination(request, sql)
        if type(all_operation) is not dict:
            return all_operation
        sql = all_operation['sql']
        exist_page = all_operation['exist_page']
        query_dict = SQLOperation().deal_sql_result(sql, "id", "ques_name")
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
    return JsonResponse({
        'status': False,
        'errmsg': '该接口只支持GET请求。'
    })
