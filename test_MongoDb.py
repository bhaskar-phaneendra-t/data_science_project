from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

username = quote_plus("bhaskarphaneendrat_db_user")
password = quote_plus("Admin@5")

url = f"mongodb+srv://{username}:{password}@cluster0.3axkdkw.mongodb.net/?appName=Cluster0"
print(url)
client = MongoClient(url, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
