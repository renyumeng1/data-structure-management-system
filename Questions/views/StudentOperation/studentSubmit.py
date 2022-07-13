# -*- coding: utf-8 -*-
# @Time : 2022/7/13 17:04
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : studentSubmit.py
# @Project : DataStructureManagementSystem
from Questions.views.form import SubmitQuestion
from Questions.views.StudentOperation.config import mk_ans_dir
from utils.SQL.GenerateSQL import GenerateSQL
from utils.SQL.runMYSQL import SQLOperation

from django.http import JsonResponse
import requests


def submitQuestion(request, ques_id):
    if request.method == "POST":
        form = SubmitQuestion(data=request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            stu_id = form_data['stu_id']
            language = form_data['language']
            form_data['ques_id'] = ques_id
            res = GenerateSQL(table_name='Questions_studentquestionstatus', form_data=form_data,
                              operation='INSERT').run_sql(if_get_id=True)
            if not res['status']:
                return JsonResponse({
                    'status': False,
                    'errmsg': "服务器出现故障，请稍后再试。"
                })
            sql_id = res['id']
            mk_dir_res = requests.get(url=mk_ans_dir).json()
            if not mk_dir_res['status']:
                return JsonResponse({
                    'status': False,
                    'errmsg': "创建答案目录失败，请稍后重试。"
                })
            jud_url = f"http://101.34.38.102:4000/api/jud/{language}/{stu_id}/{ques_id}"
            jud_res = requests.get(url=jud_url).json()

            if not jud_res['status']:
                return JsonResponse(jud_res)
            temp_jud_res = jud_res['judgeResult']
            for key in temp_jud_res:
                if temp_jud_res[key]['ans'] != 'ACCEPT':
                    sql = f"""
                    update Questions_studentquestionstatus set status = '{temp_jud_res[key]['ans']}' where id={sql_id};
                    """
                    sql_res = SQLOperation().run_sql(operation="UPDATE", sql=sql)
                    if sql_res:
                        return JsonResponse({
                            'status': True,
                            'jud_res': temp_jud_res[key]['ans']
                        })
                    return JsonResponse({
                        'status': False,
                        'errmsg': "服务器出现故障，请稍后再试。"
                    })
            sql = f"""
                update Questions_studentquestionstatus set status = 'ACCEPT' where id={sql_id};
                """
            sql_res = SQLOperation().run_sql(operation="UPDATE", sql=sql)
            if sql_res:
                return JsonResponse({
                    'status': True,
                    'jud_res': 'ACCEPT'
                })
            return JsonResponse({
                'status': False,
                'errmsg': "服务器出现故障，请稍后再试。"
            })
        return JsonResponse({
            'status': False,
            'errmsg': form.errors
        })
    return JsonResponse({
        'status': False,
        'errmsg': "该接口只支持POST请求。"
    })
