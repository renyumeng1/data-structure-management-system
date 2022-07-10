import os

path = os.path.dirname(__file__)

TestCase_DIR = os.path.join( "../subsAndCase", "test_case")

# 测试文件地址

WORK_DIR = os.path.join("../subsAndCase", "subs/user")
print(WORK_DIR)
# 提交文件地址

if __name__ == "__main__":
    open("../subsAndCase/subs/user/1/1/code/main.py")
    open(WORK_DIR+"/1/1/")
