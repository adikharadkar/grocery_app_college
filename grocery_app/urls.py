from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="app-home"),
	path('shop-by-category/', views.category, name="app-categories")
]