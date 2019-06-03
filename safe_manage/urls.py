from django.urls import path,re_path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    #主页
    path('', views.index, name='index'),
    #显示所有检查
    path('examinations/', views.examinations, name='examinations'),
    #显示某次检查中发现的所有问题
    path('problems/(?P<examination_id>\d+)/', views.problems, name='problems'),
    #查看整改措施
    path('rectification/(?P<problem_id>\d+)/',views.rectification,name='rectification'),
    #新增检查
    path('new_examination/',views.new_examination,name='new_examination'),
    #新增问题
    path('new_problem/(?P<examination_id>\d+)/',views.new_problem,name='new_problem'),
    #修改检查
    path('edit_examination/(?P<examination_id>\d+)/',views.edit_examination,name='edit_examination'),
    #修改问题
    path('edit_problem/(?P<problem_id>\d+)/',views.edit_problem,name='edit_problem'),
    #新增整改措施
    path('new_rectification/(?P<problem_id>\d+)/',views.new_rectification,name='new_rectification'),
    #修改整改措施
    path('edit_rectification/(?P<rectification_id>\d+)/',views.edit_rectification,name='edit_rectification'),
    #对问题进行合格评价
    path('new_comment_pass/(?P<problem_id>\d+)/',views.new_comment_pass,name='new_comment_pass'),
    #对整改措施进行添加评价
    path('new_comment/(?P<rectification_id>\d+)/',views.new_comment,name='new_comment'),
    #上传图片
    path('upload/(?P<problem_id>\d+)/',views.upload,name='upload'),
    #删除图片
    path('/deleteimg/(?P<img_id>\d+)/',views.deleteimg,name= 'deleteimg'),
    
    
]
