from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def start(request):
    return HttpResponse('Welcome to my main page!')