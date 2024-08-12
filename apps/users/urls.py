from django.urls import path

from apps.users.views import ContactView, SubscribersView, UserLoginView, logout_user, RegisterUserView

app_name = 'users'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path("subscribe-request/", SubscribersView.as_view(), name="subscribe-request"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("logout/", logout_user, name="logout"),
]
