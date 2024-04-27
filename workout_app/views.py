from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Plan, Workout
from .forms import PlanForm, WorkoutForm
from .forms import RegistrationForm

def index(request):
    return render(request, 'workout_app/index.html')

def menu(request):
    return render(request, 'workout_app/menu.html')


def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'workout_app/plan_list.html', {'plans': plans})

@login_required
def add_plan(request):
    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plan_list')
    else:
        form = PlanForm()
    return render(request, 'workout_app/add_plan.html', {'form': form})

def plan_detail(request, pk):
    plan = Plan.objects.get(pk=pk)
    return render(request, 'workout_app/plan_detail.html', {'plan': plan})

@login_required
def add_workout(request, pk):
    plan = Plan.objects.get(pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.plan = plan
            workout.save()
            return redirect('plan_detail', pk=pk)
    else:
        form = WorkoutForm()
    return render(request, 'workout_app/add_workout.html', {'form': form, 'plan': plan})

@login_required
def delete_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('plan_list')  # Redirect to the plan list page or wherever appropriate
    return render(request, 'workout_app/delete_workout.html', {'workout': workout})

@login_required
def edit_plan(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'POST':
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('plan_detail', pk=pk)
    else:
        form = PlanForm(instance=plan)
    return render(request, 'workout_app/edit_plan.html', {'form': form, 'plan': plan})

@login_required
def edit_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('plan_detail', pk=workout.plan.pk)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workout_app/edit_workout.html', {'form': form, 'workout': workout})

def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workout_app/workout_detail.html', {'workout': workout})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to index page after registration
    else:
        form = UserCreationForm()
    return render(request, 'workout_app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to index page
        else:
            return render(request, 'workout_app/login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'workout_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')
