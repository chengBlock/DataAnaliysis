from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

# 首页
from app01 import models

def index(request):
    return render(request, "index.html")


def register(request):

    if request.method == 'GET':
        username =request.GET.get('username','none')
        pwd = request.GET.get('pwd','123456')
        models.Admin.objects.create(
            username=username,
            pwd=pwd
        )

        return HttpResponse("%s 注册成功!" % username)


def manage(request):
    # if request.method == 'GET':
    #     return

    return render(request,"manage.html",{"msg":1000})


def update(request):

    print(request.POST.get('str'))
    # print(request.body)
    return HttpResponse('ok')