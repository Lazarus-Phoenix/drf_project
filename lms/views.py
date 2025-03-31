from rest_framework import status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, get_object_or_404)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from lms.models import Course, Lesson, CourseSubscription
from lms.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsAdmin, IsModer, IsOwner
from rest_framework.permissions import IsAuthenticated


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated, ~IsModer)
        elif self.action in ["update", "retrieve","list"]:
            self.permission_classes = (IsAuthenticated, IsModer | IsOwner | IsAdmin,)
        if self.action == "destroy":
            self.permission_classes = (IsAuthenticated, ~IsModer, IsOwner | IsAdmin)
        return super().get_permissions()

    def perform_create(self, serializer):
        course = serializer.save(owner=self.request.user)
        course.save()


class LessonCreateApiView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModer]

    def perform_create(self, serializer):
        lesson = serializer.save(owner=self.request.user)
        lesson.save()


class LessonListApiView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsModer | IsOwner]


class LessonUpdateApiView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsModer | IsOwner]


class LessonRetrieveApiView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsAdmin | IsModer | IsOwner]


class LessonDestroyApiView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModer | IsAdmin | IsOwner]

class SubscribeToCourseView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        subscription, created = CourseSubscription.objects.get_or_create(
            user=request.user, course=course
        )
        if created:
            return Response(
                {"message": "Вы успешно подписались на обновления курса."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"message": "Вы уже подписаны на обновления этого курса."},
                status=status.HTTP_400_BAD_REQUEST,
            )

