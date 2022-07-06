# Teachers

| id  int  primary key auto_increasement | teacher_name varchar(6) not null | teacher_id varchar(32) not null unique | teacher_pwd varchar(32) not null |
| :------------------------------------: | :------------------------------: | -------------------------------------- | -------------------------------- |
|                 教师id                 |             教师姓名             | 教师工号（账号）                       | 教师密码                         |

# Classes

| id  int  primary key auto_increasement | class_name  varchar(16) not null unique | teacher_id int foreign key references to Teachers(id) |
| :------------------------------------: | :-------------------------------------: | :---------------------------------------------------: |
|                 班级id                 |                  班级                   |            一个教师所管理的班级（一对多）             |

# Students

| id  int  primary key auto_increasement | stu_id varchar(12) not null unique | stu_img varchar(64) | stu_pwd varchar(32) not null | stu_name varchar(5) not null unique | stu_gender tinyint not null | teacher_id int foreign key references to Teachers(id) | class_id int foreign key references to Classes(id) |
| :------------------------------------: | :--------------------------------: | ------------------- | ---------------------------- | :---------------------------------: | :-------------------------: | :---------------------------------------------------: | :------------------------------------------------: |
|                 学生id                 |          学生学号（账号）          | 学生头像            | 学生密码                     |              学生姓名               |   学生性别（用0，1表示）    |          一个老师所管理的所有学生（一对多）           |            一个班级的所有学生（一对多）            |

# QuestionCategory

| id  int  primary key auto_increasement | ques_category varchar(10) not null unique |      |      |      |
| -------------------------------------- | ----------------------------------------- | ---- | ---- | ---- |
| 题目类型 id                            | 题目类型                                  |      |      |      |

# QuestionBank（显示页）

| id  int  primary key auto_increasement | ques_name varchar(20) not null | desc_id int foreign key references to QuestionBankDesc(id) |      |      |
| :------------------------------------: | :----------------------------: | ---------------------------------------------------------- | ---- | ---- |
|                 题目id                 |            题目名称            | 对应的详情页（一对一）                                     |      |      |

# QuestionBankDesc（详情页）

| id  int  primary key auto_increasement | ques_detail varchar(1024) not null | category_id int foreign key references to QuestionCategory(id) | total int default 0 | ques_sample varchar(1024) not null unique | ques_answer varchar(1024) not null unique |
| -------------------------------------- | ---------------------------------- | ------------------------------------------------------------ | ------------------- | ----------------------------------------- | ----------------------------------------- |
| 详情id                                 | 题目详细描述                       | 题目的类型                                                   | 该题目学生完成情况  | 测试用例（地址）                          | 样例对应的答案(地址)                      |

```mysql
total
select t1.desc_id,count(t2.stu_id) 
from CategoryDesc as t1,
	StudentQuestion as t2
where t1.desc_id = t2.ques_id
group by t1.desc_id
```

# CategoryDesc（题目类型，和题目多对多）

| id  int  primary key auto_increasement | desc_id int foreign key references to QuestionBank(id) | category_id int foreign key references to QuestionCategory(id) |      |      |
| -------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------ | ---- | ---- |
| 中间表id                               | 对应的题目id                                           | 对应的题目类型id                                             |      |      |

# StudentQuestion(学生完成题目情况 （学生和题目多对多）)

| id  int  primary key auto_increasement | stu_id int foreign key references to Students(id) | ques_id int foreign key references to QuestionBank(id) | status tinyint （0/1/2）                            | solution not null varchar(1024) |
| -------------------------------------- | ------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------- | ------------------------------- |
| 中间表id                               | 对应的学生id                                      | 对应的题目id                                           | 0：未提交 1：已提交但结果不争取 2：已提交且结果正确 | 学生提交的答案                  |

# TeacherPublish(老师发布的题目)

| id  int  primary key auto_increasement | teacher_id foreign key references to Teachers(id) | class_id foreign key references to Classes(id) | ques_id int foreign key references to QuestionBank(id) |
| -------------------------------------- | ------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------ |
| 中间表id                               | 发布该题目的老师                                  | 对应班级id                                     | 对应题目id                                             |
|                                        |                                                   |                                                |                                                        |
|                                        |                                                   |                                                |                                                        |

