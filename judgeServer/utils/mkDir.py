# -*- coding: utf-8 -*-
# @Time : 2022/7/9 23:21
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : mkDir.py
# @Project : DataStructureManagementSystem
import os
from utils.SQL.runMYSQL import SQLOperation


class MakePythonFileFromDataBase:
    def __init__(self, sql_path, subs_path):
        self.sql_path = sql_path
        self.subs_path = subs_path

    @staticmethod
    def mkdir(path):
        """
        创建指定的文件夹
        :param path: 文件夹路径，字符串格式
        :return: path || False
        """
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        is_exists = os.path.exists(path)
        # 判断结果
        if not is_exists:
            os.makedirs(path)
            return path
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return 'false'

    @staticmethod
    def MakeFile(file_name, path, python):
        cre_path = MakePythonFileFromDataBase.mkdir(path)
        if cre_path == 'false':
            return f'{path}目录已经存在'
        temp_path = os.path.join(cre_path, file_name)
        file = open(temp_path, 'w')
        file.write(python)
        file.close()
        return True

    def makePythonFile(self, python_filename='main.py'):
        sql = SQLOperation().load_sql(self.sql_path)
        res = SQLOperation().run_sql(sql, 'SELECT')
        status = {
            'status': False,
        }
        if len(res) == 0:
            status['errmsg'] = '没有学生提交代码'
            return status
        for i in range(len(res)):
            temp_path = os.path.join(self.subs_path, 'user', f'{res[i][1]}/{res[i][0]}/code')
            temp_status = MakePythonFileFromDataBase.MakeFile(python_filename, temp_path, res[i][2])
            if temp_status != True:
                status['errmsg'] = temp_status
                return status
        status['status'] = True
        return status


if __name__ == "__main__":
    print(os.path.join('../subs/user', '1/1/code'))
    if not '1234':
        print(1)
