"""为应用程序users定义URL模式"""
from django.contrib.auth.views import LoginView
from django.urls import path,re_path,include
from . import views


LoginView.template_name = 'users/login.html'
urlpatterns = [
#登陆
path(r'login/', LoginView.as_view(), {'template_name': 'users/login.html'},name='login'),
#注销
path(r'^logout/', views.logout_view, name='logout'),
# 注册页面
path(r'^register/', views.register, name='register'),

]


app_name = 'users'
