from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    # Show this when the user types help
    help = "Creates default superuser noninteractively with login admin and pass admin"

    # A command must define handle()
    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True).count() != 0:
            self.stdout.write("Superuser exists!")
        else:
            u = User(username='admin')
            u.set_password('admin')
            u.is_superuser = True
            u.is_staff = True
            u.save()
            self.stdout.write("Superuser created!. Don't forget to change password")
