import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from nine.models import Student


def hello(request):
    return HttpResponse('Hello 分页')

def add(request):
    for i in range(20):
        students = Student(name='Jack%s'%(random.randrange(100000)),age='%s'%(random.randrange(100000)))
        students.save()
    return HttpResponse('students add success')


def page(request):
    return None