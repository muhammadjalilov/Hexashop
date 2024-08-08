from django.urls import path

from apps.shared.views import HomeView, AboutUsView

app_name = 'shared'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("about/", AboutUsView.as_view(), name='about'),
]
