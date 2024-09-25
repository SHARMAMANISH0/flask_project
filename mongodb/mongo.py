from pymongo import MongoClient

# Replace '<db_password>' with your actual MongoDB password
client = MongoClient("mongodb+srv://mmanishssharma2:<db_password>@cluster0.lyvb9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Access a specific database and collection
db = client.your_database_name  # replace 'your_database_name' with your actual database name
collection = db.your_collection_name  # replace 'your_collection_name' with your actual collection name

# Example: finding a document
document = collection.find_one()
print(document)

