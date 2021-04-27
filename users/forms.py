from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class UsersSignUpForm(forms.Form):

    class Meta:
        model = Profile
        fields = (
            'username',
            'password1',
            'password2'
        )


class UsersLoginForm(forms.Form):

    class Meta:
        model = Profile
        fields = (
            'username',
            'password1'
        )
