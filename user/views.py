import json, MySQLdb, time
from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from home.models import *


def get_all_user(request):
    """
    获取所有注册用户的相关信息并转换成json响应的前端
    :param request:
    :return:
    """
    rows = request.GET.get('rows')
    page = request.GET.get('page')
    user_list = TUser.objects.all().order_by('user_id')
    all_page = Paginator(user_list, rows)

    # 处理最后删除当页最后一条数据
    if int(page) > all_page.num_pages:
        page = all_page.num_pages

    # 获取第一页对象
    page_obj = Paginator(user_list, rows).page(page).object_list
    page_data = {
        'page': page,
        'total': all_page.num_pages,
        'records': all_page.count,
        'rows': list(page_obj)
    }

    def myDefault(u):
        if isinstance(u, TUser):
            return {"id": u.user_id,
                    'username': u.username,
                    'nickname': u.nickname,
                    'address': u.address,
                    'status': '不禁用' if u.status == 1 else '禁用',
                    'register_time': u.register_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'thumbnail': str(u.thumbnail_url)}

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)


@csrf_exempt
def add_user(request):
    """
    用户数据表添加一行数据
    :param request: 需要添加的数据
    :return:
    """
    username = request.POST.get("username")
    nickname = request.POST.get('nickname')
    address = request.POST.get('address')
    status = request.POST.get('status')
    gender = request.POST.get('gender')
    thumbnail = request.FILES.get('thumbnail')
    print(status, username, nickname, address, gender, thumbnail)
    try:
        result = TUser.objects.create(username=username,
                                      password=123456,
                                      thumbnail_url=thumbnail,
                                      nickname=nickname,
                                      gender=gender,
                                      address=address,
                                      status=int(status))
        if result:
            return HttpResponse('添加成功！')
    except BaseException as error:
        print(error)
        return HttpResponse('添加失败！')


@csrf_exempt
def edit_user(request):
    """
    修改、删除用户数据表中的数据
    :param request: 当行数据、修改或者删除
    :return:
    """

    method = request.POST.get("oper")
    print(method)
    if method == 'edit':
        id = request.POST.get('id')
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        address = request.POST.get('address')
        status = request.POST.get('status')
        print(id, username, nickname, address, status)
        user = TUser.objects.get(user_id=id)
        user.username = username
        user.nickname = nickname
        user.address = address
        user.status = status
        user.save()
        return HttpResponse('修改成功')

    elif method == 'del':
        id = request.POST.get('id')
        user = TUser.objects.get(user_id=id)
        user.delete()
        return HttpResponse('删除成功')



def get_added_num(request):
    """
    数据库中获取一周内新注册用户数量
    :param request:
    :return: 返回echart数据
    """
    x = ['2020-04-02',
         '2020-04-03',
         '2020-04-04',
         '2020-04-05',
         '2020-04-06',
         '2020-04-07',
         '2020-04-08']
    y = [0, 0, 0, 0, 0, 0, 0]
    users = TUser.objects.filter(register_time__range=('2020-04-02', '2020-04-09'))
    for user in users:
        date = user.register_time.strftime("%Y-%m-%d")
        for i in x:
            if i == date:
                y[x.index(i)] += 1
    data = {
        'x': x,
        'y': y,
    }
    return JsonResponse(data)


def get_map_data(request):
    """
    数据库中更具地区筛选各个省的人数
    :param request: 
    :return: 
    """

    data = []
    user_list = TUser.objects.all()
    for i in user_list:
        for j in range(len(data)):
            if data[j]['name'] == i.address:
                data[j]['value'] += 1
                break
        else:
            data.append({'name': i.address, 'value': 1})
    # print(data)
    return JsonResponse(data, safe=False)
