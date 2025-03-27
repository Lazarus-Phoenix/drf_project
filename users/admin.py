from django.contrib import admin

from lms.models import Course, Lesson
from users.models import CustomUser, Payment


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone", "city", "avatar")
    list_filter = ("email",)
    search_fields = ("email",)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "payment_date",
        "paid_course",
        "paid_lesson",
        "amount",
        "payment_method",
    )
    list_filter = ("payment_date",)
    search_fields = ("user", "paid_course", "paid_lesson")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "preview", "description")
    list_filter = ("title",)
    search_fields = ("title", "description")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "preview", "description", "video_link", "course")
    list_filter = ("title",)
    search_fields = ("title", "description")