from django.core.management.base import BaseCommand

from hw2app.models import Customer


class updateCustomer(BaseCommand):
    help = 'Updates a customer by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='CoinFlip pk')
    def handle(self, *args, **options):
        pk = options.get['pk']
        name = options.get('name')
        customer = Customer.objects.filter(pk=pk).first()
        Customer.name = name
        customer.save()
        self.stdout.write(f'{customer}')