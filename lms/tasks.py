from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from lms.models import Course, CourseSubscription
from users.models import CustomUser


@shared_task
def send_course_update_email(course_id):
    """Отправка писем с сообщением об обновлении курса"""
    """
    Временная проверка важна для предотвращения спама уведомлений. 
    Если курс обновляется часто (менее чем раз в 4 часа), 
    система не будет беспокоить подписчиков слишком частыми уведомлениями.
    """
    course = Course.objects.get(id=course_id)
    subscriptions = CourseSubscription.objects.none()
    if timezone.now() - course.updated_at > timedelta(hours=4):
        subscriptions = CourseSubscription.objects.filter(course_id=course_id)

    if subscriptions.exists():
        for subscription in subscriptions:
            print(f"Отправка письма на {subscription.user.email}")
            send_mail(
                "Обновление курса",
                f"Курс {subscription.course.title} был обновлён.",
                EMAIL_HOST_USER,
                [
                    subscription.user.email,
                ],
                fail_silently=False,
            )
    else:
        print(f"Уведомление не отправлено, курс был обновлен менее 4 часов назад.")


@shared_task
def block_inactive_users():
    """Заблокировать пользователей, не активных в течение месяца"""
    month_ago = timezone.now() - timedelta(days=30)
    inactive_users = CustomUser.objects.filter(last_login__lt=month_ago, is_active=True)
    inactive_users.update(is_active=False)
