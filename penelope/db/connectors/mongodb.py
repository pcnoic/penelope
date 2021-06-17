from pymongo import MongoClient
## pprint for beautiful printing
from config import ConfigParams


def get_db_connection():
    db_host = ConfigParams.INGEST_DB_HOST
    db_port = ConfigParams.INGEST_DB_PORT
    db_name = ConfigParams.INGEST_DB_NAME
    
    client = MongoClient(db_host, db_port)
    db = client[db_name]

    return db    
