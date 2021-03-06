from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Users

class UserRegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(
        label=("User Type"),
        choices=Users.USER_TYPE_CHOICE)

    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
        }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',

        }),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )


    class Meta:
        model = Users
        fields = ("username", "first_name", "last_name", "email", "country", "city", "address", "phone")
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label="Username",
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={
                                   "class": "form-control",
                                   "autocomplete": "new-password"
                               }))
