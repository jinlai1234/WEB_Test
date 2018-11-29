from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def login(request):
    u_name = request.POST.get('username')
    response = redirect(reverse('three:mine'))
    response.set_cookie('name',u_name,max_age=30)
    # 删除cookie
    # response.delete_cookie('name')
    return response


def mine(request):
    name = request.COOKIES.get('name')

    return render(request,'three/mine.html',context={'names':name})


def dologin(request):
    return render(request,'three/login.html')

def hello(request):
    return HttpResponse('Hello Cookies')