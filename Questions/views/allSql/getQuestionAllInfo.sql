select result.id,result.ques_name,qc.ques_category,result.ques_Detail,result.total_students_finish
from (select bank.id, bank.ques_name, qq.ques_Detail, qq.category_id, qq.total_students_finish
      from questions_questionbank bank
               inner join questions_questionbankdesc qq on bank.desc_id = qq.id) result,questions_questioncategory qc
         where result.category_id = qc.id;
