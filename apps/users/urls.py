from django.urls import path

from apps.users.views import ContactView, SubscribersView

app_name = 'users'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path("subscribe-request/", SubscribersView.as_view(), name="subscribe-request"),
]
