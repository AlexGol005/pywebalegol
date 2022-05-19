from django.test import  TestCase
from django.contrib.auth.models import User


from blog.models import Note
from blog_api import filters


class TestNoteFilter(TestCase):
    @classmethod
    def setUp(cls):
        test_user_1 = User.objects.create(
            username="test_user_1",
            password="123"
        )
        test_user_2 = User.objects.create(
            username="test_user_2",
            password="123"
        )

        Note.objects.create(title="title_1", public=False, author=test_user_2)
        Note.objects.create(title="title_2", public=True, author=test_user_2)
        Note.objects.create(title="title_3", public=False, author=test_user_1)
        Note.objects.create(title="title_4", public=True, author=test_user_1)


    def test_filter_notes_by_autor_id(self):
        filter_author_id = 1
        queryset = Note.objects.all()
        expected_queryset = Note.objects.filter(author_id=filter_author_id)

        actual_queryset = filters.filter_notes_by_autor_id(
            queryset, filter_author_id
        )
        self.assertQuerysetEqual(actual_queryset, expected_queryset, ordered=False)



