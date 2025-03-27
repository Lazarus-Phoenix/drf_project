from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

from users.models import CustomUser


class Command(BaseCommand):
    help = 'Create moderators group'

    def handle(self, *args, **options):
        moderators_group, created = Group.objects.get_or_create(name='Модераторы')

        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модераторы" успешно создана.'))

            # Получаем всех активных пользователей с ролью staff
            active_staff_users = CustomUser.objects.filter(is_staff=True, is_active=True)

            # Добавляем каждого пользователя в группу "Модераторы"
            for user in active_staff_users:
                user.groups.add(moderators_group)
                self.stdout.write(self.style.SUCCESS(f'Пользователь {user.email} добавлен в группу модераторы'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Модераторы" уже существует'))