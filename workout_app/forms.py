from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Plan, Workout

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['title', 'about', 'is_active']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'description']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
