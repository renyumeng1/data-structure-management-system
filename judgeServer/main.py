# -*- coding: utf-8 -*-
# @Time : 2022/7/9 22:53
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : main.py
# @Project : DataStructureManagementSystem
import os
import time

from utils.mkDir import MakeCodeFileFromDataBase
from utils.SQL.runMYSQL import SQLOperation
from pymysql.cursors import DictCursor
from flask import Flask
# from gevent import monkey
import logging
import judger

# monkey.patch_all()

app = Flask(__name__)


@app.route('/api/create/path')
def createPath():
    res = MakeCodeFileFromDataBase(sql_path='./allSQL/getJudgeInfo.sql', subs_path='./subs').makeCodeFile
    return {
        'status': True,
        'makeFileStatus': res
    }


@app.route('/api/jud/<language>/<stu_id>/<que_id>')
def JudAPI(stu_id, que_id, language):
    sql = f"""
    select t1.stu_solution, t1.stu_id, t1.ques_id, t2.time_limit, t2.memory_limit
    from Questions_studentquestionstatus t1,
        Questions_questionbankdesc t2
    where t1.stu_id = {stu_id}
    and t1.ques_id = {que_id}
    and t1.status = '0'
    and t2.id = t1.ques_id;
    """
    sql_res = SQLOperation(cursor_class=DictCursor).run_sql(sql=sql, operation='SELECT')

    if len(sql_res) == 0:
        return {
            'status': False,
            'errmsg': "该用户没有还未判断的题目。"
        }
    for i in range(len(sql_res)):
        temp_sql_res = sql_res[i]
        path = os.path.join('./subs/user', str(temp_sql_res['stu_id']), str(temp_sql_res['ques_id']))
        jud_time = 0
        while True:
            path_status = os.path.exists(path)
            if not path_status:  # 如果该目录还未创建延时2s
                jud_time += 1
                time.sleep(2)
                if jud_time >= 10:
                    return {
                        'status': False,
                        'errmsg': '数据库中没有该学生的做题记录，请重新提交该题目。'
                    }
            break
    memory_limit = eval(sql_res[0]['memory_limit'][:-2])
    time_limit = eval(sql_res[0]['time_limit'][:-2])
    if language == 'gcc':
        language = 'g++'
    Jud = judger.MainJudge(language, TimeLim=time_limit, MemLim=memory_limit, solution_id=que_id, user_id=stu_id)
    res = Jud.run()
    print(res)
    return {
        'status': True,
        'judgeResult': res
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
