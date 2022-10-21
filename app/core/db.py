from functools import lru_cache
from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient
from ..settings import AppSettings, get_app_settings

settings = get_app_settings()

@lru_cache
def init_mongo_engine() -> AIOEngine:

    dbname: str = settings.MONGODB_DB
    host: str = settings.MONGODB_HOST
    port: int = settings.MONGODB_PORT
    
    motor_client: AsyncIOMotorClient = AsyncIOMotorClient(host=host, port=port)

    return AIOEngine(client=motor_client, database=dbname)
