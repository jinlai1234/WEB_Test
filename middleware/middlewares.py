import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class HelloMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print('有个小崽子在访问你，他的IP是:'+request.META.get('REMOTE_ADDR'))
        # request.path能够返回对方访问的url
        # print(request.path)
        # 黑名单配置
        if request.path == '/hello/':
            ip = request.META.get('REMOTE_ADDR')
            # if cache.get(ip):
            #     return HttpResponse("10S之后再来，一直访问个屁啊")
            # cache.set(ip,ip,timeout=10)
            # if request.META.get('REMOTE_ADDR') == '10.0.122.202':
            #     return HttpResponse('滚犊子')
            black_list = cache.get(ip,[])
            requests = cache.get(ip,[])
            if ip in black_list:
                return HttpResponse('滚')
            else:
                while requests and time.time() - requests[-1] > 60:
                    requests.pop()
                requests.insert(0, time.time())
                cache.set(ip,requests, timeout=60)
                if len(requests) > 30:
                    black_list.append(ip)
                    cache.set(ip,black_list,timeout=60*60*24)
                    return HttpResponse('屏蔽了谢谢')
                if len(requests) > 10:
                    return HttpResponse('你这也太急了吧')

    def process_exception(self,request,exception):
        print("出现错误")
        return render(request,'404.html')
            