from django.core.management.base import BaseCommand
from users.models import CustomUser, Payment
from lms.models import Course, Lesson

class Command(BaseCommand):
    help = 'Clear database'

    def handle(self, *args, **options):
        CustomUser.objects.all().delete()
        Course.objects.all().delete()
        Lesson.objects.all().delete()
        Payment.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Database cleared successfully'))