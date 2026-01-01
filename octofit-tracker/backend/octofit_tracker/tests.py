from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        self.assertEqual(str(user), 'Test User')
    def test_activity_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=10)
        self.assertEqual(str(activity), 'Test User - run')
    def test_workout_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        workout = Workout.objects.create(user=user, description='desc', duration=20)
        self.assertEqual(str(workout), 'Test User - desc')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=42)
        self.assertEqual(str(leaderboard), 'Test Team - 42')
