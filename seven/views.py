

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from seven.models import Icon


def hello(request):
    # 直接URL：http://127.0.0.1:8000/static/img/tupian.png可以打开静态文件图片
    return HttpResponse('Hello 图片上传')
    # return render(request,'seven/fuck.html')
    # return JsonResponse(data={'link':'ok'})

# 万金油图像储存方式[缺点：位置固定，更换环境之后需要更改目标位置]
def image(request):
    if request.method == 'GET':
        return render(request,'seven/fuck.html')
    elif request.method == 'POST':
        print("ok")
        imagess = request.FILES.get('imagess')
        print(imagess)
        # with可以自动释放资源获取空间
        with open(r'C:\Users\Normann\Desktop\RongWEB\static\img\img.png','wb') as a:
            for part in imagess.chunks():
                a.write(part)
                a.flush()
    return HttpResponse("image upload ok")

def goimagess(request):
    return redirect(reverse('seven:helloseven'))


# 添加豁免装饰器可以直接跳过csrf验证
@csrf_exempt
def newimg(request):
    if request.method == 'GET':
        return render(request,'seven/index.html')
    elif request.method == 'POST':
        images = request.FILES.get('imagess')
        users = request.POST.get('names')
        icon = Icon(ico=images,name=users)
        icon.save()
        return HttpResponse("save success")


def login(request):
    if request.method == 'GET':
        return render(request,'seven/login.html')
    elif request.method == 'POST':
        names = request.POST.get('names')
        if Icon.objects.filter(name=names):
            user = Icon.objects.get(name=names)
            # session写到request中直接
            # 如果是Cookie就需要使用实例化return对象response之后，使用set_cookie('键',值[,max_age=秒])指令来进行设置cookie，获取cookie也是resquest.COOKIES.get('键')
            request.session['name']=user.name
            request.session['icons']=user.ico.url
            return redirect(reverse('seven:mine'))
        else :
            data={
                'status':404,
                'message':'用户名错误'
            }
            return JsonResponse(data=data)


def mine(request):
    names = request.session.get('name')
    icons = request.session.get('icons')
    print(icons)
    print(type(icons))
    context = {
        'name':names,
        'icons':'/static/img/'+icons
    }
    return render(request,'seven/mine.html',context=context)


