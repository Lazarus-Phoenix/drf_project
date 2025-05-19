from django.core.validators import URLValidator
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson
from lms.validators import ExternalLinksValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "description", "course", "video_link", "owner"]
        extra_kwargs = {
            "video_link": {
                "validators": [
                    URLValidator(),  # Проверяет, что это валидный URL
                    ExternalLinksValidator(field="video_link"),  # Проверяет домен
                ]
            },
            "description": {
                "validators": [
                    ExternalLinksValidator(field="description")  # Проверяет описание
                ]
            },
        }


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.IntegerField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "lessons_count",
            "lessons",
            "owner",
            "is_subscribed",
        ]
        extra_kwargs = {
            "description": {"validators": [ExternalLinksValidator(field="description")]}
        }

    def get_is_subscribed(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.subscribers.filter(id=request.user.id).exists()
        return False

    def get_lessons_count(self, obj):
        try:
            return obj.lesson_set.count()
        except Course.DoesNotExist:
            return 0
