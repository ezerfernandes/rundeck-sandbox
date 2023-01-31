import logging
import os

import requests
# import module for getting env variable from .env
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)
load_dotenv('.env')

API_TOKEN = os.getenv('API_TOKEN')
LOG_FILENAME = os.getenv('LOG_FILENAME')
HOSTNAME = os.getenv('HOSTNAME')
PORT = os.getenv('PORT')
API_VERSION = os.getenv('API_VERSION', '41')
BASE_URL = f'http://{HOSTNAME}:{PORT}'
API_URL = f'{BASE_URL}/api/{API_VERSION}'

headers = {
    'X-Rundeck-Auth-Token': API_TOKEN,
    'Accept': 'application/json',
}

def get_system_info():
    response = requests.get(
        f'{API_URL}/system/info',
        headers=headers,
        timeout=10,
        )
    return response.json()


def list_projects():
    response = requests.get(
        f'{API_URL}/projects',
        headers=headers,
        timeout=10,
        )
    return response.json()

if __name__ == "__main__":
    logging.info(get_system_info())
    logging.info(list_projects())
