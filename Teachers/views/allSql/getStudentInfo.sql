select result.id,result.stu_name,result.stu_id,result.teacher_name,tc.class_name
from (select t1.id,t1.stu_name, t1.stu_id, t1.Class_id, t2.teacher_name
      from Students_student t1,
           Teachers_teacher t2
      where t1.teacher_id = t2.id) result,
     Teachers_classes tc
where result.Class_id = tc.id;


