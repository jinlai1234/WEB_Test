from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^hello/',views.hello,name='hello'),
    url(r'^index/',views.index,name='index'),
    url(r'^getstudent/',views.getstudent,name='getstudent'),

    url(r'entendss/',views.entendss,name='entendss')
]