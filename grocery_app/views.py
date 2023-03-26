from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'grocery_app/home.html')

def category(request):
	return render(request, 'grocery_app/category.html')

def category_fruits_vegetables(request):
	return render(request, 'grocery_app/categories/fruits-and-vegetables.html')

def category_beverages(request):
	return render(request, 'grocery_app/categories/beverages.html')

def category_snack_store(request):
	return render(request, 'grocery_app/categories/snack-store.html')

def category_cleaning_household(request):
	return render(request, 'grocery_app/categories/cleaning-household.html')

def category_beauty_hygiene(request):
	return render(request, 'grocery_app/categories/beauty-hygiene.html')

def category_home_kitchen(request):
	return render(request, 'grocery_app/categories/home-kitchen.html')

def login(request):
	return render(request, 'grocery_app/login.html')