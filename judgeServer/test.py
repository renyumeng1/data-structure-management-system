# -*- coding: utf-8 -*-
# @Time : 2022/7/10 1:32
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : test.py
# @Project : DataStructureManagementSystem
from utils.mkDir import MakePythonFileFromDataBase

print(MakePythonFileFromDataBase('./allSQL/test.sql', './subs').makePythonFile('main.py'))
