"还没有做防护措施,千万别试着运行什么危险代码QAQ"

'''
Sandbox:Lorun
https://github.com/dojiong/Lo-runner
'''

'''
complier --version:

python3:3.10
python2:None
gcc:gcc version 7.5.0
java:{openjdk version "11.0.15" 2022-04-19
        OpenJDK Runtime Environment (build 11.0.15+10-Ubuntu-0ubuntu0.18.04.1)
        OpenJDK 64-Bit Server VM (build 11.0.15+10-Ubuntu-0ubuntu0.18.04.1, mixed mode, sharing)
    }#不太懂这个版本,都放上来了

support language:
[python3,c,c++,java]
'''

from operator import imod
from complier import Complier
import language
from language import Language_rm
from judge import Judger
import os


class MainJudge:
    def __init__(self, language, TimeLim, MemLim,solution_id, user_id,mode="acm"
) -> None:
        self.language = language
        self.TimeLim = TimeLim
        self.MemLim = MemLim
        self.solution_id,self.user_id=solution_id, user_id
        self.mode=mode
    def get_id(self) ->list:
        return [self.user_id,self.solution_id]

    def run(self) -> dict:
        cp = Complier(self.solution_id, self.user_id, self.language)  # 获取编译器

        msg = cp.run_compile()  # 编译

        if not msg:
            return {
                        "solution_id":self.solution_id,
                        "test_id":"#",
                        "user_id":self.user_id,
                        "your_time_used":"#"+"ms",
                        "your_mem_used":"#"+"KB",
                        "ans":"Complier Error",
                    }  # 编译失败
        result = Judger.judge(self.solution_id, self.user_id, language, self.TimeLim, self.MemLim,self.mode)
        # 取得结果，这里用字典的形式返回，方便转json
        os.remove(Language_rm[language].format(user_id=self.user_id,solution_id=self.solution_id))
        # 删除编译文件
        return result


if __name__ == "__main__":
    # 这个到时候应该是前端传下来的，先暂时像这样
    language = "python3"
    # language="gcc"
    # language="g++"
    # language="java"现在在我的环境下(wsl2 ubuntu18.04.5)还运行不了java
    Jud = MainJudge(language,1000,102400,1001,5120201234)
    print(Jud.run())