# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, override_settings
# from lms.models import Course, CourseSubscription, Lesson
#
#
# @override_settings(DEBUG=True)
# class LessonTestCase(APITestCase):
#     def setUp(self) -> None:
#         self.user = get_user_model().objects.create(email="test@test.ru")
#         self.client.force_authenticate(user=self.user)
#
#         self.course = Course.objects.create(
#             title="Test Course", description="Test Description"
#         )
#
#         self.lesson = Lesson.objects.create(
#             title="Lesson",
#             video_link="https://www.youtube.com/lesson1/",
#             owner=self.user,
#             course=self.course,
#         )
#
#     def test_lesson_detail(self):
#         url = reverse("lms:retrieve", args=(self.lesson.pk,))
#         response = self.client.get(url)
#         data = response.json()
#         self.assertEqual(self.lesson.owner, self.user)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data.get("title"), self.lesson.title)
#
#     def test_lesson_create(self):
#         url = reverse("lms:new")
#         data = {
#             "title": "test_lesson",
#             "video_link": "https://www.youtube.com/testlesson/",
#             "course": self.course.pk,
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Lesson.objects.all().count(), 2)
#
#     def test_lesson_create_invalid_link(self):
#         url = reverse("lms:new")
#         data = {
#             "title": "test_lesson",
#             "video_link": "https://www.vkvideo.com/testlesson/",
#             "course": self.course.pk,
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#         # Проверяем сообщение об ошибке без URL
#         error_message = response.json().get("video_link", [])
#         self.assertEqual(len(error_message), 1)
#         self.assertEqual(
#             error_message[0].split(":")[0],
#             "Ссылка на сторонний ресурс обнаружена в поле video_link",
#         )
#
#     def test_lesson_update(self):
#         url = reverse("lms:edit", args=(self.lesson.pk,))
#         data = {"title": "test_lesson1"}
#         response = self.client.patch(url, data)
#         data = response.json()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data.get("title"), "test_lesson1")
#
#     def test_lesson_delete(self):
#         url = reverse("lms:delete", args=(self.lesson.pk,))
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Lesson.objects.all().count(), 0)
#
#     def test_lesson_list(self):
#         response = self.client.get(reverse("lms:lessons_list"))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         # Проверяем структуру ответа
#         data = response.json()
#
#         # Проверяем, что ответ может быть либо словарём (с пагинацией), либо списком (без пагинации)
#         if isinstance(data, dict):
#             # Проверяем наличие ключа 'results'
#             self.assertIn("results", data)
#
#             # Проверяем, что results содержит список уроков
#             self.assertIsInstance(data["results"], list)
#             self.assertEqual(len(data["results"]), 1)
#
#             # Проверяем данные первого урока
#             lesson_data = data["results"][0]
#             self.assertEqual(lesson_data["title"], self.lesson.title)
#         else:
#             # Если ответ - список (без пагинации)
#             self.assertIsInstance(data, list)
#             self.assertEqual(len(data), 1)
#             self.assertEqual(data[0]["title"], self.lesson.title)
#
# @override_settings(DEBUG=True)
# class CourseTestCase(APITestCase):
#     def setUp(self):
#         User = get_user_model()
#         self.user = User.objects.create(
#             email="admin@example.com", is_staff=True, is_superuser=True, is_active=True
#         )
#         self.course = Course.objects.create(
#             title="Алгебра", owner=self.user, description="Курс по алгебре"
#         )
#         self.lesson = Lesson.objects.create(
#             course=self.course,
#             title="Первый урок",
#             owner=self.user,
#             description="Самый первый урок",
#         )
#         self.client.force_authenticate(user=self.user)
#
#     def test_course_retrieve(self):
#         url = reverse("lms:course-detail", args=(self.course.pk,))
#         response = self.client.get(url)
#         data = response.json()
#         # print(data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data["title"], self.course.title)
#         self.assertEqual(data["description"], self.course.description)
#         self.assertEqual(data["is_subscribed"], False)
#
#     def test_course_create(self):
#         url = reverse("lms:course-list")
#         data = {
#             "title": "test",
#             "owner": self.user.pk,
#             "description": "Тестовый курс",
#         }
#         response = self.client.post(url, data)
#         # print(response.json())
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Lesson.objects.all().count(), 1)
#
#     def test_course_update(self):
#         url = reverse("lms:course-detail", args=(self.course.pk,))
#         data = {
#             "title": "test_update",
#             "description": "Тестовый курс",
#         }
#         response = self.client.patch(url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data.get("title"), "test_update")
#         self.assertEqual(Course.objects.get(pk=self.course.pk).title, "test_update")
#
#     # def test_course_delete(self):
#     #     url = reverse("lms:course-detail", args=(self.course.pk,))
#     #
#     #     response = self.client.delete(url)
#     #     print(response.json())
#     #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#     #     self.assertEqual(Course.objects.all().count(), 0)
#
#     def test_course_list(self):
#         url = reverse("lms:course-list")
#         response = self.client.get(url)
#         data = response.json()
#
#         # Проверяем статус код
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         # Проверяем структуру ответа
#         if isinstance(data, dict):
#             # Пагинированный ответ
#             self.assertIn("results", data)
#             self.assertEqual(data["count"], 1)
#             self.assertIsNone(data["next"])
#             self.assertIsNone(data["previous"])
#             courses = data["results"]
#         else:
#             # Непагинированный ответ (просто список)
#             courses = data
#
#         # Проверяем количество курсов
#         self.assertEqual(len(courses), 1)
#
#         # Проверяем данные курса
#         course_data = courses[0]
#         self.assertEqual(course_data["title"], self.course.title)
#         self.assertEqual(course_data["description"], self.course.description)
#         self.assertEqual(course_data.get("is_subscribed", False), False)
#         self.assertEqual(course_data.get("count_of_lessons", 1), 1)
#
#         # Проверяем данные урока, если они есть в ответе
#         if "lessons_info" in course_data:
#             self.assertEqual(len(course_data["lessons_info"]), 1)
#             lesson_data = course_data["lessons_info"][0]
#             self.assertEqual(lesson_data["title"], self.lesson.title)
#             self.assertEqual(lesson_data["description"], self.lesson.description)
#
# @override_settings(DEBUG=True)
# class CourseSubscriptionTests(APITestCase):
#     def setUp(self):
#         User = get_user_model()
#         self.user = User.objects.create(
#             email="admin@example.com", is_staff=True, is_superuser=True, is_active=True
#         )
#         self.course = Course.objects.create(
#             title="Test Course", description="Test Description"
#         )
#         self.subscribe_url = reverse(
#             "lms:subscribe_to_course", kwargs={"pk": self.course.pk}
#         )
#         self.unsubscribe_url = reverse(
#             "lms:unsubscribe_from_course", kwargs={"pk": self.course.pk}
#         )
#
#     def test_subscribe_to_course_authenticated(self):
#         """Тест успешной подписки на курс"""
#         self.client.force_authenticate(user=self.user)
#         response = self.client.post(self.subscribe_url)
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(
#             response.data["message"], "Вы успешно подписались на обновления курса."
#         )
#         self.assertTrue(
#             CourseSubscription.objects.filter(
#                 user=self.user, course=self.course
#             ).exists()
#         )
#
#     def test_subscribe_to_course_unauthenticated(self):
#         """Тест попытки подписки без аутентификации"""
#         response = self.client.post(self.subscribe_url)
#
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#     def test_subscribe_to_course_already_subscribed(self):
#         """Тест попытки повторной подписки на курс"""
#         CourseSubscription.objects.create(user=self.user, course=self.course)
#         self.client.force_authenticate(user=self.user)
#         response = self.client.post(self.subscribe_url)
#
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(
#             response.data["message"], "Вы уже подписаны на обновления этого курса."
#         )
#
#     def test_subscribe_to_nonexistent_course(self):
#         """Тест попытки подписки на несуществующий курс"""
#         invalid_url = reverse("lms:subscribe_to_course", kwargs={"pk": 999})
#         self.client.force_authenticate(user=self.user)
#         response = self.client.post(invalid_url)
#
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_unsubscribe_from_course_authenticated(self):
#         """Тест успешной отписки от курса"""
#         CourseSubscription.objects.create(user=self.user, course=self.course)
#         self.client.force_authenticate(user=self.user)
#         response = self.client.delete(self.unsubscribe_url)
#
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(
#             CourseSubscription.objects.filter(
#                 user=self.user, course=self.course
#             ).exists()
#         )
#
#     def test_unsubscribe_from_course_unauthenticated(self):
#         """Тест попытки отписки без аутентификации"""
#         response = self.client.delete(self.unsubscribe_url)
#
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#
#     def test_unsubscribe_from_course_not_subscribed(self):
#         """Тест попытки отписки от курса, на который не подписан"""
#         self.client.force_authenticate(user=self.user)
#         response = self.client.delete(self.unsubscribe_url)
#
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(
#             response.data["message"], "Вы не подписаны на обновления этого курса."
#         )
#
#     def test_unsubscribe_from_nonexistent_course(self):
#         """Тест попытки отписки от несуществующего курса"""
#         invalid_url = reverse("lms:unsubscribe_from_course", kwargs={"pk": 999})
#         self.client.force_authenticate(user=self.user)
#         response = self.client.delete(invalid_url)
#
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
