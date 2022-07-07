# -*- coding: utf-8 -*-
# @Time : 2022/7/7 13:44
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : From.py
# @Project : DataStructureManagementSystem
from Students.models import Student
from django import forms


class AddStudentInfoForm(forms.Form):
    stu_id = forms.CharField(max_length=12)
    stu_img = forms.CharField(max_length=1024)
    stu_name = forms.CharField(max_length=10)
    stu_pwd = forms.CharField(max_length=32)
    stu_gender = forms.IntegerField()
    teacher = forms.IntegerField()
    Class = forms.IntegerField()
