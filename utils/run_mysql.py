# -*- coding: utf-8 -*-
# @Time : 2022/7/6 17:39
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : run_mysql.py
# @Project : DataStructureManagementSystem


import logging
import pymysql
import time
from typing import Tuple, Union, Any


class SQLOperation:
    def __init__(self, db_host="localhost", db_user="root", db_password="renyumeng",
                 db_name="datastructuremanagementsystemdatabase"):
        self.host = db_host
        self.user = db_user
        self.pwd = db_password
        self.name = db_name

    def run_sql(self, sql):
        """

        :param sql: 执行的sql语句
        :return: 查询结果
        """

        con = None
        while True:
            try:
                con = pymysql.connect(host=self.host, user=self.user, password=self.pwd,
                                      database=self.name)
                break
            except:
                logging.error('Cannot connect to database,trying again')
                time.sleep(1)
        cur = con.cursor()
        try:
            if type(sql) == str:
                cur.execute(sql)
            elif type(sql) == list:
                for i in sql:
                    cur.execute(i)
        except pymysql.OperationalError as e:
            logging.error(e)
            cur.close()
            con.close()
            return False
        con.commit()
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def deal_sql_result(self, sql: str, *key: str):
        """

        :param sql: 执行的sql语句
        :param key: 查询数据的键值
        :return:
        """
        query_result: Union[bool, Tuple[Tuple[Any, ...], ...]] = self.run_sql(sql)
        result_lst = []
        for i in range(len(query_result)):
            dict_res = {}
            for j in range(len(query_result[i])):
                dict_res[key[j]] = query_result[i][j]
            result_lst.append(dict_res)
        return result_lst

    @staticmethod
    def load_sql(path):
        """

        :param path: sql文件的地址必须是绝对路径
        :return: Sql语句
        """
        sql = ""
        with open(path) as file:
            sql_list = file.readlines()
            for i in range(len(sql_list)):
                sql += sql_list[i]
        file.close()
        return sql


if __name__ == "__main__":
    SQL = """
    select result.stu_name,result.stu_id,result.teacher_name,tc.class_name
from (select t1.stu_name, t1.stu_id, t1.Class_id, t2.teacher_name
      from students_student t1,
           teachers_teacher t2
      where t1.teacher_id = t2.id) result,
     teachers_classes tc
where result.Class_id = tc.id;
    """
    print(SQLOperation("localhost", "root", "renyumeng", "datastructuremanagementsystemdatabase").deal_sql_result(SQL,
                                                                                                                  "学生姓名",
                                                                                                                  "学号",
                                                                                                                  "对应教师",
                                                                                                                  "班级"))
