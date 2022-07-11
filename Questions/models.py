from django.db import models
from Students.models import Student
from Teachers.models import Teacher, Classes


class QuestionCategory(models.Model):
    # 题目类别表
    ques_category = models.CharField(max_length=10, null=False, unique=True)  # 题目的类别

    def __str__(self):
        return self.ques_category


# 题目详情
class QuestionBankDesc(models.Model):
    ques_detail = models.CharField(max_length=1024, null=False)
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)  # 题目类别关联QuestionCategory表
    total_students_finish = models.IntegerField(default=0)  # 学生该题目的完成情况
    # ques_case = models.CharField(max_length=255)  # 题目测试样例（地址）
    time_limit = models.CharField(max_length=1024, default='1000ms')  # 题目的时间限制
    memory_limit = models.CharField(max_length=1024, default='102400KB')  # 题目的内存限制


# 题目的显示页
class QuestionBank(models.Model):
    ques_name = models.CharField(max_length=20, null=False)  # 题目名称
    desc = models.OneToOneField(to=QuestionBankDesc, on_delete=models.CASCADE)

    def __str__(self):
        return self.ques_name


# 学生对应题目情况
class StudentQuestionStatus(models.Model):
    stu = models.ForeignKey(Student, on_delete=models.CASCADE)
    ques = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
    status = models.CharField(max_length=64, default=0)
    language = models.CharField(max_length=64, null=False, default='python3')
    stu_solution = models.CharField(max_length=1024, null=False)


# 老师发布题目信息
class TeacherPublishQuestion(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    Class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
