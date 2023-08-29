from django import forms
from .models import CategoryImage,PartImages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User,AbstractUser,PermissionsMixin
from phonenumber_field.formfields import PhoneNumberField




class CatForm(forms.ModelForm):
    class Meta:
        model = CategoryImage
        fields =('name','description','image')
    








class GalleryForm(forms.ModelForm):
    class Meta:
        model = PartImages
        fields = ['name','image_file','category']





class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'email','password1', 'password2')  
    def __str__(self):
        return self.username 










class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )




