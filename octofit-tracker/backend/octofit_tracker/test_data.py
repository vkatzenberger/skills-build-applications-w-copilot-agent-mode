from bson import ObjectId

test_data = {
    "users": [
        {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
        {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
        {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
        {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
    ],
    "teams": [
        {"_id": ObjectId(), "name": "Blue Team"},
        {"_id": ObjectId(), "name": "Gold Team"},
    ],
    "activities": [
        {"_id": ObjectId(), "user": "thundergod", "activity_type": "Cycling", "duration": "01:00:00"},
        {"_id": ObjectId(), "user": "metalgeek", "activity_type": "Crossfit", "duration": "02:00:00"},
        {"_id": ObjectId(), "user": "zerocool", "activity_type": "Running", "duration": "01:30:00"},
        {"_id": ObjectId(), "user": "crashoverride", "activity_type": "Strength", "duration": "00:30:00"},
        {"_id": ObjectId(), "user": "sleeptoken", "activity_type": "Swimming", "duration": "01:15:00"},
    ],
    "leaderboard": [
        {"_id": ObjectId(), "user": "thundergod", "score": 100},
        {"_id": ObjectId(), "user": "metalgeek", "score": 90},
        {"_id": ObjectId(), "user": "zerocool", "score": 95},
        {"_id": ObjectId(), "user": "crashoverride", "score": 85},
        {"_id": ObjectId(), "user": "sleeptoken", "score": 80},
    ],
    "workouts": [
        {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
        {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
        {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
        {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
        {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
    ],
}
