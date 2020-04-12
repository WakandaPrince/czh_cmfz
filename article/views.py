import json
import os

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
from home.models import *


@xframe_options_sameorigin
@csrf_exempt
def upload_img(request):
    """
    上传文章图片
    :param request:
    :return:
    """
    file = request.FILES.get("imgFile")
    if file:
        # 获取图片所在的服务的全路径
        img_url = request.scheme + "://" + request.get_host() + "/static/article_img/" + str(file)
        ArticleImg.objects.create(img_url=file)
        result = {"error": 0, "url": img_url}
    else:
        result = {"error": 1, "url": "上传失败"}
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_all_img(request):
    """
    获取所有图片的方法
    :param request:
    :return:
    """
    # 找到图片所在的目录  方便进行回显
    pic_dir = request.scheme + "://" + request.get_host() + '/static/'
    pic_list = ArticleImg.objects.all()

    rows = []

    for i in list(pic_list):
        # 获取图片的后缀
        path, pic_suffix = os.path.splitext(i.img_url.url)
        print(path, pic_suffix)
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": i.img_url.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffix,
            "filename": i.img_url.name,
            "datetime": "2018-06-06 00:36:39"
        })

    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_dir,
        "total_count": len(pic_list),
        "file_list": rows

    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def add_article(request):
    """
    添加文章
    :param request:
    :return:
    """
    category = request.GET.get('category')
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 存到数据库中
    try:
        # TArticle.objects.create()
        return JsonResponse({'status': 1, 'msg':f'添加成功！'})
    except BaseException as error:
        return JsonResponse({'status': 0, 'msg':f'添加失败:{error}'})



def get_all_article(request):
    return HttpResponse()
