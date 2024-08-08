from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ForeignKey, CASCADE, IntegerField, TextField
from django.forms import ChoiceField

from apps import users
from apps.shared.models import BaseModel


class Review(BaseModel):
    product = ForeignKey('product.Product', CASCADE, related_name='reviews')
    user = ForeignKey('users.User', CASCADE, related_name='reviews')
    rating = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = TextField(blank=True, default='No comment')
