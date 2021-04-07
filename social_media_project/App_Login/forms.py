from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm as BaseAuthenticationForm
from App_Login.models import UserProfile


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': "Your Email"}))
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': "Your Username"}))
    password1 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        required=True,
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomAuthenticationForm(BaseAuthenticationForm):
    username = forms.CharField(max_length=254, label="",
                               widget=forms.TextInput(attrs={'placeholder': "Enter Username"}), required=True)
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
                               required=True)

    class Meta:
        model = User
        fields = ["username", "password"]


class EditProfile(forms.ModelForm):
    full_name = forms.CharField(max_length=254, label="",
                                widget=forms.TextInput(attrs={'placeholder': "Enter Fullname"}), required=True)
    website = forms.CharField(max_length=254, label="",
                              widget=forms.URLInput(attrs={'placeholder': "Website URL"}), required=True)
    facebook = forms.CharField(max_length=254, label="",
                               widget=forms.URLInput(attrs={'placeholder': "Facebook URL"}), required=True)
    description = forms.CharField(max_length=254, label="",
                                  widget=forms.Textarea(attrs={'placeholder': "Your Description"}), required=True)
    dob = forms.DateField(label="", widget=forms.TextInput(attrs={'type': 'date', 'placeholder': 'Your DOB'}))
    profile_pic = forms.ImageField(label="", required=True)

    class Meta:
        model = UserProfile
        exclude = ('user',)
        fields = ('profile_pic', 'full_name', 'dob', 'description', 'website', 'facebook')
