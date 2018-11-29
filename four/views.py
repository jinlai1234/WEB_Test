from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def hello(request):
    return HttpResponse("Hello Session")


def login(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        # session有默认的过期时间，默认为14天，session的数据会固化到数据库中，并且session基于Cookie，Cokkie中有一个session_id，系统根据session数据库中的id来查找你想要的session，所以最好退出登录不要删除cookie注销4
        # session默认支持中文
        request.session['username'] = u_name
        # 下面这个删除session{注意删除的知识session_data中的数据}
        # del request.session['username']
        # NB删除能够将cookie和session一起删除
        # request.session.flusj()
        response = redirect(reverse('four:mine'))
        return response
    elif request.method == 'GET':
        return render(request,'four/login.html')


def mine(request):
    # 两者都可以获取session中的数据，但是[]情况下如果键不存在就会报错
    username2 = request.session['username']
    username1 = request.session.get('username')
    data = {
        'status':200,
        'message':'Hello',
        'name1':username1,
        'name2':username2,
    }
    response = JsonResponse(data=data)
    return response