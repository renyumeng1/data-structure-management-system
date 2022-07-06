# -*- coding: utf-8 -*-
# @Time : 2022/7/6 18:43
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : QuestionInfoOperation.py
# @Project : DataStructureManagementSystem
from utils.run_mysql import SQLOperation
from django.http import JsonResponse, Http404
import os


def getQuestionAllInfo(request):
    if request.method == "GET":
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "./allSql/getQuestionAllInfo.sql")
        sql = SQLOperation.load_sql(file_path)
        if sql is None:
            return Http404
        query_dict = SQLOperation().deal_sql_result(sql, "id", "ques_name", "ques_category", "ques_detail",
                                                    "total_finish")
        return JsonResponse(query_dict, safe=False)
