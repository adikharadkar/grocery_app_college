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