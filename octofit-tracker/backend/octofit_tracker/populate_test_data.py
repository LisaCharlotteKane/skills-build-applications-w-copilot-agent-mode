from pymongo import MongoClient
from bson import ObjectId
from datetime import timedelta

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Drop existing collections
for col in ['users', 'teams', 'activity', 'leaderboard', 'workouts']:
    db[col].drop()

# Insert users
test_users = [
    {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
    {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
]
user_ids = db.users.insert_many(test_users).inserted_ids

# Insert teams
blue_team = {"_id": ObjectId(), "name": "Blue Team", "members": user_ids[:3]}
gold_team = {"_id": ObjectId(), "name": "Gold Team", "members": user_ids[3:]}
db.teams.insert_many([blue_team, gold_team])

# Insert activities
activities = [
    {"_id": ObjectId(), "user": user_ids[0], "activity_type": "Cycling", "duration": 60*60},
    {"_id": ObjectId(), "user": user_ids[1], "activity_type": "Crossfit", "duration": 2*60*60},
    {"_id": ObjectId(), "user": user_ids[2], "activity_type": "Running", "duration": 90*60},
    {"_id": ObjectId(), "user": user_ids[3], "activity_type": "Strength", "duration": 30*60},
    {"_id": ObjectId(), "user": user_ids[4], "activity_type": "Swimming", "duration": 75*60},
]
db.activity.insert_many(activities)

# Insert leaderboard
leaderboard = [
    {"_id": ObjectId(), "user": user_ids[0], "score": 100},
    {"_id": ObjectId(), "user": user_ids[1], "score": 90},
    {"_id": ObjectId(), "user": user_ids[2], "score": 95},
    {"_id": ObjectId(), "user": user_ids[3], "score": 85},
    {"_id": ObjectId(), "user": user_ids[4], "score": 80},
]
db.leaderboard.insert_many(leaderboard)

# Insert workouts
workouts = [
    {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
    {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
    {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
    {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
    {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
]
db.workouts.insert_many(workouts)

print("Test data successfully inserted into octofit_db.")
