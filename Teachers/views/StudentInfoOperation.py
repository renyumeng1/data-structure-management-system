# -*- coding: utf-8 -*-
# @Time : 2022/7/6 13:58
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : StudentInfoOperation.py
# @Project : DataStructureManagementSystem
from utils.run_mysql import SQLOperation
from django.http import JsonResponse


def getStuInfo(request):
    if request.method == "GET":
        SQL = """
                select result.id,result.stu_name,result.stu_id,result.teacher_name,tc.class_name
              from (select t1.id,t1.stu_name, t1.stu_id, t1.Class_id, t2.teacher_name
              from students_student t1,
                   teachers_teacher t2
              where t1.teacher_id = t2.id) result,
                   teachers_classes tc
              where result.Class_id = tc.id;
                """
        query_dict = SQLOperation().deal_sql_result(SQL, "id", "stu_name", "stu_id", "teacher_name", "class_id")
        return JsonResponse(query_dict, safe=False)
