from django.urls import path

from common import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]