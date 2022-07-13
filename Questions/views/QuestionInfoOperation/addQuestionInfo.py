# -*- coding: utf-8 -*-
# @Time : 2022/7/12 17:43
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : addQuestionInfo.py
# @Project : DataStructureManagementSystem
import os

import requests
from pymysql.cursors import DictCursor
from django.http import JsonResponse

from utils.SQL.runMYSQL import SQLOperation
from utils.mkDir import MakeCodeFileFromDataBase
from Questions.views.form import AddQuestionInfoForm


def addQuestionInfo(request):
    # 增添一道新的题目
    all_path = os.path.dirname(__file__)
    if request.method == "POST":
        form = AddQuestionInfoForm(data=request.POST)
        zip_file_obj = request.FILES.get('case_file')
        if zip_file_obj is None:
            return JsonResponse({
                'status': False,
                'errmsg': "没有上传对应题目的测试样例。"
            })
        if form.is_valid():
            form_data = form.cleaned_data
            sql = f"""
            insert into Questions_questionbankdesc(ques_detail, total_students_finish, category_id, memory_limit,time_limit) 
            value ('{form_data['ques_detail']}', 0, {form_data['category_id']}, '{form_data['memory_limit']}', '{form_data['time_limit']}'); 
            set @id = LAST_INSERT_ID();
            insert into Questions_questionbank(ques_name, desc_id) value ('{form_data['ques_name']}',@id);
            """
            sql_res = SQLOperation().run_sql(sql=sql, operation='INSERT', if_CLIENT=True, if_get_id=True)

            if sql_res['status']:  # 如果sql执行成功，题目信息上传至数据库，开始上传题目测试样例
                get_id_sql = f"""
                select id
                from Questions_questionbank where desc_id = {sql_res['id']};
                """
                ques_id = SQLOperation(cursor_class=DictCursor).run_sql(sql=get_id_sql, operation='SELECT')[0]['id']
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
                    return JsonResponse({
                        'status': res.json()['status'],
                        'msg': '题目添加成功'
                    })
                return JsonResponse({
                    'status': False,
                    'errmsg': "判题服务器出现故障，请稍后重新上传题目"
                })
            return JsonResponse({
                'status': False,
                'errmsg': "传入字段参数有误，请检查后重试。"
            })
        return JsonResponse({
            'status': False,
            'errmsg': form.errors
        })
