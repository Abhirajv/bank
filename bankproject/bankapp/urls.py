from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('login', views.login, name='login'),
    path('register',views.register,name='register'),
    path('form',views.form,name='form'),
    path('message',views.message,name='message'),
    path('newlog',views.newlog,name='newlog'),
    path('logout',views.logout,name='logout'),
    path('index', views.index, name='index')


]