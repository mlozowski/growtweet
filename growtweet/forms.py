
from django import forms
from django.contrib.auth.forms import UsernameField


class TwitterUserForm(forms.Form):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    password = forms.CharField(
        strip=True,
        widget=forms.PasswordInput,
    )
