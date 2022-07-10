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
import logging
import judger

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
    sql = f"select stu_solution,stu_id,ques_id from Questions_studentquestionstatus where ques_id={que_id} and stu_id={stu_id} and status = '0';"
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
    Jud = judger.MainJudge(language, TimeLim=1000, MemLim=102400, solution_id=que_id, user_id=stu_id)
    res = Jud.run()
    return {
        'status': True,
        'judgeResult': res
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
