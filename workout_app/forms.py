from django import forms
from .models import Plan, Workout

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['title', 'about', 'is_active']

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'description']
