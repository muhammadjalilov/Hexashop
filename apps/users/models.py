from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db.models import CharField, EmailField, OneToOneField, CASCADE, ImageField, TextField, Model, ForeignKey, \
    BooleanField, IntegerField
from django.forms import TextInput
from phonenumber_field.modelfields import PhoneNumberField
from apps.shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class User(BaseModel, AbstractUser):
    role = CharField(max_length=256, default='Customer')
    email = EmailField(unique=True, db_index=True, help_text=_("Required. Your email address."),
                       error_messages={"unique": _("A user with that email already exists")},
                       validators=[validate_email])
    address = CharField(max_length=256)
    phone = PhoneNumberField(region='UZ')
    avatar = ImageField(upload_to='users/', null=True)


class ClientDetails(Model):
    user = ForeignKey(User, CASCADE, 'client_details')
    first_name = CharField(max_length=100, verbose_name='first name', help_text=_('your first name'))
    last_name = CharField(max_length=100, verbose_name='last name', help_text=_('your last name'))
    region = CharField(max_length=100, verbose_name='region', help_text=_('region'))
    city = CharField(max_length=100, verbose_name='city', help_text=_('city'))
    street = TextField(verbose_name='street', help_text=_('street'))
    flat_number = IntegerField(null=True, blank=True, verbose_name='flat number', help_text=_('flat number'))

    def __str__(self):
        return f'client: {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'client_details'
        verbose_name = "client detail"
        verbose_name_plural = "client details"


class Services(BaseModel):
    heading = CharField(max_length=256)
    description = TextField()
    image = ImageField(upload_to='services/')


class Subscribers(BaseModel):
    fullname = CharField(max_length=256)
    email = EmailField(unique=True, db_index=True, help_text=_("Required. Your email address."),
                       error_messages={"unique": _("A user with that email already exists")},
                       validators=[validate_email])


class Feedbacks(BaseModel):
    fullname = CharField(max_length=256)
    email = EmailField(unique=True, db_index=True, help_text=_("Required. Your email address."),
                       error_messages={"unique": _("A user with that email already exists")},
                       validators=[validate_email])
    feedback = TextField()
