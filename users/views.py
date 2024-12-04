from django.contrib.auth.views import LoginView as BaseLoginView
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm


class RegisterView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:log')


class LoginView(BaseLoginView):
    template_name = 'login.html'
    authentication_form = LoginForm
    next_page = reverse_lazy('applications:index')
