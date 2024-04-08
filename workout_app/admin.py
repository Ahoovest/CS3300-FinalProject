from django.contrib import admin
from .models import User, Plan, Workout

# Register your models here.
admin.site.register(User)
admin.site.register(Plan)
admin.site.register(Workout)