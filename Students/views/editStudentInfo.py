# -*- coding: utf-8 -*-
# @Time : 2022/7/17 20:49
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : editStudentInfo.py
# @Project : DataStructureManagementSystem
from django.http import JsonResponse
from pymysql.cursors import DictCursor
from utils.SQL.GenerateSQL import SQLOperation

from Students.views.form import EditStuInfoForm


def editStudentInfo(request, stu_id):
    if request.method == "GET":
        sql = f"""
        select t1.id, t1.stu_name,t1.stu_img, t1.stu_id, t1.stu_gender, t2.class_name
            from Students_student t1,
            Teachers_classes t2
        where t1.Class_id = t2.id
            and t1.id = {stu_id};
        """
        sql_res = SQLOperation(cursor_class=DictCursor).run_sql(sql=sql, operation="SELECT")
        if len(sql_res) == 0:
            return JsonResponse({
                'status': False,
                'errmsg': "学生的id不正确，或该id的学生不存在。"
            })
        return JsonResponse({
            'status': True,
            'stu_info': sql_res[0]
        })
    form = EditStuInfoForm(data=request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        sql = f"""
        update Students_student
            set stu_name='{form_data['stu_name']}',
                stu_img='{form_data['stu_img']}',
                stu_gender={form_data['stu_gender']}
            where id = {stu_id};
        """
        try:
            sql_res = SQLOperation(cursor_class=DictCursor).run_sql(sql=sql, operation='UPDATE')
            if sql_res:
                return JsonResponse({
                    'status': True,
                    'msg': "信息修改成功。"
                })
            return JsonResponse({
                'status': False,
                'errmsg': "服务器出现故障，请稍后重试。"
            })
        except Exception as e:
            return JsonResponse({
                'status': False,
                'errmsg': "服务器出现故障，请稍后重试。"
            })

    return JsonResponse({
        'status': False,
        'errmsg': form.errors
    })
