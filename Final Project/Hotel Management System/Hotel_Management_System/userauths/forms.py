from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import FileInput, ImageField, TextInput, Select
from userauths.models import User, Profile

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': '','id': "",'placeholder':"Full Name"}), max_length=100,required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': '','id': "",'placeholder':"Username"}), max_length=100,required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': '','id': "",'placeholder':"Email Address"}),required=True)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': '','id': "",'placeholder':"Phone Number"}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': "",'placeholder':"Password"}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': "",'placeholder':"Confirm Password"}),required=True)
    

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email', 'phone', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = [
            'image',
            'full_name',
            # 'email',
            'phone',
            'gender',
            'address',
            'city',
            'state',
            'country',
            'identity_type',
            'identity_image',
            'facebook',
            'twitter',
        ]

        widgets = {
            'image': FileInput(attrs={'onChange': 'loadFile(event)', 'class': 'upload'})
        }