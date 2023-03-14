from django.core.management.base import BaseCommand, CommandError
from polls.models import User


class Command(BaseCommand):
    help = 'Delete Users'

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int)

    def handle(self, *args, **options):
        user_id = options['user_id']
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise CommandError('User with ID {} does not exist'.format(user_id))

        if user.is_superuser:
            raise CommandError('Superuser cannot be deleted')

        user.delete()


