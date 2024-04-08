from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Plan, Workout
from .forms import PlanForm, WorkoutForm

# Create your views here.
def index(request) :

#Render HTML template index.html
    return render( request, 'workout_app/index.html')

def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'workout_app/plan_list.html', {'plans': plans})

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

def delete_workout(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if request.method == 'POST':
        workout.delete()
        return redirect('plan_list')  # Redirect to the plan list page or wherever appropriate
    return render(request, 'workout_app/delete_workout.html', {'workout': workout})

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
