from django.urls import path

from authors import views

urlpatterns = [
    path('create/', views.AuthorCreateView.as_view(), name='add-author'),
    path('datails/', views.AuthorDetailsView.as_view(), name='details-author'),
    path('edit/', views.AuthorEditView.as_view(), name='edit-author'),
    path('delete/', views.AuthorDeleteView.as_view(), name='delete-author'),
]
