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
from Teachers.views import StudentInfoOperation
from Questions.views import QuestionInfoOperation

urlpatterns = [
    path('api/student/get/info/', StudentInfoOperation.getStuInfo),  # 展示学生信息
    path('api/student/add/info/', StudentInfoOperation.addStuInfo),  # 增添学生信息
    path('api/question/get/all/info/', QuestionInfoOperation.getQuestionAllInfo),  # 展示所有题目信息

]
