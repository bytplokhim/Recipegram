import csv

from django.conf import settings
from django.core.management import BaseCommand
from recipes.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data_path = settings.BASE_DIR
        with open(
            f'{data_path}/recipes/data/tags.csv',
            'r',
            encoding='utf-8'
        ) as file:
            reader = csv.DictReader(file)
            Tag.objects.bulk_create(Tag(**tag) for tag in reader)
        self.stdout.write(self.style.SUCCESS('Теги загружены.'))
