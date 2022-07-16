# -*- coding: utf-8 -*-
# @Time : 2022/7/16 20:04
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : getQuestionDescInfo.py
# @Project : DataStructureManagementSystem
from utils.SQL.runMYSQL import SQLOperation
from django.http import JsonResponse
from pymysql.cursors import DictCursor


def getQuestionDescInfo(request, ques_id):
    if request.method == "GET":
        sql = f"""
        select t1.id,
               t1.ques_name,
               t2.ques_detail,
               t2.total_students_finish,
               t2.ques_category,
               t2.memory_limit,
               t2.time_limit
        from Questions_questionbank t1,
             (select t1.id, t1.ques_detail, t1.total_students_finish, t2.ques_category, t1.memory_limit, t1.time_limit
             from Questions_questionbankdesc t1,
                  Questions_questioncategory t2
             where t1.category_id = t2.id) t2
        where t1.desc_id = t2.id
           and t1.id = {ques_id};
        """
        sql_res = SQLOperation(cursor_class=DictCursor).run_sql(sql=sql, operation='SELECT')
        if len(sql_res) == 0:
            return JsonResponse({
                'status': False,
                'errmsg': "该题目的信息不存在，请重试，或者重新上传题目。"
            })
        return JsonResponse({
            'status': True,
            'ques_desc': sql_res[0]
        })
    return JsonResponse({
        'status': False,
        'errmsg': "该接口只支持GET请求。"
    })
