from django.core.management.base import BaseCommand

from


class Command(BaseCommand):
    help = 'Displays all customers'

    def handle(self, *args, **options):
        all = Customer.objects.all()
        self.stdout.write(f'{all}')

