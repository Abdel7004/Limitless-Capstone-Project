from django.db import models

# Create your models here.
class Workout(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

# below Artist Model

class Set(models.Model):

    title = models.CharField(max_length=150)
    rep = models.CharField(max_length=150)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="workouts")

    def __str__(self):
        return self.title

class Routine(models.Model):

    title = models.CharField(max_length=150)
    # this is going to create the many to many relationship and join table
    sets = models.ManyToManyField(Set)

    def __str__(self):
        return self.title
