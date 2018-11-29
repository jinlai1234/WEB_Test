from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from app.models import Students


def hello(request):
    '''
    测试
    '''
    return render(request,'app/base.html')


def index(request):
    '''
    首先loader一个templates
    再渲染成HTML
    然后输出
    '''
    temp = loader.get_template('app/index.html')
    # print(temp)
    content = temp.render()
    # print(content)
    return HttpResponse(content)
    # return render(request,'app/index.html')


def getstudent(request):
    student = Students.objects.all()
    student_none = Students.objects.all().filter(name='desk')
    hobby = {
        "coding_time1":'three_years1',
        "coding_time2":'three_years2',
    }
    context = {
        'students':student,
        'student_none':student_none,
        'hobby':hobby,
    }
    return render(request,'app/index.html',context=context)


def entendss(request):
    return render(request,'app/second.html')