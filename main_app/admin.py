from django.contrib import admin
from .models import Workout, Set # import the Workout model from models.py
# Register your models here.

admin.site.register(Workout) # this line will add the model to the admin panel
admin.site.register(Set)