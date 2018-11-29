import random
from time import sleep

from django.core.cache import caches, cache
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


def hello(request):

    return HttpResponse('Hello 各种缓存')

# 导入这个cache包后面定义的为过期时间下面定义的为30S
@cache_page(30)
def news(request):
    
    list = []
    # python manage.py createcachetable cache
    for i in range(10):
        sleep(1)
        list.append('%s只羊'%(random.randrange(100000)))
    data = {
        'list':list
    }
    return render(request,'sixs/index.html',context=data)


# 不适用装饰器的缓存
def news2(request):
    rel = cache.get('news2')
    if rel:
        return HttpResponse(rel)
    else:
        list = []
        # python manage.py createcachetable cache
        for i in range(10):
            sleep(1)
            list.append('%s只猪' % (random.randrange(100000)))
        data = {
            'list': list
        }
        response = render(request, 'sixs/index.html', context=data)
        cache.set('news2',response.content,timeout=30)
        return  response


# 不适用装饰器并且使用Redis缓存
def news3(request):

    cache = caches['redis_backend']

    rel = cache.get('news3')
    if rel:
        return HttpResponse(rel)
    else:
        list = []
        # python manage.py createcachetable cache
        for i in range(10):
            sleep(1)
            list.append('%s只你' % (random.randrange(100000)))
        data = {
            'list': list
        }
        response = render(request, 'sixs/index.html', context=data)
        cache.set('news3',response.content,timeout=30)
        return  response