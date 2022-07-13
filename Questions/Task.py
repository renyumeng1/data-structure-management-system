# -*- coding: utf-8 -*-
# @Time : 2022/7/13 14:11
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : Task.py
# @Project : DataStructureManagementSystem
import requests


def mkResDirTask():
    url = "http://101.34.38.102:4000/api/create/ans/path"
    res = requests.get(url=url)
    return res.json()


if __name__ == "__main__":
    print(mkResDirTask())
