from django.conf.urls import url

from sixs import views

urlpatterns = [
    url(r'^hello/',views.hello,name='hello'),

    url(r'^news/',views.news,name='news'),
    url(r'^news2/',views.news2,name='news2'),
    url(r'^news3/',views.news3,name='news3'),
]