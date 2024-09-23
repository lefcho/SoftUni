from django.urls import path
from forum.posts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
]
