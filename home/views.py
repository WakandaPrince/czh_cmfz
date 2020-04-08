from redis import Redis
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from czh_cmfz.settings import *
from utilities.generate_code import random_code
from utilities.send_msg import YunPian

import re


def main(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')

redis = Redis(host="localhost", port=PORT)
@csrf_exempt
def get_code(request):
    """
    发送手机验证码
    :param request: 接受输入的手机号码
    :return: 发送状态
    """
    phone = request.POST.get('mobile')
    # 正则判断输入手机号是否合法
    result = re.match(r"^1[35678]\d{9}$", phone)
    if result:
        saved_code = redis.get(f'{phone}_1')
        if saved_code:
            return JsonResponse({'status': 0, 'msg': '已经发送了验证码请检查！'})
        code = random_code()
        print(f'验证码：{code}')
        yun_pian = YunPian(API_KEY)
        # yun_pian.send_msg(phone,code)

        # 将手机号与对应的验证码存入redis  防止无限制发送

        redis.set(f"{phone}_1", code, 120)
        # 保证验证码的有效期
        redis.set(f"{phone}_2", code, 600)

        return JsonResponse({'status': 1, 'msg': '发送成功！请查收！'})
    else:
        return JsonResponse({'status': 0, 'msg': '请输入合法的手机号！'})


def check_user(request):
    """
    用户登陆信息校验
    :param request:用户手机号验证码
    :return:成功跳转，失败提示信息
    """
    phone = request.GET.get('mobile')
    code = request.GET.get('code')
    phone_result = re.match(r"^1[35678]\d{9}$", phone)
    code_result = re.match(r"\d{4}$", code)
    if phone_result and code_result:
        try:
            saved_code = redis.get(f'{phone}_2')
            if saved_code.decode() == code:
                return JsonResponse({'status': 1, 'msg': '登陆成功！'})
        except BaseException as error:
            print(error)
            return JsonResponse({'status': 0, 'msg': f'{error}请先发送验证码！'})
        return JsonResponse({'status': 0, 'msg': '登陆失败！'})
    else:
        return JsonResponse({'status': 0, 'msg': '有字段输入不合法！请检查！'})

