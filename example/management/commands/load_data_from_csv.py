import csv
from os import name
from pathlib import Path

from django.core.management.base import BaseCommand
from example.models import Country, City

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent


class Command(BaseCommand):
    help = 'Populates Country and City models with data in src/worldcities.csv'

    def handle(self, *args, **options):
        cities = []
        with open(BASE_DIR / 'worldcities.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                # change these if importing from a different file
                country, created = Country.objects.get_or_create(
                    name=row[4],
                    iso2=row[5],
                    iso3=row[6]
                )
                # deal with empty values
                if row[9] == '':
                    population = 0
                # and with . separated ones
                else:
                    population = int(row[9].replace('.', ''))
                country=Country.objects.get(name=row[4])
                cities.append(City(
                    name=row[1],
                    country=country,
                    population=population
                ))
        # much faster than creating each individually
        City.objects.bulk_create(
            cities,
            100
        )

        self.stdout.write(self.style.SUCCESS(
            f'Successfully populated {Country.objects.count()} countries and {City.objects.count()} cities!'))
