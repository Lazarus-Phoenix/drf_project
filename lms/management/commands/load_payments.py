import datetime

from django.core.management.base import BaseCommand

from lms.models import Course, Lesson
from users.models import CustomUser, Payment


class Command(BaseCommand):
    help = "Create sample users, courses, lessons and load sample payments"

    def handle(self, *args, **options):
        # Создаем несколько пользователей
        emails = [
            "user1@email.com",
            "user2@email.com",
            "user3@email.com",
            "user4@email.com",
            "user5@email.com",
        ]
        passwords = [
            "password123",
            "password456",
            "password789",
            "password012",
            "password345",
        ]

        for i in range(len(emails)):
            CustomUser.objects.create(email=emails[i], password=passwords[i])

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {len(emails)} sample users")
        )

        # Создаем тестовые курсы
        courses = [
            Course(
                title="Python Basics",
                preview=None,
                description="Introduction to Python programming",
            ),
            Course(
                title="Data Structures and Algorithms",
                preview=None,
                description="Advanced data structures and algorithms",
            ),
            Course(
                title="Web Development",
                preview=None,
                description="Building web applications with Django",
            ),
            Course(
                title="Machine Learning",
                preview=None,
                description="Introduction to machine learning techniques",
            ),
            Course(
                title="Database Management",
                preview=None,
                description="Design and management of databases",
            ),
        ]

        Course.objects.bulk_create(courses)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {len(courses)} sample courses")
        )

        # Создаем тестовые уроки
        lessons = []
        for course in Course.objects.all():
            if len(lessons) < 6:
                lesson_title = f"{course.title} - Lesson {len(lessons)+1}"
                lessons.append(
                    Lesson(
                        course=course,
                        title=lesson_title,
                        description=f"Lesson {len(lessons)+1} for {course.title}",
                        preview=None,
                        video_link=None,
                    )
                )

        Lesson.objects.bulk_create(lessons)

        self.stdout.write(
            self.style.SUCCESS(f"Successfully created {len(lessons)} sample lessons")
        )

        # Загружаем данные о пользователях
        users = CustomUser.objects.all()

        # Загружаем данные о курсах
        courses = Course.objects.all()

        # Загружаем данные о уроках
        lessons = Lesson.objects.all()

        # Создаем примерные платежи
        for user in users:
            for course in courses:
                payment = Payment(
                    user=user,
                    paid_course=course,
                    payment_date=datetime.datetime.now(),
                    amount=100.00,
                    payment_method="cash",
                )
                payment.save()

            for lesson in lessons:
                payment = Payment(
                    user=user,
                    paid_lesson=lesson,
                    payment_date=datetime.datetime.now(),
                    amount=50.00,
                    payment_method="transfer",
                )
                payment.save()

        self.stdout.write(self.style.SUCCESS("Successfully loaded sample payments"))
