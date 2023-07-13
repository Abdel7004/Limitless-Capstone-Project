from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), # <- new route
    path('workouts/', views.WorkoutList.as_view(), name="workout_list"),
    path('workouts/new/', views.WorkoutCreate.as_view(), name="workout_create"),
    path('workouts/<int:pk>/', views.WorkoutDetail.as_view(), name="workout_detail"),
    path('workouts/<int:pk>/update',views.WorkoutUpdate.as_view(), name="workout_update"),
    path('workouts/<int:pk>/delete',views.WorkoutDelete.as_view(), name="workout_delete"),
    path('workouts/<int:pk>/sets/new/', views.SetCreate.as_view(), name="set_create"),
    path('routines/<int:pk>/sets/<int:set_pk>/', views.RoutineSetAssoc.as_view(), name="routine_set_assoc"),
]