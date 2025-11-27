from django import forms
from .models import Expense, CustomUser
from django.contrib.auth.forms import UserCreationForm

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']