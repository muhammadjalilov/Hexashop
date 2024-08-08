from django.forms import ModelForm, EmailInput, TextInput, Textarea
from django_extensions import validators

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
