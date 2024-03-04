from django.shortcuts import render
from filmapp .models import Movie

from django.db.models import Q

def search_result(request):
    movie = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        movie = Movie.objects.all().filter(Q(movie_title__icontains=query) | Q(description__icontains=query))

    return render(request, 'search.html', {'query': query, 'movie': movie})


