# -*- coding: utf-8 -*-
# @Time : 2022/7/6 18:43
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : QuestionInfoOperation.py
# @Project : DataStructureManagementSystem
from utils.run_mysql import SQLOperation
from django.http import JsonResponse


def getQuestionAllInfo(request):
    if request.method == "GET":
        sql = """
        select result.id,result.ques_name,qc.ques_category,result.ques_Detail,result.total_students_finish
from (select bank.id, bank.ques_name, qq.ques_Detail, qq.category_id, qq.total_students_finish
      from questions_questionbank bank
               inner join questions_questionbankdesc qq on bank.desc_id = qq.id) result,questions_questioncategory qc
         where result.category_id = qc.id;
        """
        query_dict = SQLOperation().deal_sql_result(sql, "id", "ques_name", "ques_category", "ques_detail",
                                                    "total_finish")
        return JsonResponse(query_dict,safe=False)



