# -*- coding: utf-8 -*-
# @Time : 2022/7/7 19:24
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : GenerateSQL.py
# @Project : DataStructureManagementSystem
import pymysql.err
from utils.SQL.runMYSQL import SQLOperation


class GenerateSQL:
    """
    该类封装了ADD操作的SQL，和需要开启分页功能的SQL
    """

    def __int__(self):
        pass

    def __init__(self, table_name=None, form_data=None, pagination=None, operation='INSERT', select_sql=None):
        """
        :param table_name: 需要增添数据的字段名
        :param form_data: 前端发送的表单数据
        :param pagination: 当为SELECT时是否开启分页 {paginator:True|False,page:页码,count:每页的数据条数}
        :param operation: SQL操作
        :param select_sql: 当SQL操作为SELECT时需传入的SQL语句
        """
        if pagination is None:
            pagination = {'paginator': False, 'page': 1, 'count': '__all__'}
        self.table_name = table_name
        self.form_data = form_data
        self.pagination = pagination
        self.operation = operation
        self.select_sql = select_sql

    @property
    def generate_statement(self):
        """
        :return: 增添加数据的sql语句
        """
        if self.operation == 'INSERT':
            _table_name = ""
            _value = ""
            size = 0
            for i in self.form_data:
                key = i
                dict_value = self.form_data[key]
                change_list = ["Class", "teacher"]
                if key in change_list:
                    key += "_id"
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
        elif (self.operation == "SELECT") and (self.pagination['paginator'] is True):
            page = self.pagination['page']
            count = self.pagination['count']
            start_index = (page - 1) * count
            limit_sql = f" limit {start_index},{count};"
            if self.select_sql[-1] != ";":
                index = self.select_sql.find(';')
                new_sql = self.select_sql[:index] + limit_sql
            else:
                new_sql = self.select_sql[:-1] + limit_sql
            return new_sql

    def run_sql(self, if_get_id=False):
        """
        :returns:result:True || False
        :returns:errorMsg
        """
        sql = self.generate_statement
        try:
            result = SQLOperation().run_sql(sql, operation=self.operation, if_get_id=if_get_id)
        except pymysql.err.IntegrityError as e:
            _error = str(e)
            # error = _error[_error.index('"'):-1]
            return _error
        return result


if __name__ == "__main__":
    # data = {'stu_id': '434132411', 'stu_img': '/txt/', 'stu_name': 'xpy', 'stu_pwd': '123456',
    #         'stu_gender': 0,
    #         'teacher': 1, 'Class': 1}
    # print(GenerateSQL(table_name='Students_student', form_data=data,
    #                   pagination={'paginator': True, 'page': 1, 'count': 10},
    #                   operation="SELECT").generate_add_statement)
    sql = SQLOperation.load_sql("../../Teachers/views/allSql/classSQL/getClassInfo.sql")
    ew_sql = GenerateSQL(pagination={'paginator': True, 'page': 2, 'count': 2}, operation="SELECT",
                         select_sql=sql).generate_statement
    print(SQLOperation().deal_sql_result(ew_sql, "id", "stu_name", "stu_id", "teacher_name", "class_name"))
