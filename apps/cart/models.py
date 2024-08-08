from django.db import models
from django.db.models import OneToOneField, CASCADE

from apps import users
from apps.shared.models import BaseModel


class Cart(BaseModel):
    user = OneToOneField('users.User', CASCADE)


class CartItem(BaseModel):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='cart_items')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.BigIntegerField()
