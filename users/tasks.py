from celery import shared_task
from celery.beat import logger
from django.utils import timezone
from datetime import timedelta
from users.models import CustomUser


# @shared_task
# def check_last_login():
#     """Заблокировать пользователей, не активных в течение месяца"""
#     month_ago = timezone.now() - timedelta(days=30)
#     inactive_users = CustomUser.objects.filter(last_login__lt=month_ago, is_active=True)
#     inactive_users.update(is_active=False)


@shared_task(bind=True)
def check_last_login(self):
    """Заблокировать пользователей, не активных в течение месяца"""
    try:
        month_ago = timezone.now() - timedelta(days=30)
        inactive_users = CustomUser.objects.filter(
            last_login__lt=month_ago, is_active=True
        )

        if inactive_users.exists():
            updated_count = inactive_users.update(is_active=False)
            logger.info(
                f"Блокировка завершена: {updated_count} пользователей обновлено"
            )

    except Exception as e:
        logger.error(f"Ошибка при блокировке пользователей: {str(e)}")
        raise self.retry(countdown=60 * 5)  # Повторная попытка через 5 минут
