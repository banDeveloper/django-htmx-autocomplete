from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Country, City

def home_view(request):
    return render(request, "home.html", {})

def autocomplete_return_all(request):
    if request.method == 'POST':
        term = request.POST["search"]
        countries = Country.objects.filter(name__istartswith=term).order_by('name')
        context = {
            "countries": countries
        }
        return render(request, "autocomplete_all.html", context)

def autocomplete_return_first(request):
    if request.method == 'POST':
        term = request.POST["search"]
        country = Country.objects.filter(name__istartswith=term).order_by('name').first()
        context = {
            "country": country
        }
        return render(request, "autocomplete_one.html", context)

def autocomplete_populate_option(request):
    if request.method == 'POST':
        term = request.POST["search"]
        countries = Country.objects.filter(name__istartswith=term).order_by('name')
        context = {
            "countries": countries
        }
        return render(request, "autocomplete_option.html", context)

def search_cities(request):
    if request.method == 'POST':
        term = request.POST["country"]
        country_qs = Country.objects.filter(name=term)
        if country_qs.exists():
            cities = City.objects.filter(country=country_qs.first())
            context = {
                "cities": cities
            }
            return render(request, "cities.html", context)