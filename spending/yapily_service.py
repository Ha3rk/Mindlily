from django.conf import settings
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://auth.yapily.com/"
CLIENT_ID = settings.YAPILY_ID
CLIENT_SECRET = settings.YAPILY_SECRET_KEY

def get_access_token():
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    url = f"{BASE_URL}/auth/token"
    response = requests.post(url, auth=auth)
    response.raise_for_status()
    return response.json().get("access_token")

def get_user_accounts(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"{BASE_URL}/users/me/accounts"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
