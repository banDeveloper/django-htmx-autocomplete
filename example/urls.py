from django.urls import path
from .views import (
    home_view,
    autocomplete_return_all,
    autocomplete_return_first,
    autocomplete_populate_option,
    search_cities
)

app_name = 'example'

urlpatterns = [
    path('search-all/', autocomplete_return_all, name='autocomplete_return_all'),
    path('search-one/', autocomplete_return_first, name='autocomplete_return_first'),
    path('search-option/', autocomplete_populate_option, name='autocomplete_populate_option'),
    path('search-cities/', search_cities, name='search_cities'),
    path('', home_view, name='home'),
]
