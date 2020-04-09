import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from home.models import *


def get_all_user(request):
    """
    获取所有轮播图的相关信息并转换成json响应的前端
    :param request:
    :return:
    """
    rows = request.GET.get('rows')
    page = request.GET.get('page')
    user_list = TUser.objects.all().order_by('id')
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
            return {"id": u.id,
                    'title': u.title,
                    'upload_time': u.upload_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'status': '展示' if u.status == 1 else '不展示',
                    'pic': str(u.url)}

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)



@csrf_exempt
def add_user(request):
    """
    轮播图表添加一行数据
    :param request: 需要添加的数据
    :return:
    """
    title = request.POST.get("title")
    status = request.POST.get('status')
    pic = request.FILES.get('pic')
    print(status, title, pic)
    try:
        result = TUser.objects.create(url=pic,title=title,status=int(status))
        if result:
            return HttpResponse('添加成功！')
    except BaseException as error :
        print(error)
        return HttpResponse('添加失败！')


@csrf_exempt
def edit_user(request):
    """
    修改、删除轮播图表中的数据
    :param request: 当行数据、修改或者删除
    :return:
    """

    method = request.POST.get("oper")
    print(method)
    if method == 'edit':
        id = request.POST.get('id')
        title = request.POST.get('title')
        status = request.POST.get('status')
        print(id,title,status)
        user = TSlidpic.objects.get(id=id)
        user.title = title
        user.status = status
        user.save()
        return HttpResponse('修改成功')

    elif method == 'del':
        id = request.POST.get('id')
        user = TUser.objects.get(id=id)
        user.delete()
        return HttpResponse('删除成功')