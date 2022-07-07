# dataStructureManagementSystem
[toc]

## 1	学生信息

> GET  /api/student/get/info/
### 接口说明
> 返回学生部分信息
### 响应体
● 200: OK 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| id|number||false|id|
| stu_name|string||true|学生姓名|
| stu_id|string||true|学生学号|
| teacher_name|string||true|管理该学生的教师姓名|
| class|string||true|班级|


## 2	题目信息

> GET  /api/question/get/all/info/
### 接口说明
> 返回所有题目的信息
### 响应体
● 200: OK 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| id|number||false|id|
| ques_name|string||true|题目名称|
| ques_category|string||true|题目类别|
| ques_detail|string||true|题目描述|
| total_finish|number|0|true|完成人数|


## 3	增添学生信息（单个）

> POST  /api/student/add/info/
### 接口说明
> 上传学生信息
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| stu_name|object||true|学生姓名|
| stu_id|string||true|学生学号（账号）|
| stu_pwd|string||true|学生账号的密码|
| stu_gender|int32||true|学生性别(0:男,1:女)|
| stu_img|string|null|true|学生头像|
| teacher|string||true|所属教师的id|
| Class|string||true|所属班级id|
### 响应体
● 200: OK 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| status|boolean|True|true|表示添加成功|
| status|object||true|{status:false,errmsg:对应的错误信息}|
|⇥ status|boolean|false|true|表单验证失败|
|⇥ errmsg|string||true|对应的错误信息|
| status|string||true|数据库已存在该数据，不能添加|

