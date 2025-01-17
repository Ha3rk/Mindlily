import requests
import os
import logging
import re
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Spending


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def spending_list(request):
    spending_app = Spending.objects.all()
    return render(request, 'index.html', {'spending_app': spending_app})
def base(request):
    return render(request, 'base.html', {'base': base})
def about(request):
    return render(request, 'about.html', {'about': about})
