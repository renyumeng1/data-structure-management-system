# -*- coding: utf-8 -*-
# @Time : 2022/7/9 23:21
# @Author : renyumeng
# @Email : 2035328756@qq.com
# @File : mkDir.py
# @Project : DataStructureManagementSystem
import os


class MakePythonFile:
    def __init__(self):
        pass

    @staticmethod
    def mkdir(path):
        """
        创建指定的文件夹
        :param path: 文件夹路径，字符串格式
        :return: True(新建成功) or False(文件夹已存在，新建失败)
        """

        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        print(path)

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        is_exists = os.path.exists(path)

        # 判断结果
        if not is_exists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            print(path + ' 创建成功')
            return path
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path + ' 目录已存在')
            return False

    @staticmethod
    def MakeFile(file_name, path, python):
        cre_path = MakePythonFile.mkdir(path)
        if not cre_path:
            return '目录已经存在'
        temp_path = os.path.join(cre_path,file_name)
        print(temp_path)
        file = open(temp_path, 'w')
        file.write(python)
        file.close()
        return True


if __name__ == "__main__":
    MakePythonFile.mkdir('../subs/user/3/5')
