from django.shortcuts import render
from . import fetch


def index(request):
    return render(request, 'index.html', {})

