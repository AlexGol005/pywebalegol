from django.test import  TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from blog.models import Note
from django.contrib.auth.models import User

class TestNotePublicNoteListAPIView(APITestCase):
    def test_empty_list_note(self):
        path = "/note/public/"
        resp = self.client.get(path)
        self.assertEqual(
            resp.status_code, status.HTTP_200_OK
        )
        data = resp.data
        self.assertEqual(data, [])

    def test_get_public_notes(self):
        test_user=User.objects.create(
            username="test_user",
            password="123"
        )
        Note.objects.create(title="title_1", public=False, author=test_user)
        Note.objects.create(title="title_2", public=True, author=test_user)
        path = "/note/public/"
        resp = self.client.get(path)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # expected_count_public_notes =
        # data = resp.data
        # self.assertEqual(data, [])



