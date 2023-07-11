from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView


# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    
#...
class About(TemplateView):
    template_name = "about.html"

 #adds artist class for mock database data
class Workout:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


workouts = [
  Workout("Lat Pulldown", "https://i.imgur.com/G4oYdPp.jpg", "The lat pulldown is a popular exercise that targets the muscles in the back and helps to improve upper body strength and posture."),
  Workout("Bench Press", "https://i.imgur.com/zYy7CFJ.jpg", "The bench press is a widely used exercise that primarily targets the muscles in the chest, shoulders, and triceps. It is effective for building upper body strength and developing a well-rounded physique."),
  Workout("Deadlift", "https://i.imgur.com/WyMiH8S.jpg", "The deadlift is a powerful compound exercise that engages multiple muscle groups, including the back, glutes, hamstrings, and core. It is known for building overall strength and promoting functional movement patterns."),
]

class WorkoutList(TemplateView):
    template_name = "workout_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["workouts"] = workouts # this is where we add the key into our context object for the view to use
        return context
