from typing import List

from repository.models import Example


def create(example: Example):
    example.save()


def get_by_id(example_id: int) -> Example:
    return Example.objects.get(id=example_id)


def find_by_integer_field_below_x(x: int) -> List[Example]:
    return Example.objects.filter(integer_field__lt=x)


def get_by_integer_and_text(integer: int, text: str) -> Example:
    return Example.objects.get(integer_field=integer, text_field=text)
