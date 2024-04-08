from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('plan/list/', views.plan_list, name='plan_list'),
    path('plan/add/', views.add_plan, name='add_plan'),
    path('plan/<int:pk>/', views.plan_detail, name='plan_detail'),
    path('plan/<int:pk>/add_workout/', views.add_workout, name='add_workout'),
    path('plan/<int:pk>/edit/', views.edit_plan, name='edit_plan'),  # New URL pattern for editing plans
    path('workout/<int:pk>/delete/', views.delete_workout, name='delete_workout'),
    path('workout/<int:pk>/edit/', views.edit_workout, name='edit_workout'),  # New URL pattern for editing workouts
     path('workout/<int:pk>/', views.workout_detail, name='workout_detail'),
]
