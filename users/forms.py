
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'foto']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
