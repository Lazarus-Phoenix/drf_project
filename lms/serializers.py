from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_count(self, obj):
        try:
            return obj.lesson_set.count()
        except Course.DoesNotExist:
            return 0

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'course']