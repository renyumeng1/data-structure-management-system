# dataStructureManagementSystem
[toc]

## 1	学生信息

> GET  /api/student/get/info/
### 接口说明
> 返回所有题目的信息
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|pagination|False|开启分页模式，返回的数据会根据页码和每页条数分好页如果开启了分页page和count为必传项|
|page|1|页码|
|count|__all__|每页的条数|
### 响应体
● 200: OK 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| status|boolean|true||true|请求成功|请求失败|
| page|number|1|true|返回的当页页码|
| data|array[object]||true|返回的所有数据为一个数组|
|⇥ id|number||true|id|
|⇥ stu_name|string||true|学生姓名|
|⇥ stu_id|string||true|学生id|
|⇥ teacher_name|string||true|所属老师姓名|
|⇥ class|string||true|所属班级名称|
请求示例(注意：传入的为params参数)：
```
axios
.get('/api/student/get/info/?pagination=true&page=1&count=5')
.then(response => {console.log(respnse.data)})
```
返回：
```
{
    "status": true,
    "page": 1,
    "data": [
        {
            "id": 1,
            "stu_name": "小志刚",
            "stu_id": "5120206377",
            "teacher_name": "张三",
            "class": "大数据2001"
        },
        {
            "id": 2,
            "stu_name": "小娃给",
            "stu_id": "5120206378",
            "teacher_name": "张三",
            "class": "大数据2001"
        },
        {
            "id": 3,
            "stu_name": "张啊",
            "stu_id": "5120206379",
            "teacher_name": "张三",
            "class": "大数据2001"
        },
        {
            "id": 4,
            "stu_name": "汤森",
            "stu_id": "5120206380",
            "teacher_name": "张三",
            "class": "大数据2001"
        },
        {
            "id": 5,
            "stu_name": "李白",
            "stu_id": "5120206381",
            "teacher_name": "张三",
            "class": "大数据2002"
        }
    ]
}
```


## 2	题目信息

> GET  /api/question/get/all/info/
### 接口说明
> 返回所有题目的信息
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|pagination|false|开启分页模式，返回的数据会根据页码，和每页条数分好页，如果开启了分页，page和count为必传项|
|page|1|页码|
|count|__all__|每页的条数|
### 响应体
● 200: OK 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| id|number||false|id|
| ques_name|string||true|题目名称|
| ques_category|string||true|题目类别|
| ques_detail|string||true|题目描述|
| total_finish|number|0|true|完成人数|


## 3	班级信息

> GET  /api/question/get/all/info/
### 接口说明
> 返回所有题目的信息
### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|pagination|false|开启分页模式，返回的数据会根据页码，和每页条数分好页，如果开启了分页，page和count为必传项|
|page|1|页码|
|count|__all__|每页的条数|
### 响应体
● 200: OK 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| status|boolean|true|false|true|查询成功|查询失败|
| page|number|1|true|当前页码|
| data|array[object]||true|查询的数据|
|⇥ id|number||true|id|
|⇥ class_name|string||true|班级名称|
|⇥ teacher_name|string||true|学生姓名|


## 4	增添学生信息（单个）

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
| status|boolean|True|true|添加成功|
| status|object||true|{status:false,errmsg:对应的错误信息}|
|⇥ status|boolean|false|true|表单验证失败|
|⇥ errmsg|string||true|对应的错误信息|
| status|string||true|数据库已存在该数据，不能添加|

