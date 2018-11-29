from django.conf.urls import url

from seven import views

urlpatterns = [
    url(r'^hello/',views.hello,name='helloseven'),
    url(r'^go/',views.goimagess,name='goimage'),
    url(r'^image/',views.image,name='image'),

    url(r'^newimg/',views.newimg,name='newimg'),

    url(r'^login/',views.login,name='login'),
    url(r'^mine/',views.mine,name='mine'),

]