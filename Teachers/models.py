from django.db import models


# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=6, null=False)
    teacher_id = models.CharField(max_length=32, unique=True, null=False)
    teacher_pwd = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.teacher_name


class Classes(models.Model):
    class_name = models.CharField(max_length=32, null=False, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


