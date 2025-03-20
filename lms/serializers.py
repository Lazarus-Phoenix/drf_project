from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons_info = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        # Подсчет количества уроков, связанных с данным курсом

        return obj.lesson.count()

    def get_lessons_info(self, obj):
        # Получение информации об уроках, связанных с данным курсом

        return LessonSerializer(obj.lessons.all(), many=True).data

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'lessons_count', 'lessons_info']


class LessonSerializer(ModelSerializer):


    class Meta:
        model = Lesson
        fields = "__all__"