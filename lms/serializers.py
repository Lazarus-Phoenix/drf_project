from django.core.validators import URLValidator
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson
from lms.validators import ExternalLinksValidator

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "description", "course", "video_link"]
        extra_kwargs = {
            "video_link": {
                "validators": [
                    URLValidator(), # Проверяет, что это валидный URL
                    ExternalLinksValidator(field="video_link"), # Проверяет домен
                ]
            },
            "description": {
                "validators": [
                    ExternalLinksValidator(field="description") # Проверяет описание
                ]
            },
        }


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.IntegerField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "lessons_count", "lessons", "owner"]
        extra_kwargs = {
            "description": {"validators": [ExternalLinksValidator(field="description")]}
        }


    def get_lessons_count(self, obj):
        try:
            return obj.lesson_set.count()
        except Course.DoesNotExist:
            return 0
