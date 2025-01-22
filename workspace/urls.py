from django.urls import path

from . import views


urlpatterns = [
    path('create',views.create,name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('<int:id>/',views.delete,name='delete'),
    path('', views.workspace, name='workspace'),

]