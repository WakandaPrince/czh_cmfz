from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from home.models import *


def first_page(request):
    """
    一级页面接口
    :param request: uid,type,sub_type,GET
    :return:Json
    """
    user_id = request.GET.get("uid")
    # 首页：all，闻：wen，思：si
    type = request.GET.get("type")
    # 上师言教：ssyj，显密法要：xmfy
    sub_type = request.GET.get("sub_type")
    print(user_id, type, sub_type)

    if not user_id:
        return JsonResponse({"status": 401, 'msg': '用户未登录'})

    album = []
    # 专辑
    album_qset = TAlbum.objects.all()
    for album_model in album_qset:
        album.append({
            "thumbnail": "http://127.0.0.1:8000/static/" + str(album_model.thumbnail_url),
            "title": album_model.album_title,  # 标题
            "author": album_model.author,  # 描述
            "type": "0",  # 类型（0：闻）
            "set_count": album_model.chapter_num,  # 集数（只有闻的数据才有）
            "create_date": album_model.publish_time  # 创建时间
        })
    # 文章

    ssyj = []
    xmfy = []
    article_qset = TArticle.objects.all()
    for article_model in article_qset:
        if article_model.article_category == 1:
            ssyj.append({
                "thumbnail": "http://127.0.0.1:8000/static/" + str(article_model.thumbnail_url),
                "title": article_model.title,  # 标题
                "content": article_model.content,
                "article_category": article_model.article_category,
                "type": "1",  # 类型（1：思）
                "create_date": article_model.publish_date  # 创建时间
            })
        else:
            xmfy.append({
                "thumbnail": "http://127.0.0.1:8000/static/" + str(article_model.thumbnail_url),
                "title": article_model.title,  # 标题
                "content": article_model.content,
                "article_category": article_model.article_category,
                "type": "1",  # 类型（1：思）
                "create_date": article_model.publish_date  # 创建时间
            })
    article = ssyj + xmfy
    # 代表访问的事首页
    if type == "all":
        # 查询首页所需的数据并按规定的格式响应回去
        # 轮播图
        slid_pic_qset = TSlidpic.objects.all()
        slid_pic = []
        for pic_model in slid_pic_qset:
            slid_pic.append({
                "thumbnail": "http://127.0.0.1:8000/static/" + str(pic_model.url),
                "desc": pic_model.title,  # 头图描述
                "id": pic_model.id  # 头图id
            })
        return JsonResponse({
            'status': 1,
            'slid_pic': slid_pic,
            'body': album + article,
        })
    elif type == "wen":
        # 代表范文的是专辑 查询专辑的信息响应回去
        return JsonResponse({
            'status': 1,
            'album': album,
        })
    elif type == "si":
        if sub_type == "ssyj":
            # 查询属于上师言教的文章
            return JsonResponse({
                'status': 1,
                'ssyj': ssyj,
            })
        else:
            # 查询属于显密法要的文章
            return JsonResponse({
                'status': 1,
                'xmfy': xmfy,
            })
    return HttpResponse('参数错误')
