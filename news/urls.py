from django.urls import path, include
from .views import *

urlpatterns = [
    path('profil/',profil,name='profile'),
    path('post/<int:id>/', detail, name='detail'),
    path('profil_users/<int:id>/',profil_users,name='profil_users'),
    path('more/',more,name='more'),
    path('',lending,name='lending'),
]