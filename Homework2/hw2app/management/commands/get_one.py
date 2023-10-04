from django.core.management.base import BaseCommand

from hw2app.models import Customer


class Command(BaseCommand):
    help = 'Displays one customer by pk'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='CoinFlip pk')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        customer = Customer.objects.get(id=pk)
        self.stdout.write(f'{customer}')