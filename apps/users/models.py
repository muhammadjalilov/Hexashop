from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db.models import CharField, EmailField, OneToOneField, CASCADE, ImageField, TextField
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

