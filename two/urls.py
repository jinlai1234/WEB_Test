from django.conf.urls import url

from two import views

urlpatterns = [
    url(r'^getss/$',views.gets,name='gets'),
    url(r'^getss/(?P<g_id>\d+)/',views.getss,name='getss'),
    url(r'^message/(?P<s_id>\d+)/',views.message,name='message'),

    url(r'^add_del/',views.add_del,name='add_del')
]