from djongo import models


from djongo.models import ObjectIdField

class Team(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    def __str__(self):
        return self.name

class Activity(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    def __str__(self):
        return f"{self.user.name} - {self.type}"

class Workout(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    description = models.CharField(max_length=200)
    duration = models.IntegerField()  # in minutes
    def __str__(self):
        return f"{self.user.name} - {self.description}"

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team.name} - {self.points}"
