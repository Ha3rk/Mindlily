import requests
import os
import logging
import re
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Spending
from requests.auth import HTTPBasicAuth
from django.http import JsonResponse
from .yapily_service import get_access_token, get_user_accounts
from dotenv import load_dotenv



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



load_dotenv() 


BASE_URL = "https://auth.yapily.com"
YAPILY_ID = os.getenv('CLIENT_ID', 'default-secret-key')
YAPILY_SECRET_KEY = os.getenv('CLIENT_SECRET', 'default-secret-key')


def spending_list(request):
    spending_app = Spending.objects.all()
    return render(request, 'index.html', {'spending_app': spending_app})
def base(request):
    return render(request, 'base.html', {'base': base})
def about(request):
    return render(request, 'about.html', {'about': about})




def user_accounts_view(request):
    try:
        access_token = get_access_token()
        accounts = get_user_accounts(access_token)
        return JsonResponse(accounts, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)