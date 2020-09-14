from django.shortcuts import render
import requests
from django.http import JsonResponse


def search(request):
    context = {
    }
    return render (request, 'home.html' ,context)

def movies(request, ):
    #if request.method == 'POST':
    key = 'e6748ec5'
    url = f"http://www.omdbapi.com/?apikey={key}&s=avengers"
    response = requests.get(url).json()

    context = {
        'resp' : response
    }
    return render (request, 'list.html' ,context)


def movie_detail(request, movie_id):
    key = 'e6748ec5'
    url = f"http://www.omdbapi.com/?apikey={key}&i={movie_id}"
    response = requests.get(url).json()

    context = {
        'movie' : response
    }
    return render (request, 'detail.html' ,context)
