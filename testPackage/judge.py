# -*- coding: utf-8 -*-
# @Time : 2022/7/5 21:42
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : judge.py
# @Project : DataStructureManagementSystem
import subprocess

res = subprocess.Popen("python3 1.py", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
(out, err) = res.communicate("1\n2")
print(out)
print(err)
if "3.0" in out:
    print("result is true!")
