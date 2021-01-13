from django.http import JsonResponse
from django.shortcuts import render, HttpResponse


# Create your views here.

# 首页
def index(request):
    return render(request, "index.html")
