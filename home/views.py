from django.shortcuts import render

def main(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')