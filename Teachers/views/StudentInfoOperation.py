# -*- coding: utf-8 -*-
# @Time : 2022/7/6 13:58
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : StudentInfoOperation.py
# @Project : DataStructureManagementSystem
import os
from utils.run_mysql import SQLOperation
from django.http import JsonResponse, Http404


def getStuInfo(request):
    if request.method == "GET":
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "./allSql/getStudentInfo.sql")
        sql = SQLOperation.load_sql(file_path)
        if sql is None:
            return Http404
        query_dict = SQLOperation().deal_sql_result(sql, "id", "stu_name", "stu_id", "teacher_name", "class")
        return JsonResponse(query_dict, safe=False)
