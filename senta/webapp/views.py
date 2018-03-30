from django.shortcuts import render 
from . import fetch


def index(request):
    return render(request, 'index.html', {})

def print_tweets(request):
    fetched_tweets = fetch.fetch_tweets()
    return HttpResponse(fetched_tweets)