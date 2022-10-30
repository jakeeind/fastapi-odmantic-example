from functools import lru_cache
from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
from ..settings import AppSettings, get_app_settings

settings = get_app_settings()
engine: AIOEngine = AIOEngine()

def init_mongo_engine():
    global engine
    dbname: str = settings.MONGODB_DB
    host: str = settings.MONGODB_HOST
    port: int = settings.MONGODB_PORT
    
    motor_client: AsyncIOMotorClient = AsyncIOMotorClient(host=host, port=port)


    engine = AIOEngine(client=motor_client, database=dbname)

