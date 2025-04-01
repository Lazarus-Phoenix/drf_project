from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from lms.models import Lesson, Course
from django.contrib.auth import get_user_model
from lms.constants import USER_MODEL


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(email="test@test.ru")
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title="Test Course",
            description="Test Description"
        )

        self.lesson = Lesson.objects.create(
            title="Lesson",
            video_link="https://www.youtube.com/lesson1/",
            owner=self.user,
            course=self.course
        )

    def test_lesson_detail(self):
        url = reverse("lms:retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(self.lesson.owner, self.user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        url = reverse("lms:new")
        data = {
            "title": "test_lesson",
            "video_link": "https://www.youtube.com/testlesson/",
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_create_invalid_link(self):
        url = reverse("lms:new")
        data = {
            "title": "test_lesson",
            "video_link": "https://www.vkvideo.com/testlesson/",
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json().get("video_link"),
                         ["Ссылка на сторонний ресурс обнаружена в поле video_link"])
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_lesson_update(self):
        url = reverse("lms:edit", args=(self.lesson.pk,))
        data = {"title": "test_lesson1"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "test_lesson1")

    def test_lesson_delete(self):
        url = reverse("lms:delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse("lms:lessons_list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['next'], None)
        self.assertEqual(data['previous'], None)
        lesson_data = data['results'][0]
        self.assertEqual(lesson_data['id'], self.lesson.pk)
        self.assertEqual(lesson_data['title'], self.lesson.title)
        self.assertEqual(lesson_data['description'], None)
        self.assertEqual(lesson_data['video_link'], self.lesson.video_link)
        self.assertEqual(lesson_data['course'], self.course.pk)