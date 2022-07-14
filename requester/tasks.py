from celery import shared_task
import requests
from requests.exceptions import ConnectionError, Timeout


@shared_task
def request_task(url):
    try:
        response = requests.get(url, timeout=(3, 5))
        return response.status_code
    except (ConnectionError, Timeout):
        return 0
