from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ["username", "email", "first_name", "last_name", "weight", "height", "birthDate"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user_instance = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data.get('first_name', ''),
            last_name=self.cleaned_data.get('last_name', '')
        )
        user.user = user_instance
        if commit:
            user_instance.save()
            user.save()
        return user
