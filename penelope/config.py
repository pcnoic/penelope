from helpers import get_from_environment

class ConfigParams:
    INGEST_DB_HOST = get_from_environment('INGEST_DB_HOST')
    INGEST_DB_NAME = get_from_environment('INGEST_DB_NAME')
    INGEST_DB_USER = get_from_environment('INGEST_DB_USER')
    INGEST_DB_PWD = get_from_environment('INGEST_DB_PWD')
    INGEST_DB_PORT = get_from_environment('INGEST_DB_PORT')
    INGEST_DB_ENTITY = get_from_environment('INGEST_DB_ENTITY')
    RAW_DATA_STORAGE_BUCKET = get_from_environment('RAW_DATA_STORAGE_BUCEKET')
    TRNSL_DATA_STORAGE_BUCKET = get_from_environment('TRNSL_DATA_STORAGE_BUCKET')
