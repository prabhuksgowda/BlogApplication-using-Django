from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password1','password2')

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=100)
    last_login = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class': 'form checker'}))    

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','last_login',)


class PasswordChangeingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100)
    new_password1 = forms.CharField(max_length=100)
    new_password2 = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')