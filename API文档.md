# dataStructureManagementSystem
[toc]
## 1	环境变量

### 开发环境
| 参数名 | 字段值 |
| ------ | ------ |
|baseUrl|http://101.34.38.102:8000|


## 2	题目相关API

## 2.1	展示题目信息

> GET  /api/question/get/all/info/
### 接口说明
> 展示题目的所有信息
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| pagination|string|true|false|true|为可选项 不传入参数则关闭分页模式|
| page|string|1|true|开启分页模式为必传参数|
| count|string|4|true|同上|
### 响应体
● 200: OK 响应数据格式：
```json
{
  "status": true,
  "page": 1,
  "data": [
    {
      "id": 1,
      "ques_name": "你需要计算3+334234",
      "ques_category": "栈",
      "ques_detail": "这时候一道很简单的题，只需要计算3+3",
      "total_finish": 0
    },
    {
      "id": 3,
      "ques_name": "1+2",
      "ques_category": "图论",
      "ques_detail": "xxx",
      "total_finish": 0
    },
    {
      "id": 4,
      "ques_name": "1+3",
      "ques_category": "图论",
      "ques_detail": "xxx",
      "total_finish": 0
    },
    {
      "id": 5,
      "ques_name": "1+4",
      "ques_category": "图论",
      "ques_detail": "xxx",
      "total_finish": 0
    }
  ]
}
```


## 2.2	增添题目信息

> POST  /api/question/add/all/info/
### 接口说明
> 增添一道题目
### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|Content-Type|multipart/form-data||
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| ques_name|string|逆转字符串|true|添加的题目名称|
| ques_detail|string|你需要将输入的字符串逆转|true|添加的题目信息|
| category_id|string|1|true|题目的类别id|
| memory_limit|string|102400KB|true|内存限制|
| time_limit|string|1000ms|true|时间限制|
| case_file|file||true|为zip格式的文件 包含1.in 1.out 2.in 2.out （数字为样例个数）|
### 响应体
● 200: OK 响应数据格式：
```json
{
    "status": true,
    "msg": "题目添加成功"
}
```
● 200: OK 响应数据格式：JSON
```json
{
    "status": false,
    "errmsg": {
        "memory_limit": [
            "该字段是必填项。"
        ]
    }
}
```
● 200: OK 响应数据格式：JSON
```json
{
    "status": false,
    "errmsg": "没有上传对应题目的测试样例。"
}
```


## 2.3	修改题目信息

## 2.3.1	修改题目信息（获取需要修改的题目信息部分）

> GET  /api/question/<id>/update/info/
### 接口说明
> 在路径上有个<id>，需要传入需要修改的问题的id，例如/api/question/1/update/info/
### 响应体
● 200: OK 响应数据格式：
```json
{
  "status": true,
  "selectResult": {
    "id": 1,
    "ques_name": "你需要计算3+334234",
    "ques_detail": "这时候一道很简单的题，只需要计算3+3",
    "ques_category": "栈",
    "memory_limit": "102400KB",
    "time_limit": "100000ms"
  }
}
```


## 2.3.2	修改题目信息（修改对应id题目，上传样例部分）

> POST  /api/question/<id>/update/info/
### 接口说明
> 修改对应id题目，上传样例部分 地址方括号内的id填写修改对应题目的id
### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|Content-Type|multipart/form-data; boundary=<calculated when request is sent>|||Content-Length|<calculated when request is sent>|||Host|<calculated when request is sent>|||Accept|*/*|||Accept-Encoding|gzip, deflate, br|||Connection|keep-alive||
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| ques_name|string|你需要计算3+334234|true|题目名字|
| ques_detail|string|这时候一道很简单的题，只需要计算3+3|true|题目具体信息|
| category_id|string|4|true|类别id|
| memory_limit|string|102400KB|true|内存限制|
| time_limit|string|100000ms|true|时间限制|
| case_file|file||true|*.zip|
### 响应体
● 200: OK 响应数据格式：
```json
{
  "status": false,
  "errmsg": "没有上传对应题目的测试样例。"
}
```
● 200: OK 响应数据格式：JSON
```json
{
    "status": true,
    "msg": "题目修改成功"
}
```


## 3	学生相关API

## 3.1	展示学生信息

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
```json
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


## 3.2	增添学生信息（单个）

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


## 4	班级相关API

## 4.1	增添班级信息（单个）

> POST  /api/class/add/info/
### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| class_name|string||true|增添的班级名称|
| teacher|string||true|增添的教师id|
### 响应体
● 200: OK 响应数据格式：
```json
{"status": true}
```
● 200: OK 响应数据格式：JSON
```json
{
    "status":false,
    "errmsg":xxx为必填项
}
```
● 200: OK 响应数据格式：JSON
```json
{
    "status":false,
    "errmsg":"(1062, \"Duplicate entry '班级名||教师id' for key 'class_name'\")"
}
```


## 4.2	展示班级信息

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

