from django.urls import path
from toDoProject.toDoApp.views import index_view

urlpatterns = [
    path('', index_view),
]