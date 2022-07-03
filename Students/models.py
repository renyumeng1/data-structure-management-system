from django.db import models
from Teachers.models import Teacher, Classes


class Student(models.Model):
    stu_id = models.CharField(max_length=12, null=False, unique=True)  # 学生学号
    stu_img = models.CharField(max_length=1024, null=True)  # 学生头像
    stu_pwd = models.CharField(max_length=32, null=False)
    stu_name = models.CharField(max_length=10, null=False, unique=True)
    gender_choices = (
        (0, '男'),
        (1, '女')
    )
    stu_gender = models.SmallIntegerField(default=0, choices=gender_choices)  # 性别 0：男 1：女
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)  # 被哪个老师管理
    Class = models.ForeignKey(to=Classes, on_delete=models.CASCADE)  # 所处班级

    def __str__(self):
        return self.stu_name

# Create your models here.
