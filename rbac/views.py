from django.shortcuts import render, HttpResponse, redirect

from rbac.models import *
from rbac.service.init_permission import init_permission


def login(request):
    return render(request, 'login_form.html')


def check_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    user = UserInfo.objects.get(name=username, password=password)
    print(user)
    if not user:
        return render(request, "login_form.html", {'msg': "用户名或密码错误"})

        # 处理权限相关的业务
    init_permission(user, request)

    return redirect("home_index")

