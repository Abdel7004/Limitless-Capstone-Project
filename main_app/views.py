from django.shortcuts import redirect
from django.views import View # <- View class to handle requests
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView
# import models
from .models import Workout, Set, Routine
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    # Here we have added the Routines as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["routines"] = Routine.objects.all()
        return context
    
#...
class About(TemplateView):
    template_name = "about.html"

class WorkoutList(TemplateView):
    template_name = "workout_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["workouts"] = Workout.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["workouts"] = Workout.objects.all()
            # default header for not searching 
            context["header"] = "Best Workouts"
        return context
    
class WorkoutCreate(CreateView):
    model = Workout
    fields = ['name', 'img', 'description']
    template_name = "workout_create.html"
    def get_success_url(self):
        return reverse('workout_detail', kwargs={'pk': self.object.pk})

class WorkoutDetail(DetailView):
    model = Workout
    template_name = "workout_detail.html"

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['name', 'img', 'description']
    template_name = "workout_update.html"
    def get_success_url(self):
        return reverse('workout_detail', kwargs={'pk': self.object.pk})

class WorkoutDelete(DeleteView):
    model = Workout
    template_name = "workout_delete_confirmation.html"
    success_url = "/workouts/"

class SetCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        rep = request.POST.get("rep")
        workout = Workout.objects.get(pk=pk)
        Set.objects.create(title=title, rep=rep, workout=workout)
        return redirect('workout_detail', pk=pk)

class RoutineSetAssoc(View):

    def get(self, request, pk, set_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the Routine by the id and
            # remove from the join table the given Set_id
            Routine.objects.get(pk=pk).sets.remove(set_pk)
        if assoc == "add":
            # get the Routine by the id and
            # add to the join table the given Set_id
            Routine.objects.get(pk=pk).sets.add(set_pk)
        return redirect('home')


class WorkoutDetail(DetailView):
    model = Workout
    template_name = "workout_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["routines"] = Routine.objects.all()
        return context

