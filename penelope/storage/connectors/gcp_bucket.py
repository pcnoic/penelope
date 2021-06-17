import logging
import os
from google.cloud import storage

def get_g_client():
    storage_client = storage.Client()
    return storage_client
