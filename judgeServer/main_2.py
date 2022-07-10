import os
import judger
import time
import datetime
from collections import deque
from utils.mkDir import MakePythonFileFromDataBase
from utils.SQL.runMYSQL import SQLOperation


class JudSer:
    @staticmethod
    def server():
        sql_2='''
        UPDATE Questions_studentquestionstatus 
        SET status='{res}'
        WHERE id= {id};
        '''
        sql_path='./allSQL/test.sql'
        Jud = judger.MainJudge
        maker=MakePythonFileFromDataBase(sql_path, './subs')
        while True:
            now=time.strftime("%Y%m%d_%H_%M_%S",time.localtime(time.time()))
            ERROR_MSG_DIR="../judgeServer/error_log/"+now+".txt"
            time.sleep(0.5)
            sql = SQLOperation().load_sql(sql_path)
            res = SQLOperation().run_sql(sql, 'SELECT')
            if res==False or len(res) == 0:
                time.sleep(0.2)
                continue
            q=deque()
            for msg in res:
                id,ques_id,stu_id,code,language,status=msg
                status=maker.makePythonFile_withoutsql(msg[1:])
                if not status["status"]:
                    print(ERROR_MSG_DIR)
                    e=os.open(ERROR_MSG_DIR,os.O_RDWR|os.O_CREAT)
                    os.write(e,status["errmsg"].encode())
                    os.close(e)
                    return False#返回服务器错误信息
                q.append((id,ques_id,stu_id,code,language))
            while len(q):
                id,ques_id,stu_id,code,language=q.popleft()
                res=Jud(language, TimeLim=1000, MemLim=102400, \
                    solution_id=ques_id, user_id=stu_id, mode="oi").run()
                sts=''
                if all([i["ans"]=="ACCEPT" for _,i in res.items()]):
                    sts=="1"#算正确吧？
                else:sts=="2"#算错误吧？
                sql_2=sql_2.format(res=1,id=id)
                sts = SQLOperation().run_sql(sql_2,'UPDATE')
                #修改提交状态


                "此处返回服务器判题其他结果"
if __name__=="__main__":
    ser=JudSer
    ser.server()