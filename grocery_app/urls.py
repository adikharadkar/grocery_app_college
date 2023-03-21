from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="app-home"),
	path('shop-by-category/', views.category, name="app-categories"),
	path('shop-by-category/fruits-and-vegetables/', views.category_fruits_vegetables, name="category-fruits-vegetables"),
	path('shop-by-category/beverages/', views.category_beverages, name="category-beverages")
]