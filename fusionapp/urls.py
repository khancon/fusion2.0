from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('artist/', views.ArtistListView.as_view(), name='artist_list'),
    path('artist/add/', views.ArtistCreate.as_view(), name='artist_add'),
    path('artist/<int:pk>/', views.ArtistDetailView.as_view(), name='artist_details'),
    path('artist/<int:pk>/update', views.ArtistUpdate.as_view(), name='artist_update'),
    path('artist/<int:pk>/delete', views.ArtistDelete.as_view(), name='artist_delete'),
    path('album/', views.AlbumListView.as_view(), name='album_list'),
    path('album/add/', views.album_create , name='album_add'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_details'),
    # path('album/<int:pk>/update', views.AlbumUpdate.as_view(), name='album_update'),
    # path('album/<int:pk>/delete', views.AlbumDelete.as_view(), name='album_delete'),
]