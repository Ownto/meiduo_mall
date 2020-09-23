from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # 用户注册
    path('register/', views.RegisterView.as_view(), name='register'),  # 用户模块
]
