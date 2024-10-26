from django.urls import path, include

from albums import views

urlpatterns = [
    path('add/', views.AddAlbumView.as_view(), name='add-album'),
    path('<int:id>/', include([
        path('details/', views.DetailsAlbumView.as_view(), name='details-album'),
        path('edit/', views.EditAlbumView.as_view(), name='edit-album'),
        path('delete/', views.DeleteAlbumView.as_view(), name='delete-album'),
    ]))
]
