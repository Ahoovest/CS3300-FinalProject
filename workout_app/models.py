from django.db import models
from django.urls import reverse

class User(models.Model):
    email = models.EmailField('Email Address', unique=True)
    username = models.CharField('Username', max_length=200, unique=True)
    contact_email = models.EmailField('Contact Email', blank=True)
    # pfp = models.ImageField(upload_to='profile_pics/', blank=True)
    plan = models.OneToOneField('Plan', on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

class Plan(models.Model):
    title = models.CharField(max_length=200, default='Title')
    is_active = models.BooleanField(default=False) 
    about = models.TextField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('plan-detail', args=[str(self.id)])


class Workout(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('workout-detail', args=[str(self.id)])
