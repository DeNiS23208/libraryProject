from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email= 'overlord@mail.ru',
            first_name='Denis',
            last_name='Gulyaev',
        )
        user.set_password('232')
        user.is_staff = True
        user.is_superuser = True



        user.save()

        self.stdout.write(self.style.SUCCESS(f'Администратор создан мать его {user.email}!'))