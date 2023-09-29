from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Main page')
    return HttpResponse("Main page")

def about(request):
    logger.info("Page About us")
    return HttpResponse("Some info about us to be here soon")

def hello(request):
    logger.info("Hello page")
    return HttpResponse('Hello stranger!')