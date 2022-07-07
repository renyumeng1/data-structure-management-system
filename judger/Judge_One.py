from language import Language
from unittest import result
import logging
import config
import lorun
import os

class judge_one:
    def __init__(self,solution_id,time_lim,mem_lim,lan) -> None:
        self.Path_in=os.path.join(config.TestCase_DIR,str(solution_id))#输入文件路径
        self.Path_out=os.path.join(config.TestCase_DIR,str(solution_id))#提交代码的输出文件路径
        self.tlim=time_lim#时间限制
        self.mlim=mem_lim#内存限制
        self.lan=lan#选择的语言

    def judge_result(self,test_case_id)->str:
        user_out_path=os.path.join(self.Path_out,str(test_case_id)+".txt")
        ans_path=os.path.join(self.Path_in,str(test_case_id)+".out")
        out=open(user_out_path)
        ans=open(ans_path)
        user_out=out.read().replace("\r","").rstrip()
        correct=ans.read().replace("\r","").rstrip()
        if user_out==correct:
            os.remove(user_out_path)
            return "ACCEPT"
        if user_out.split()==correct.split():
            os.remove(user_out_path)
            return "Presentation Error"
        else:
            os.remove(user_out_path)
            return "Wrong Anser"


    def run(self,test_case_id)->tuple:
        input_path=open(os.path.join(self.Path_in,str(test_case_id)+".in"))
        output_path=open(os.path.join(self.Path_out,str(test_case_id)+".txt"),"w")
        args=Language[self.lan]
        main_exe = args
        if self.lan not in ["g++","gcc"]:main_exe = args.split()
        runcfg = {
            'args': main_exe,
            'fd_in': input_path.fileno(),
            'fd_out': output_path.fileno(),
            'timelimit': self.tlim,  # in MS
            'memorylimit': self.mlim,  # in KB
        }
        result=lorun.run(runcfg)
        input_path.close()
        output_path.close()
        logging.debug(result)
        Info={
            "time":result["timeused"],
            "mem":result["memoryused"],
            }
        #result指的是运行情况，如果不等于0的话就是三种情况：
        #'Runtime Error','Time Limit Exceeded','Memory Limit Exceeded'
        if result["result"]==0:
            return Info,self.judge_result(test_case_id)
        else:
            return Info,result["result"]

   # output_path="out.txt"