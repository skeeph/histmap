from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.utils.text import slugify

from accounts.models import Profile


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
            Profile.objects.create(user=u,
                                   slug=slugify('{f} {l}'.
                                                format(f=u.first_name,
                                                       l=u.last_name),
                                                allow_unicode=True))
            self.stdout.write("Superuser created!. Don't forget to change password")
