use DataStructureManagementSystemDataBase;


select t1.id, t1.ques_name, t2.ques_detail, t2.category_id, t2.memory_limit, t2.time_limit
from Questions_questionbank t1,
     Questions_questionbankdesc t2
where t1.desc_id = t2.id;


select res.id, res.ques_name, res.ques_detail, Qc.ques_category, res.memory_limit, res.time_limit
from Questions_questioncategory Qc,
     (select t1.id, t1.ques_name, t2.ques_detail, t2.category_id, t2.memory_limit, t2.time_limit
      from Questions_questionbank t1,
           Questions_questionbankdesc t2
      where t1.desc_id = t2.id) as res
where res.category_id = Qc.id
  and res.id = 1;


update Questions_questionbank t1,Questions_questionbankdesc t2
set t1.ques_name='你需要计算sadsa',
    t2.ques_detail='dfdfs',
    t2.category_id=5,
    t2.time_limit='10000ms',
    t2.memory_limit='102400KB'
where t1.id = 1
  and t2.id = t1.desc_id;


begin;
update Questions_questionbank t1,Questions_questionbankdesc t2
set t1.ques_name='你需要计算sad213123213sa',
    t2.ques_detail='dfdfs',
    t2.category_id=5,
    t2.time_limit='10000ms',
    t2.memory_limit='102400KB'
where t1.id = 1
  and t2.id = t1.desc_id;
commit;