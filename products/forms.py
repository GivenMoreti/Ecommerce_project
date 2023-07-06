from django import forms
from .models import Sell,UserProfile
from django.contrib.auth.forms import UserCreationForm
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


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user