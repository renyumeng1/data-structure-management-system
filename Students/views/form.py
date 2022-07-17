# -*- coding: utf-8 -*-
# @Time : 2022/7/17 21:03
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : form.py
# @Project : DataStructureManagementSystem
from django import forms


class EditStuInfoForm(forms.Form):
    stu_name = forms.CharField(max_length=16)
    stu_img = forms.CharField(max_length=1024)
    stu_gender = forms.IntegerField()
