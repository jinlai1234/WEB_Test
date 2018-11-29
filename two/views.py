from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from two.models import Grade, Student
def gets(request):
    grade = Grade.objects.all()
    context = {
        'grade':grade
    }
    return render(request,'two/index.html',context=context)


def getss(request,g_id):
    student = Student.objects.filter(s_grade_id=g_id)

    return render(request,'two/student_list.html',context={"students":student})


def message(request,s_id):
    student = Student.objects.filter(id=s_id)
    context = {
        "studentss":student
    }
    return render(request,'two/message.html',context=context)


def add_del(request):
    if request.method == 'POST':
        name = request.POST.get('s_names')
        if Student.objects.filter(s_name=name):
            print("进入删除")
            STUDENT =Student.objects.get(s_name=name)
            STUDENT.delete()
            return HttpResponse("删除成功")
        else:
            print("进入创建")
            STUDENT =Student()
            STUDENT.s_name = name
            STUDENT.s_grade_id = 1
            STUDENT.save()
            return HttpResponse("创建成功")