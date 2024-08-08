from apps.users.forms import SubscribersForm


def subscribe_form(request):
    return {'subscribe_form': SubscribersForm()}
