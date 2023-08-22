from pymongo import MongoClient

uri = "mongodb+srv://admin:admin123@cluster1.jvlmuka.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

# Defining the database name
db = client['reactpy_task01']

# Defining the collection name
collection = db['main']

# Checking the connection
try:
    client.admin.command("ping")
    print("Successfully connected to MongoDB")
except Exception as e:
    print(e)