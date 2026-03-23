from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Add additional fields if needed

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField('User', related_name='teams')

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    points = models.IntegerField()
    date = models.DateField(auto_now_add=True)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField('User', related_name='suggested_workouts')

class Leaderboard(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    month = models.CharField(max_length=20)
