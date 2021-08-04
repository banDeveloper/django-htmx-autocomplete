from django.db import models
from django.db.models.fields import CharField

class Country(models.Model):
    name = CharField(max_length=200)
    iso2 = CharField(max_length=2)
    iso3 = CharField(max_length=3)

    def __str__(self):
        return self.name


class City(models.Model):
    name = CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name
