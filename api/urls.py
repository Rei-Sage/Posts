from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .yasg import urlpatterns as url_doc
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register('avatar', views.AvatarViewSet)
router.register('categories', views.CategoryViewSet)
router.register('tags', views.TagViewSet)
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('', include(router.urls))

]
urlpatterns += url_doc


{
    "id": 1,
    "username": "Rei",
    "email": "rei@gmail.com",
    "phone_number": "+996555555555",
    "gender": "male",
    "race": "asian",
    "password":2005
}


