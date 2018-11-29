from django.conf.urls import url

from four import views

urlpatterns=[
    url(r'^hello/',views.hello,name='hello'),
    url(r'^login/',views.login,name='login'),
    url(r'^mine/',views.mine,name='mine'),
]