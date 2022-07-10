select t1.stu_solution, t1.stu_id, t1.ques_id, t2.time_limit, t2.memory_limit
from Questions_studentquestionstatus t1,
     Questions_questionbankdesc t2
where t1.stu_id = 2
  and t1.ques_id = 3
  and t1.status = '0'
  and t2.id = t1.ques_id;



select time_limit, memory_limit
from Questions_questionbankdesc;