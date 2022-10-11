from django.core.management.base import BaseCommand
from cashier.apps.accounts.models import User


class Command(BaseCommand):
    help = 'Create an initial superadmin user'

    def handle(self, *args, **options):

        user = User.objects.filter(username='superadmin', email='superadmin@admin.com').first()
        if not user:
            user = User.objects.create_superuser(username='superadmin', email='superadmin@admin.com',
                                                 password='password', first_name='Super', last_name='Admin',
                                                 role=User.RoleChoices.ADMIN)

        self.stdout.write(self.style.SUCCESS('Successfully created superadmin user'))