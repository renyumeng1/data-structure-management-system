import os

path = os.path.dirname(__file__)

TestCase_DIR = os.path.join("../judgeServer/subsAndCase", "test_case")

# 测试文件地址

WORK_DIR = os.path.join("../judgeServer/subsAndCase", "subs/user")
print(WORK_DIR)
# 提交文件地址

BANNED_IMPORT=[
    "os",
    "sys",
    "socket",
    "multiprocessing",
    "requests",
    "subprocess",
]

BANNED_FUNC=[
    "eval",
    "exec",
]

if __name__ == "__main__":
    open("../judgeServer/subsAndCase/subs/user/1/1/code/main.py")
    open(WORK_DIR+"/1/1/")
