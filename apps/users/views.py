# -*- coding: utf8 -*-
from django.shortcuts import render
from django.views import View

# Creat your views here.


class RegisterView(View):

    def get(self, request):
        # 提供用户注册的页面
        return render(request, 'register.html')  # 后端渲染页面的函数

    def post(self):
        pass
