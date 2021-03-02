from django.test import TestCase
import repository.example as example_repo
from repository.models import Example
from django.db import connection


class ExampleRepoTest(TestCase):
    def setUp(self) -> None:
        with connection.cursor() as cursor:
            cursor.execute("alter sequence repository_example_id_seq restart with 1")
        Example.objects.create(integer_field=23, text_field="sdgsdg")

    def test_example_create(self):
        data = Example(
            integer_field=1,
            text_field="asdsadad"
        )
        example_repo.create(data)
        self.assertEqual(data.id, 2)

    def test_example_get_by_id(self):
        data = example_repo.get_by_id(1)
        self.assertEqual(data.integer_field, 23)
        self.assertEqual(data.text_field, "sdgsdg")

    def test_example_find_by_integer_field_below_x(self):
        list_data = example_repo.find_by_integer_field_below_x(25)
        self.assertEqual(1, len(list_data))
