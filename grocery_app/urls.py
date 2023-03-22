from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="app-home"),
	path('shop-by-category/', views.category, name="app-categories"),
	path('shop-by-category/fruits-and-vegetables/', views.category_fruits_vegetables, name="category-fruits-vegetables"),
	path('shop-by-category/beverages/', views.category_beverages, name="category-beverages"),
	path('shop-by-category/snack-store/', views.category_snack_store, name="category-snack-store"),
	path('shop-by-category/cleaning-household', views.category_cleaning_household, name="category-cleaning-household"),
	path('shop-by-category/beauty-hygiene', views.category_beauty_hygiene, name="category-beauty-hygiene"),
	path('shop-by-category/home-kitchen', views.category_home_kitchen, name="category-home-kitchen")
]