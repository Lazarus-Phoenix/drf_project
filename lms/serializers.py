from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "title", "description", "course"]


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.IntegerField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "description", "lessons_count", "lessons","owner"]

    def get_lessons_count(self, obj):
        try:
            return obj.lesson_set.count()
        except Course.DoesNotExist:
            return 0
