from django.urls import path, include
from .views import *
app_name='users'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),  
    path("register/", register, name="register"),
    path('change_password/', change_password, name='change_password'),
    path('change_profile/',change_profile,name='change_profile'),
    path('change_image',change_image,name='change_image')
] 



