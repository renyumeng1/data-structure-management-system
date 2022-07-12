# -*- coding: utf-8 -*-
# @Time : 2022/7/10 21:52
# @Author : RuanCat
# @Email : 473670005@qq.com
# @File : mkDir.py
# @Project : DataStructureManagementSystem
import os
from utils.SQL.runMYSQL import SQLOperation
from pymysql.cursors import DictCursor


class MakeCodeFileFromDataBase:
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
            return {
                'status': True,
                'path': path
            }
        return {
            'status': False,
            'path': path
        }

    @staticmethod
    def MakeFile(file_name, path, code):
        cre_path = MakeCodeFileFromDataBase.mkdir(path)
        if not cre_path['status']:  # 如果目录已经存在，则表示用户是修改自己的代码，数据库里的代码进行进行比对，如果不同就覆盖以前的代码，如果相同直接返回
            temp_path = os.path.join(cre_path['path'], file_name)
            file_exist = os.path.exists(temp_path)
            if file_exist:
                with open(temp_path) as file:
                    file_python_code = file.read().replace('\r', '').replace('\t', '').replace(' ', '')
                    new_python_code = code.replace('\r', '').replace('\t', '').replace(' ', '')
                    if new_python_code == file_python_code:
                        return "和源文件的代码一致，不需要修改"
                    file.close()
        temp_path = os.path.join(cre_path['path'], file_name)
        print(temp_path)
        file = open(temp_path, 'w')
        file.write(code)
        file.close()
        return 'true'

    @property
    def makeCodeFile(self):
        sql = SQLOperation().load_sql(self.sql_path)
        res = SQLOperation(cursor_class=DictCursor).run_sql(sql, 'SELECT')
        status = {
            'status': False,
        }
        if len(res) == 0:
            status['errmsg'] = '没有学生提交代码'
            return status
        status_list = []
        for i in range(len(res)):
            status = {}
            temp_path = os.path.join(self.subs_path, 'user', f'{res[i]["stu_id"]}/{res[i]["ques_id"]}/code')
            code = res[i]["stu_solution"]
            code_file_name = {
                'python3': 'main.py',
                'g++': 'main.cpp',
                'java': 'Main.java'
            }
            temp_status = MakeCodeFileFromDataBase.MakeFile(code_file_name[res[i]['language']], temp_path,
                                                            code)  # 创建代码文件
            status['status_id'] = i
            if temp_status != 'true':
                status['errmsg'] = temp_status
            else:
                status['status'] = True
            status_list.append(status)
        return  status_list

    def makePythonFile_withoutsql(self,res,python_filename='main.py'):
        status = {
            'status': False,
        }
        temp_path = os.path.join(self.subs_path, 'user', f'{res[1]}/{res[0]}/code')
        temp_status = MakePythonFileFromDataBase.MakeFile(python_filename, temp_path, res[2])
        if temp_status != True:
            status['errmsg'] = temp_status
            return status
        status['status'] = True
        return status


if __name__ == "__main__":
    status = MakeCodeFileFromDataBase(sql_path='../allSQL/getJudgeInfo.sql', subs_path='../subsAndCase/subs').makeCodeFile
    print(status)
