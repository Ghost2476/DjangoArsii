from django import forms
from accounts.models import CustomUser
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model  = CustomUser
        fields = ('first_name', 'last_name', 'email', 'avatar', 'bio')

class SettingsForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ('phone', 'address')
