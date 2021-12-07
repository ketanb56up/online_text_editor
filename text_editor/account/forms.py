from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserForms(UserCreationForm):
    """
    UserForms
        Using User creation form and User model creating a form class
        for validating all the input values from backend side.
    """
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Enter your first name'
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Enter your last name'
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Enter a valid email address'
    )
    contact = forms.IntegerField(
        required=True,
        help_text='Enter a valid contact number'
    )
    user_agent = forms.CharField(
        max_length=50,
        required=True,
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'contact',
            'email',
            'user_agent',
            'password1',
            'password2',
        ]
