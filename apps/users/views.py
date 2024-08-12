from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from apps.users.forms import SubscribersForm, FeedbackForm, LoginUserForm, UserRegisterForm


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):
        form = FeedbackForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for feedback!')
        else:
            messages.warning(request, 'Something Wrong!')
        return redirect('users:login')


class SubscribersView(View):
    def post(self, request, *args, **kwargs):
        form = SubscribersForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription successful! Thank you for subscribing.')
        next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'shared:home'))
        return redirect(next_url)


class UserLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('shared:home')


class RegisterUserView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse_lazy('users:login')


@login_required
def logout_user(request):
    logout(request)
    return redirect('users:login')
