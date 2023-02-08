import argparse
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
import csv
from common.models import Area

class Command(BaseCommand):
    help = 'Bulk Create or Update Area'

    def add_arguments(self, parser):
        parser.add_argument('csv', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        csvReader = csv.reader(options['csv'],delimiter=',')

        data = {}
        for row in csvReader:
            code = int(row[0])
            name = row[1]

            data[code] = name

        keys = []

        for k, v in data.items():
            keys.append(k)
            area, created = Area.objects.get_or_create(code=k, defaults={'name': v, 'center': '', 'version': timezone.now()})

            if created:
                continue

            area.name = k
            area.version = timezone.now()
        
        d = Area.objects.exclude(code__in=keys)
        d.delete()