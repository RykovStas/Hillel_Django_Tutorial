from faker import Faker

from django.core.management.base import BaseCommand
from polls.models import User

fake = Faker()

class Command(BaseCommand):
    help = 'Generate Users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1,10))

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=fake.name(), email=fake.email(), password=fake.password())
