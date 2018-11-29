"""RongWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/',include('app.urls',namespace='app')),
    url(r'^two/',include('two.urls',namespace='two')),
    url(r'^three/',include('three.urls',namespace='three')),
    url(r'^four/',include('four.urls',namespace='four')),
    url(r'^five/',include('five.urls',namespace='five')),
    url(r'^sixs/',include('sixs.urls',namespace='sixs')),
    url(r'^seven/',include('seven.urls',namespace='seven')),
    url(r'^eight/',include('eight.urls',namespace='eight')),
    url(r'^',include('nine.urls',namespace='nine')),

]
