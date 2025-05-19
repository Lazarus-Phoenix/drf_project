from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig

from lms.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonDestroyApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    SubscribeToCourseView,
    UnsubscribeFromCourseView,
)
from users.views import PaymentViewSet, UserViewSet

app_name = LmsConfig.name

router = SimpleRouter()

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lesson/new/", LessonCreateApiView.as_view(), name="new"),
    path("lesson/edit/<int:pk>/", LessonUpdateApiView.as_view(), name="edit"),
    path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="retrieve"),
    path("lesson/delete/<int:pk>/", LessonDestroyApiView.as_view(), name="delete"),
    path(
        "courses/<int:pk>/subscribe/",
        SubscribeToCourseView.as_view(),
        name="subscribe_to_course",
    ),
    path(
        "courses/<int:pk>/unsubscribe/",
        UnsubscribeFromCourseView.as_view(),
        name="unsubscribe_from_course",
    ),
]

router.register("", CourseViewSet)
router.register(r"payments", PaymentViewSet, basename="payments")
router.register(r"users", UserViewSet, basename="users")


urlpatterns += router.urls
