import json

from django.core.paginator import Paginator
from django.shortcuts import render,HttpResponse

from django.views.decorators.csrf import csrf_exempt
from home.models import *

def get_all_banner(request):
    """
    获取所有轮播图的相关信息并转换成json响应的前端
    :param request:
    :return:
    """
    rows = request.GET.get('rows')
    page = request.GET.get('page')
    pic_list = TSlidpic.objects.all().order_by('id')
    all_page = Paginator(pic_list, rows)

    # 处理最后删除当页最后一条数据
    if int(page) > all_page.num_pages:
        page = all_page.num_pages

    # 获取第一页对象
    page_obj = Paginator(pic_list, rows).page(page).object_list
    page_data = {
        'page': page,
        'total': all_page.num_pages,
        'records': all_page.count,
        'rows': list(page_obj)
    }

    def myDefault(u):
        if isinstance(u, TSlidpic):
            return {"id": u.id,
                    'title': u.title,
                    'upload_time': u.upload_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'status': '展示' if u.status == 1 else '不展示',
                    'pic': str(u.url)}

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)



@csrf_exempt
def add_banner(request):
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
        result = TSlidpic.objects.create(url=pic,title=title,status=int(status))
        if result:
            return HttpResponse('添加成功！')
    except BaseException as error :
        print(error)
        return HttpResponse('添加失败！')


@csrf_exempt
def edit_banner(request):
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
        pic = TSlidpic.objects.get(id=id)
        pic.title = title
        pic.status = status
        pic.save()
        return HttpResponse('修改成功')

    elif method == 'del':
        id = request.POST.get('id')
        pic = TSlidpic.objects.get(id=id)
        pic.delete()
        return HttpResponse('删除成功')