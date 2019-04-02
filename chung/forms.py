from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUsers

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    fullname = forms.CharField(max_length=200, help_text='Required')
    username = forms.CharField(max_length=200,help_text='Required')
    sdt = forms.CharField(max_length=200,help_text='Required')
    class Meta:
        model = MyUsers
        fields = ('username', 'email', 'sdt', 'fullname')


    def clean_email(self):
        if MyUsers.objects.filter(email__iexact=self.cleaned_data['email']):
            return False
        return self.cleaned_data['email']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        existing = MyUsers.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            return True
        else:
            return self.cleaned_data['username']

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                return False
        return self.cleaned_data
