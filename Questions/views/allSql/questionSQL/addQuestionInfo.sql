use DataStructureManagementSystemDataBase;

insert into Questions_questionbankdesc(ques_detail, total_students_finish, category_id, memory_limit,
                                       time_limit) value ('你需要计算1+1', 0, 1, '102400KB', '1000ms');
set @id = LAST_INSERT_ID();
insert into Questions_questionbank(ques_name, desc_id) value ('1+1question', @id);

set @id = LAST_INSERT_ID();
select id
from Questions_questionbank
where id = @id;


select *
from Questions_questionbankdesc;

select *
from Questions_questionbank;
select id
from Questions_questionbank where desc_id = 26;
