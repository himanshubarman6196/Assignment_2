from django.contrib import admin
from django.urls import path, include
from .views import DetailView, SearchView, get_images, IndexView

urlpatterns = [
	path('',IndexView,name='IndexView'),
    path('detail/',DetailView,name='detail'),
    path('search/',SearchView,name='search'),
    path('get_images/',get_images,name='get_images'),
]