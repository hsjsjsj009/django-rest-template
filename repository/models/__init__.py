from django.db import models


class Example(models.Model):
    integer_field = models.IntegerField()
    text_field = models.TextField()
