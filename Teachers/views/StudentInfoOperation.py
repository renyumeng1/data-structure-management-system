# -*- coding: utf-8 -*-
# @Time : 2022/7/6 13:58
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : StudentInfoOperation.py
# @Project : DataStructureManagementSystem
import os
from utils.pagination import pagination
from utils.SQL.runMYSQL import SQLOperation
from utils.SQL.GenerateSQL import GenerateSQL
from Teachers.views.form import AddStudentInfoForm
from django.http import JsonResponse, Http404


def getStuInfo(request):
    """
    :param request: 前端发送的请求
    :return: 查询所有学生数据
    """
    if request.method == "GET":
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "allSql/studentSQL/getStudentInfo.sql")
        sql = SQLOperation.load_sql(file_path)
        if sql is None:
            return Http404
        all_operation = pagination(request, sql)
        if type(all_operation) is not dict:
            return all_operation
        sql = all_operation['sql']
        exist_page = all_operation['exist_page']
        query_dict = SQLOperation().deal_sql_result(sql, "id", "stu_name", "stu_id", "teacher_name", "class")
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


def addStuInfo(request):
    """
    :param request: 前端发送的请求
    :return: 添加学生信息
    """
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


def editStudentInfo(request, nid):
    pass
