from django.conf.urls import url

from eight import views

urlpatterns = [
    url(r'^hello/',views.hello,name='hello'),
    url(r'^new/',views.hello,name='new'),
]