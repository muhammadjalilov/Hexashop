from django.db import models
from django.db.models import Model, DateTimeField
from django.utils import timezone


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=timezone.now())
    updated_at = DateTimeField(auto_now=timezone.now())

    class Meta:
        abstract = True
