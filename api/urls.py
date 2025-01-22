from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.list_posts),
    path('posts/<int:id>/', views.detail_post),
    path('posts_update/<int:id>/',views.update),
]