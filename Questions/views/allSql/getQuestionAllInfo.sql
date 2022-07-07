select result.id,result.ques_name,qc.ques_category,result.ques_Detail,result.total_students_finish
from (select bank.id, bank.ques_name, qq.ques_detail, qq.category_id, qq.total_students_finish
      from Questions_questionbank bank
               inner join Questions_questionbankdesc qq on bank.desc_id = qq.id) result,Questions_questioncategory qc
         where result.category_id = qc.id;
