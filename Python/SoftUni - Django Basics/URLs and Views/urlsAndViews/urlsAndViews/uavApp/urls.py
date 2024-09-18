from django.urls import path, re_path
from urlsAndViews.uavApp import views


urlpatterns = [
    path('', views.index, name='home'),
    path('redirect', views.redirect_view),
    path('<int:pk>/<slug:slug>/', views.slug_view),
    path('<int:pk>/', views.view_with_pk, name='primary'),
    path('softuni/', views.redirect_to_softuni),
    path('<key>/', views.view_with_args_and_kwargs, name='vak'),
    re_path(r'^archive/(?P<archive_year>202[0-3])/$', views.show_archive),
    path('<variable>/', views.view_with_name),
    path('<path:variable>/', views.view_with_name),
]