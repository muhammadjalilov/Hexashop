from django.core.validators import MinValueValidator
from django.db.models import ForeignKey, CASCADE, BigIntegerField, DecimalField, CharField, BooleanField, Index, \
    PositiveIntegerField

from apps import users
from apps.shared.models import BaseModel


class Order(BaseModel):
    user = ForeignKey('users.User', on_delete=CASCADE, related_name='orders')
    postal_code = CharField(max_length=20)
    city = CharField(max_length=100)
    paid = BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
        indexes = [
            Index(fields=['-created_at'])
        ]

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(BaseModel):
    order = ForeignKey(Order, CASCADE, related_name='items')
    product = ForeignKey('product.Product', CASCADE, related_name='order_items', verbose_name='Product')
    quantity = PositiveIntegerField(default=1, verbose_name='Quantity')
    price = DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
