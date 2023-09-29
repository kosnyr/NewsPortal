from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SingUpForm


class SignUp(CreateView):
    model = User
    form_class = SingUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

