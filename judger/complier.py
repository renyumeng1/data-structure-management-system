import os
import ast
import subprocess
import judger.config as config
from Protector import ProtectFroPython

# from language import Language


class Complier:
    def __init__(self, solution_id, user_id, language) -> None:
        self.id = solution_id
        self.lan = language
        self.dir_work = os.path.join(config.WORK_DIR, str(user_id), str(solution_id), "code")

    def run_compile(self) -> bool:
        '''将程序编译成可执行文件'''
        build_cmd = {
            "gcc": "gcc main.c -o main -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE",
            "g++": "g++ main.cpp -O2 -Wall -lm --static -DONLINE_JUDGE -o main",
            "java": "javac Main.java",
            "python2": 'python2 -m py_compile main.py',
            "python3": 'python3 -m py_compile main.py',
        }
        if self.lan=="python3":
            code_read=open(os.path.join(self.dir_work,"main.py"),"r",encoding="UTF-8")
            code=code_read.read()
            protect=ProtectFroPython()
            protect.visit(ast.parse(code))
            if not protect.Is_safe():
                return False
        p = subprocess.Popen(build_cmd[self.lan], shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        out, err = p.communicate()  # 获取编译错误信息

        if p.returncode == 0:  # 返回值为0,编译成功
            Code = {
                "gcc": "main.c",
                "g++": "main.cpp",
                "java": "Main.class",
                "python3": "main.py",
                "python2": "main.py",
            }
            os.remove(os.path.join(self.dir_work,Code[self.lan]))
            # 删除源文件
            return True
        else:
            return False

if __name__ == "__main__":
    cp=Complier(1,1,"python3")
    cp.run_compile()