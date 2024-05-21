from django import forms

class LoginForm(forms.Form):
    nombre = forms.CharField()
    contraseña = forms.CharField(widget=forms.PasswordInput)