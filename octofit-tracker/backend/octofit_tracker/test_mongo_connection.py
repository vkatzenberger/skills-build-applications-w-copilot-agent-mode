from pymongo import MongoClient

# Connect to MongoDB
print("Connecting to MongoDB...")
client = MongoClient('localhost', 27017)
db = client['octofit_db']

# Insert test data
print("Inserting test data...")
db.test_collection.insert_one({"test_key": "test_value"})

# Retrieve test data
print("Retrieving test data...")
result = db.test_collection.find_one({"test_key": "test_value"})
print("Inserted and retrieved data:", result)

# Clean up
print("Cleaning up test data...")
db.test_collection.delete_one({"test_key": "test_value"})
print("Test completed.")
