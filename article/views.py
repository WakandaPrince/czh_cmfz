from django.shortcuts import render, HttpResponse

# Create your views here.
def upload_img(request):
    print(request.FILES)
    return HttpResponse()
