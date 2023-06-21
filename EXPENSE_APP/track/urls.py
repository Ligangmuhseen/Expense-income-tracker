
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index1,name='index1'),
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('registration',views.registration,name='registration'),


]
