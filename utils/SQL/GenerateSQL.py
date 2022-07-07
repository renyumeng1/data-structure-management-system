# -*- coding: utf-8 -*-
# @Time : 2022/7/7 19:24
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : GenerateSQL.py
# @Project : DataStructureManagementSystem
import pymysql.err

from utils.SQL.runMYSQL import SQLOperation


class GenerateSQL:
    def __int__(self):
        pass

    def __init__(self, table_name, form_data):
        self.table_name = table_name
        self.form_data = form_data

    @property
    def generate_add_statement(self):
        _table_name = ""
        _value = ""
        size = 0
        for i in self.form_data:
            key = i
            dict_value = self.form_data[key]
            change_list = ["Class", "teacher"]
            if key in change_list:
                key += "_id"
            # if key == "Class":
            #     key = "Class_id"
            # if key == "teacher":
            #     key = "teacher_id"
            if type(dict_value) != str:
                dict_value = str(dict_value)
            else:
                dict_value = "'" + dict_value + "'"

            if size == len(self.form_data) - 1:

                _table_name += key
                _value += dict_value
            else:
                size += 1
                _table_name += key
                _value += dict_value
                _table_name += ","
                _value += ","
        sql = f"""
            insert into {self.table_name}({_table_name})
        value ({_value});
            """
        return sql

    def run_sql(self):
        sql = self.generate_add_statement
        try:
            result = SQLOperation().run_sql(sql, operation="ADD")
        except pymysql.err.IntegrityError as e:
            _error = str(e)
            # error = _error[_error.index('"'):-1]
            return _error
        return result


if __name__ == "__main__":
    data = {'stu_id': '434132411', 'stu_img': '/txt/', 'stu_name': 'xpy', 'stu_pwd': '123456',
            'stu_gender': 0,
            'teacher': 1, 'Class': 1}
    print(GenerateSQL("Students_student", data).run_sql())
