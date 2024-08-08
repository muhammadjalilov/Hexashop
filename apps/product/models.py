from datetime import timedelta

from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from django.db.models import CharField, TextField, FloatField, ForeignKey, CASCADE, ImageField, SlugField, \
    OneToOneField, IntegerField, DateTimeField, BooleanField, Index
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from apps.shared.models import BaseModel


class Product(BaseModel):
    name = CharField(max_length=256, verbose_name='Product Name')
    description = TextField(verbose_name='Description')
    price = FloatField(verbose_name='Price')
    category = ForeignKey('product.Category', on_delete=CASCADE, related_name='products')
    image = ImageField(upload_to='products/', verbose_name='Product Image')
    slug = SlugField(db_index=True, blank=True)
    available = BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            Index(fields=['id', 'slug']),
            Index(fields=['name']),
            Index(fields=['-created_at'])
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        unique_slug = self.slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{self.slug}-{num}'
            num += 1
        self.slug = unique_slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product:product', args=[self.slug])


class Category(BaseModel):
    name = CharField(max_length=128)
    short_description = CharField(max_length=512)
    image = ImageField(upload_to='categories/')
    slug = SlugField(db_index=True, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


def expire_date():
    return timezone.now() + timedelta(days=3)


class Discount(BaseModel):
    product = OneToOneField(Product, CASCADE)
    discount_percentage = IntegerField(validators=[MaxValueValidator(99), MinValueValidator(1)])
    start_date = DateTimeField(default=timezone.now)
    end_date = DateTimeField(default=expire_date)
