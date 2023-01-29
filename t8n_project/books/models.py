from django.db import models
from django_jsonform.models.fields import JSONField
from .utils import SCHEMA


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Book(TimestampedModel):
    BOOK_TYPES = (("PAPERBACK", "Paperback"), 
                    ("HANDMADE", "Handmade"),
                    ("HARDCOVER", "Hardcover"))

    title = JSONField(schema=SCHEMA)
    book_type = models.CharField(max_length=20,
                                choices=BOOK_TYPES,
                                default="PAPERBACK")