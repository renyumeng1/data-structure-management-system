# -*- coding: utf-8 -*-
# @Time : 2022/7/9 22:53
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : main.py
# @Project : DataStructureManagementSystem
from utils.mkDir import MakePythonFileFromDataBase
from flask import Flask
import judger

app = Flask(__name__)

if __name__ == "__main__":
    language = 'python3'
    Jud = judger.MainJudge('python3', TimeLim=1000, MemLim=102400, solution_id=1, user_id=1)

    print(Jud.run())
    # app.run()
