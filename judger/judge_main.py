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

from complier import Complier
from language import Language_rm
from judge import Judger
import os
from get_id import solution_id,user_id

#这个到时候应该是前端传下来的，先暂时像这样
language="python3"
# language="gcc"
# language="g++"
# language="java"现在在我的环境下(wsl2 ubuntu18.04.5)还运行不了java
tlim=1000 #ms
memlim=102400 #kb

cp=Complier(solution_id,user_id,language)#获取编译器

msg=cp.run_compile()#编译

if not msg:
    raise("Compiler Error")#编译失败

result=Judger.judge(solution_id,user_id,language,tlim,memlim,"oi")
#取得结果，这里用字典的形式返回，方便转json

os.remove(Language_rm[language])
#删除编译文件

if __name__=="__main__":
    print(result)

