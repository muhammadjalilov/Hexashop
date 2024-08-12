from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, EmailInput, TextInput, Textarea, CharField, PasswordInput

from apps.users.models import Subscribers, Feedbacks


class SubscribersForm(ModelForm):
    class Meta:
        model = Subscribers
        fields = '__all__'
        widgets = {
            'fullname': TextInput(attrs={'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'placeholder': 'Your Email Address'})
        }


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedbacks
        fields = '__all__'
        widgets = {
            'fullname': TextInput(attrs={'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'placeholder': 'Your Email Address'}),
            'feedback': Textarea(attrs={'placeholder': 'Your Massage'})
        }


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Username', widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = CharField(label='Username', widget=TextInput(attrs={'class': 'form-control'}))
    email = CharField(label='Email', widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(label='ConfirmPassword', widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Firstname',
            'last_name': 'Lastname'
        }
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError('This email already existed!')
        return email
