from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :

#Render HTML template index.html
    return render( request, 'workout_app/index.html')
