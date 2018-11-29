from django.conf.urls import url

from three import views

urlpatterns = [
     url(r'^hello/', views.hello, name='hello'),
     
     url(r'^login/',views.login,name='login'),
     url(r'^dologin/',views.dologin,name='dologin'),
     url(r'^mine/',views.mine,name='mine'),
]