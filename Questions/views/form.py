# -*- coding: utf-8 -*-
# @Time : 2022/7/8 16:21
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : form.py
# @Project : DataStructureManagementSystem
from django import forms


class AddQuestionInfoForm(forms.Form):
    ques_name = forms.CharField(max_length=20)
    ques_detail = forms.CharField(max_length=1024)
    category_id = forms.IntegerField()
    memory_limit = forms.CharField(max_length=1024)
    time_limit = forms.CharField(max_length=1024)


class SubmitQuestion(forms.Form):
    stu_id = forms.IntegerField()
    language = forms.CharField(max_length=16)
    stu_solution = forms.CharField(max_length=1024)
    status = forms.CharField(max_length=32)
