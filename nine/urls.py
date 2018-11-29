from django.conf.urls import url

from nine import views

urlpatterns = [
    url(r'^hello/',views.hello,name='name'),
    url(r'^add/',views.add,name='add'),
    url(r'^page/',views.page,name='page'),
]