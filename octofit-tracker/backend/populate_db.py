import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]

# Sample data for users
users = [
    {"email": "user1@example.com", "name": "User One", "age": 16},
    {"email": "user2@example.com", "name": "User Two", "age": 17},
    {"email": "user3@example.com", "name": "User Three", "age": 15},
]

# Sample data for teams
teams = [
    {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
    {"name": "Team Beta", "members": ["user3@example.com"]},
]

# Sample data for activity
activity = [
    {"user_email": "user1@example.com", "type": "running", "duration": 30},
    {"user_email": "user2@example.com", "type": "cycling", "duration": 45},
    {"user_email": "user3@example.com", "type": "swimming", "duration": 60},
]

# Sample data for leaderboard
leaderboard = [
    {"team_name": "Team Alpha", "points": 100},
    {"team_name": "Team Beta", "points": 80},
]

# Sample data for workouts
workouts = [
    {"name": "Morning Run", "description": "A quick 5km run to start the day."},
    {"name": "Evening Yoga", "description": "Relaxing yoga session."},
]

# Insert data into collections
db.users.insert_many(users)
db.teams.insert_many(teams)
db.activity.insert_many(activity)
db.leaderboard.insert_many(leaderboard)
db.workouts.insert_many(workouts)

print("Database populated with sample data.")
