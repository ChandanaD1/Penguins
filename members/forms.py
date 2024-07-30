from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    grade = forms.ChoiceField(choices=CustomUser.GRADE_CHOICES, required=False)
    mentor_or_mentee = forms.ChoiceField(choices=CustomUser.MENTOR_MENTEE_CHOICES, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'grade', 'major', 'financial_situation', 'mentor_or_mentee', 'username', 'password1', 'password2']

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)