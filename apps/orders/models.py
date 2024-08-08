from django.core.validators import MinValueValidator
from django.db.models import ForeignKey, CASCADE, BigIntegerField, DecimalField

from apps import users
from apps.shared.models import BaseModel


class Order(BaseModel):
    user = ForeignKey('users.User', on_delete=CASCADE, related_name='orders')
    total_amount = BigIntegerField()


class OrderItem(BaseModel):
    order = ForeignKey(Order, CASCADE, related_name='order_items')
    product = ForeignKey('product.Product', CASCADE, related_name='order_items', verbose_name='Product')
    quantity = BigIntegerField(validators=[MinValueValidator(0)], verbose_name='Quantity')
    price = DecimalField(max_digits=10, decimal_places=2)
