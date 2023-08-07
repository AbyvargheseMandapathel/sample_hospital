from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomAuthenticationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'authentication_app/register.html'

    def get_success_url(self):
        return reverse_lazy('authentication_app:login')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'authentication_app/login.html'
