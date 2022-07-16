use DataStructureManagementSystemDataBase;


select t1.id,
       t1.ques_name,
       t2.ques_detail,
       t2.total_students_finish,
       t2.ques_category,
       t2.memory_limit,
       t2.time_limit
from Questions_questionbank t1,
     (select t1.id, t1.ques_detail, t1.total_students_finish, t2.ques_category, t1.memory_limit, t1.time_limit
      from Questions_questionbankdesc t1,
           Questions_questioncategory t2
      where t1.category_id = t2.id) t2
where t1.desc_id = t2.id
  and t1.id = 1;


select t1.id, t1.ques_detail, t1.total_students_finish, t2.ques_category, t1.memory_limit, t1.time_limit
from Questions_questionbankdesc t1,
     Questions_questioncategory t2
where t1.category_id = t2.id;