from django.conf.urls import url, include
# from django.conf import admin
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', (views.index), name = 'index'),
    path('signup', views.signup, name = 'signup'),
    path('loginpage', views.loginpage, name = 'loginpage'),
    path('login', views.login , name='login' ),
    path('logout', views.logout , name='logout' ),
    path('Alienation', (views.page_01) , name='page_01' ),
    path('Anxiety', (views.page_02) , name='page_02' ),
    path('Depression', (views.page_03) , name='page_03' ),
    path('PCOS', (views.page_04) , name='page_04' ),
]
