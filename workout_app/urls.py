from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),  # URL for user registration

    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # URL for password reset
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # URL for password reset done
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # URL for password reset confirm
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # URL for password reset complete
    path('plan/list/', views.plan_list, name='plan_list'),
    path('plan/add/', views.add_plan, name='add_plan'),
    path('plan/<int:pk>/', views.plan_detail, name='plan_detail'),
    path('plan/<int:pk>/add_workout/', views.add_workout, name='add_workout'),
    path('plan/<int:pk>/edit/', views.edit_plan, name='edit_plan'),  # New URL pattern for editing plans
    path('workout/<int:pk>/delete/', views.delete_workout, name='delete_workout'),
    path('workout/<int:pk>/edit/', views.edit_workout, name='edit_workout'),  # New URL pattern for editing workouts
    path('workout/<int:pk>/', views.workout_detail, name='workout_detail'),
]
