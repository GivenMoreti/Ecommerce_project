from django import forms
from .models import Sell, UserProfile, Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)


class SellNowForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = "__all__"


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"

# user registrations form


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "username",
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': "Email",
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Enter password",
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Confirm password",
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# user login form.
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "username",
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': "Enter password",
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

# add a new product form.


class AddNewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price',
                  'quantity', 'image', 'category','sold_by',)
