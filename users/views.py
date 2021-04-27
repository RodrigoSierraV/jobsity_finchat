from django.contrib.auth.views import LogoutView, LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy


class UsersSignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


class UsersLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = AuthenticationForm
    success_url = 'chatrooms:list_rooms'
