from django.db import models

from config import settings
from lms.constants import USER_MODEL

# from users.models import CustomUser


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    preview = models.ImageField(
        upload_to="course_previews/", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    owner = models.ForeignKey(
        USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец",
    )
    subscribers = models.ManyToManyField(
        USER_MODEL, related_name="subscribed_courses", blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс"
    )
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    preview = models.ImageField(
        upload_to="lesson_previews/", blank=True, null=True, verbose_name="Превью"
    )
    video_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео")

    owner = models.ForeignKey(
        USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class CourseSubscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        unique_together = (
            "user",
            "course",
        )  # Уникальность подписки для каждого пользователя и курса

    def __str__(self):
        return f"{self.user.email} подписан на {self.course.name}"
