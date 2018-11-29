from django.conf.urls import url

from five import views

urlpatterns = [
    url(r'^hello/',views.hello,name='hello'),


    url(r'^adduser/',views.adduser,name='adduser'),
    url(r'^addcardid/',views.addcardid,name='addcardid'),
    url(r'^user_card/',views.user_card,name='user_card'),

    url(r'^add_cat/',views.add_cat,name='add_cat'),
    url(r'^add_dog/',views.add_dog,name='add_dog')
]