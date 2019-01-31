from django import forms
from django.contrib.auth import authenticate
class LoginForm(forms.Form):
    username=forms.CharField(max_length=15)
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user=self.cleaned_data.get("username")
        passw=self.cleaned_data.get("password")
        usern=authenticate(username=user,password=passw)
        if usern is None:
            raise forms.ValidationError("wrong credentials")