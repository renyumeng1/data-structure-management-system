from Judge_One import judge_one
class Judger:
    @staticmethod
    def judge(solution_id,user_id,language,tlim,memlim,mode="acm")->dict:
        sts={
            2:"Time Limit Exceeded",
            3:"Memory Limit Exceeded",
            5:"Runtime Error",
        }
        test_num=2#应该获取
        judger=judge_one(solution_id,user_id,tlim,memlim,language)
        status={}#相当于每一个题目的完成情况
        if mode=="acm":
            #每个点都必须正确才算是写出题来，所以遇到出错的直接停止判题
            #所以如果题目出错的话就直接返回了
            for i in range(test_num):
                Info,res=judger.run(i+1)
                if res in [5,2,3]:
                    status[i+1]=({
                        "solution_id":solution_id,
                        "user_id":user_id,
                        "test_id":i+1,
                        "your_time_used":str(Info["time"])+"ms",
                        "your_mem_used":str(Info["mem"])+"KB",
                        "ans":sts[res],
                    })
                    return status
                else:
                    status[i+1]=({
                        "solution_id":solution_id,
                        "test_id":i+1,
                        "user_id":user_id,
                        "your_time_used":str(Info["time"])+"ms",
                        "your_mem_used":str(Info["mem"])+"KB",
                        "ans":res,
                    })
                if res!="ACCEPT":
                    return status
            return status
        elif mode=="oi":#如果是oi模式的话就每个题都判断一遍，然后返回所有题目的完成情况
            for i in range(test_num):
                Info,res=judger.run(i+1)
                if res in [5,2,3]:
                    status[i+1]=({
                        "solution_id":solution_id,
                        "test_id":i+1,
                        "user_id":user_id,
                        "your_time_used":str(Info["time"])+"ms",
                        "your_mem_used":str(Info["mem"])+"KB",
                        "ans":sts[res],
                    })
                else:
                    status[i+1]=({
                        "solution_id":solution_id,
                        "test_id":i+1,
                        "user_id":user_id,
                        "your_time_used":str(Info["time"])+"ms",
                        "your_mem_used":str(Info["mem"])+"KB",
                        "ans":res,
                    })
            return status
