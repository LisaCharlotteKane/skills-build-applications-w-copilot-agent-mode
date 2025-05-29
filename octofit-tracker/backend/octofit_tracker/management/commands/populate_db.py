from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), name='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), name='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), name='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), name='crashoverride', email='crashoverride@mhigh.edu', password='crashoverridepassword'),
        ]
        db.users.insert_many([user.__dict__ for user in users])

        # Create teams
        teams = [
            Team(_id=ObjectId(), name='Team Alpha', members=[users[0]._id, users[1]._id]),
            Team(_id=ObjectId(), name='Team Beta', members=[users[2]._id, users[3]._id]),
        ]
        db.teams.insert_many([{'_id': team._id, 'name': team.name, 'members': team.members} for team in teams])

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0]._id, activity_type='run', duration=30),
            Activity(_id=ObjectId(), user=users[1]._id, activity_type='walk', duration=45),
            Activity(_id=ObjectId(), user=users[2]._id, activity_type='cycle', duration=60),
        ]
        db.activity.insert_many([{'_id': a._id, 'user': a.user, 'activity_type': a.activity_type, 'duration': a.duration} for a in activities])

        # Create leaderboard
        leaderboard = [
            Leaderboard(_id=ObjectId(), team=teams[0]._id, points=100),
            Leaderboard(_id=ObjectId(), team=teams[1]._id, points=80),
        ]
        db.leaderboard.insert_many([{'_id': l._id, 'team': l.team, 'points': l.points} for l in leaderboard])

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Pushups', description='Do 20 pushups'),
            Workout(_id=ObjectId(), name='Situps', description='Do 30 situps'),
        ]
        db.workouts.insert_many([{'_id': w._id, 'name': w.name, 'description': w.description} for w in workouts])

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
