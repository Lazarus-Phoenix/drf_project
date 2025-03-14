from rest_framework.serializers import ModelSerializer

from lms.models import Course, Lesson


class UserSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"