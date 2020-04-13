import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from home.models import *
from django.views.decorators.csrf import csrf_exempt


def getAllAlbum(request):
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = TAlbum.objects.all().order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, TAlbum):
            return {
                "author": u.author,
                "brief": u.description,
                "broadcast": u.bordcaster,
                "count": u.chapter_num,
                "cover": u.thumbnail_url,
                "createDate": u.publish_time.strftime('%Y-%m-%d %H:%M:%S'),
                "id": u.id,
                "publishDate": u.publish_time.strftime('%Y-%m-%d %H:%M:%S'),
                "score": u.rating,
                "status": u.status,
                "title": u.album_title,
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)


@csrf_exempt
def editAlbum(request):
    method = request.POST.get('oper')
    print(method)
    author = request.POST.get("author")
    brief = request.POST.get("brief")
    broadcast = request.POST.get("broadcast")
    count = request.POST.get("count")
    cover = request.FILES.get("cover")
    create_date = request.POST.get("createDate")
    id = request.POST.get("id")
    publish_date = request.POST.get("publishDate")
    score = request.POST.get("score")
    status = request.POST.get("status")
    title = request.POST.get("title")
    print(f'id: {id} 作者：{author}简介：{brief}播音员:{broadcast}章节数量:{count} 封面：{cover} 创建日期{create_date} 发布日期{publish_date}'
          f'评分:{score} 状态：{status} 标题：{title}')
    if method == 'add':
        try:
            TAlbum.objects.create(album_title=title, author=author, bordcaster=broadcast, chapter_num=count,
                                  description=brief, rating=score, status=status)
            return JsonResponse({'status': 1, 'msg': f'添加成功！'})
        except BaseException as error:
            return JsonResponse({'status': 0, 'msg': f'添加失败！{error}'})
    elif method == 'edit':
        try:
            album = TAlbum.objects.get(id=id)
            album.album_title = title
            album.rating = score
            album.bordcaster = broadcast
            album.description = brief
            album.status = status
            album.save()
            return JsonResponse({'status': 1, 'msg': f'修改成功！'})
        except BaseException as error:
            return JsonResponse({'status': 0, 'msg': f'添加失败！{error}'})
    elif method == 'del':
        try:
            album = TAlbum.objects.get(id=id)
            album.delete()
            return JsonResponse({'status': 1, 'msg': f'删除成功！'})
        except BaseException as error:
            return JsonResponse({'status': 0, 'msg': f'添加失败！{error}'})
    return HttpResponse()


def getChapterByAlbumId(request):
    album_Id = request.GET.get('albumId')
    page_num = request.GET.get('page')
    row_num = request.GET.get('rows')

    rows = []
    album = TAudioChapter.objects.all().filter(album_id=album_Id).order_by('id')
    all_page = Paginator(album, row_num)
    page = Paginator(album, row_num).page(page_num)

    for i in page:
        rows.append(i)

    page_data = {
        "total": all_page.num_pages,
        "records": all_page.count,
        "page": page_num,
        "rows": rows
    }

    def myDefault(u):
        if isinstance(u, TAudioChapter):
            return {
                "albumId": u.album_id,
                "createDate": u.publish_time.strftime('%Y-%m-%d %H:%M:%S'),
                "duration": u.audio_duration,
                "id": u.id,
                "size": u.audio_size,
                "title": u.chapter_name,
                "url": u.audio_url,
            }

    data = json.dumps(page_data, default=myDefault)

    return HttpResponse(data)
