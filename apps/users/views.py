from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from apps.users.forms import SubscribersForm, FeedbackForm


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
        return redirect('users:contact')


class SubscribersView(View):
    def post(self, request, *args, **kwargs):
        form = SubscribersForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription successful! Thank you for subscribing.')
        next_url = request.POST.get('next', request.META.get('HTTP_REFERER', 'shared:home'))
        return redirect(next_url)
