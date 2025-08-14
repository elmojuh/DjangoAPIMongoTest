from pymongo import MongoClient

def get_db():
    client = MongoClient(
        host='test_mongodb',
        port=27017,
        username='root',
        password='pass',
        authSource="admin"
    )
    return client["animal_db"]