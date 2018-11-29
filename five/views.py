import random


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from five.models import Person, IDCard, Cat, Dog


def hello(request):
    return HttpResponse('Hello')


def adduser(request):
    user_name = request.GET.get("u_name")
    user = Person(p_name=user_name)
    user.save()
    data = {
        'status':'200',
        'message':'%s user add success'%(user_name)
    }
    return JsonResponse(data=data)


def addcardid(request):
    card_id = request.GET.get('card_id')
    id_card = IDCard(id_num=card_id)
    id_card.save()
    data = {
        'status': '200',
        'message': 'card id %s add success' % (card_id)
    }
    return JsonResponse(data=data)


def user_card(request):
    # 注意主从获取，主获取从是隐性属性，默认是级联模型的名字，从获取主是显性属性，就是属性的名字
    # order_by 方法可以针对一个列名进行排序，加-号可以反向排列
    user = Person.objects.all().order_by('id').last()
    users = Person.objects.filter(id)
    # user = Person.objects.last()
    card = IDCard.objects.last()
    card.id_person=user
    card.save()
    return HttpResponse("Bind Success")


def add_cat(request):
    c = Cat(a_anme='Tom %s'%(random.randrange(10000)),c_eat='fish')
    c.save()
    Web = loader.get_template('five/index.html')
    response = Web.render()
    Response = HttpResponse(response)
    Response.content = {'successful':"successful"}
    return Response


def add_dog(request):
    d = Dog(a_anme='Tom %s'%(random.randrange(10000)),d_eat='fish')
    d.save()
    Web = loader.get_template('five/index.html')
    response = Web.render()
    Response = HttpResponse(response)
    Response.content = {'successful':"successful"}
    return Response