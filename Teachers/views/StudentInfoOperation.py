# -*- coding: utf-8 -*-
# @Time : 2022/7/6 13:58
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : StudentInfoOperation.py
# @Project : DataStructureManagementSystem
import os

from utils.SQL.runMYSQL import SQLOperation
from utils.SQL.GenerateSQL import GenerateSQL
from Teachers.views.From import AddStudentInfoForm
from django.http import JsonResponse, Http404


def getStuInfo(request):
    if request.method == "GET":
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "./allSql/getStudentInfo.sql")
        sql = SQLOperation.load_sql(file_path)
        if sql is None:
            return Http404
        query_dict = SQLOperation().deal_sql_result(sql, "id", "stu_name", "stu_id", "teacher_name", "class")
        print(query_dict)
        return JsonResponse(query_dict, safe=False)


def addStuInfo(request):
    if request.method == "POST":
        form = AddStudentInfoForm(data=request.POST)
        if form.is_valid():
            stu_data = form.cleaned_data
            status = GenerateSQL(table_name="Students_student", form_data=stu_data).run_sql()
            if status == True:
                return JsonResponse({
                    "status": True
                })
            return JsonResponse({
                "errmsg": status
            })
        return JsonResponse({
            "status": False,
            "errmsg": form.errors
        })
