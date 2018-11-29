from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    a = 10
    b= 0
    c = a/b
    # 因为设置了错误跳转因此如果网页出现5XX错误会直接出现自定义404错误页面
    return HttpResponse(c)