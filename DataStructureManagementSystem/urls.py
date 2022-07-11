"""DataStructureManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from Teachers.views import StudentInfoOperation, ClassInfoOperation
from Questions.views import QuestionInfoOperation

urlpatterns = [
    path('api/student/get/info/', StudentInfoOperation.getStuInfo),  # 展示学生信息
    path('api/student/add/info/', StudentInfoOperation.addStuInfo),  # 增添学生信息
    path('api/student/edit/int:nid/info/', StudentInfoOperation.editStudentInfo),  # 修改学生信息
    path('api/question/get/all/info/', QuestionInfoOperation.getQuestionAllInfo),  # 展示所有题目信息
    path('api/question/add/all/info', QuestionInfoOperation.addQuestionInfo),  # 增加一道题目
    path('api/class/get/info/', ClassInfoOperation.getClassInfo),  # 展示班级信息
    path('api/class/add/info/', ClassInfoOperation.addClassInfo)  # 增加学生信息

]
