# Django HTMX autocomplete example

## Installation

```python
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
# populates Country and City models with data from worldcities.csv
# look at example/management/commands/load_data_from_csv.py to change it
python manage.py load_data_from_csv
```

![Preview](https://i.imgur.com/0Q7Dm8o.png)