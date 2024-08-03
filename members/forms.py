from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    grade = forms.ChoiceField(choices=CustomUser.GRADE_CHOICES, required=False)
    status = forms.ChoiceField(choices=CustomUser.STATUS_CHOICES, required=True)
    financial_situation = forms.ChoiceField(choices=CustomUser.NEED_MERIT_CHOICES, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email', 'grade', 'major', 'college', 'financial_situation', 'status']
        widgets = {
            'major': forms.TextInput(attrs={'placeholder': 'Enter your major or desired major', 'style': 'width: 200px;'}),
            'college': forms.TextInput(attrs={'placeholder': 'Enter your college or desired college', 'style': 'width: 200px;'}),
        }

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)