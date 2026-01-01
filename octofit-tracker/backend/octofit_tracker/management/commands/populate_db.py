from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from djongo import models

# Define models for test data (if not already defined in models.py)
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data in correct order to avoid FK issues
        # Use Djongo's raw collection access to clear collections
        from django.db import connection
        db = connection.cursor().db_conn.client[connection.settings_dict['NAME']]
        db['octofit_tracker_activity'].delete_many({})
        db['octofit_tracker_workout'].delete_many({})
        db['octofit_tracker_leaderboard'].delete_many({})
        db['octofit_tracker_user'].delete_many({})
        db['octofit_tracker_team'].delete_many({})

        # Create teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create users
        ironman = app_models.User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        captain = app_models.User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel)
        batman = app_models.User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = app_models.User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        # Create activities
        app_models.Activity.objects.create(user=ironman, type='run', duration=30)
        app_models.Activity.objects.create(user=captain, type='cycle', duration=45)
        app_models.Activity.objects.create(user=batman, type='swim', duration=60)
        app_models.Activity.objects.create(user=superman, type='run', duration=50)

        # Create workouts
        app_models.Workout.objects.create(user=ironman, description='Chest day', duration=60)
        app_models.Workout.objects.create(user=batman, description='Leg day', duration=70)

        # Create leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=100)
        app_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
