from motor.motor_asyncio import AsyncIOMotorClient


DATABASE_URL = 'mongodb://localhost:7777'
client = AsyncIOMotorClient(DATABASE_URL)
db = client.get_database("college")

