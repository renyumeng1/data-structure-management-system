# -*- coding: utf-8 -*-
# @Time : 2022/7/12 18:35
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : updateQuestionInfo.py
# @Project : DataStructureManagementSystem
import os

import requests

from utils.SQL.runMYSQL import SQLOperation
from Questions.views.form import AddQuestionInfoForm
from django.http import JsonResponse
from pymysql.cursors import DictCursor

from utils.mkDir import MakeCodeFileFromDataBase


def updateQuestionInfo(request, ques_id):
    all_path = os.path.dirname(__file__)
    form = AddQuestionInfoForm(data=request.POST)
    zip_file_obj = request.FILES.get('case_file')
    if zip_file_obj is None:
        return JsonResponse({
            'status': False,
            'errmsg': "没有上传对应题目的测试样例。"
        })
    if request.method == "GET":
        sql = f"""
        select res.id, res.ques_name, res.ques_detail, Qc.ques_category, res.memory_limit, res.time_limit
        from Questions_questioncategory Qc,
        (select t1.id, t1.ques_name, t2.ques_detail, t2.category_id, t2.memory_limit, t2.time_limit
        from Questions_questionbank t1,
            Questions_questionbankdesc t2
        where t1.desc_id = t2.id) as res
        where res.category_id = Qc.id
        and res.id = {ques_id};
        """
        sql_res = SQLOperation(cursor_class=DictCursor).run_sql(sql=sql, operation='SELECT', if_CLIENT=True)
        if (len(sql_res)) != 0:
            return JsonResponse({
                'status': True,
                'selectResult': sql_res[0]
            })
        return JsonResponse({
            'status': False,
            'errmsg': '请求的题目不存在，请重试'
        })
    if form.is_valid():
        form_data = form.cleaned_data
        sql = f"""
        update Questions_questionbank t1,Questions_questionbankdesc t2
        set t1.ques_name='{form_data['ques_name']}',
            t2.ques_detail='{form_data['ques_detail']}',
            t2.category_id={form_data['category_id']},
            t2.time_limit='{form_data['time_limit']}',
            t2.memory_limit='{form_data['memory_limit']}'
        where t1.id = {ques_id}
          and t2.id = t1.desc_id;
        """
        temp_file_path = '../tempFile'
        if not os.path.exists(temp_file_path):
            temp_file_path = MakeCodeFileFromDataBase.mkdir(temp_file_path)['path']
        temp_file_path = os.path.join(all_path, '../tempFile', zip_file_obj.name)
        with open(temp_file_path, "wb") as f:
            for line in zip_file_obj.chunks():
                f.write(line)
            f.close()
        url = f"http://101.34.38.102:4000/api/create/{ques_id}/case/path"
        s = requests.session()
        s.keep_alive = False
        headers = {'Connection': 'close'}
        with open(temp_file_path, "rb") as f:
            files = {"zip": (zip_file_obj.name, f)}
            res = requests.post(url=url, files=files, verify=False, headers=headers)
            res_msg = res.json()
        if res_msg['status']:
            try:
                os.remove(temp_file_path)
            except:
                pass
            try:
                sql_result = SQLOperation().run_sql(operation="UPDATE", sql=sql)
                if sql_result:
                    return JsonResponse({
                        'status': res.json()['status'],
                        'msg': '题目修改成功'
                    })
            except Exception as e:
                return JsonResponse({
                    'status': False,
                    'errmsg': e
                })
        return JsonResponse({
            'status': False,
            'errmsg': "判题服务器出现故障，请稍后重新修改该题目"
        })
    return JsonResponse({
        'status': False,
        'errmsg': form.errors
    })
