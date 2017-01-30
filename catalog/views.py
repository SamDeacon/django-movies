from django.shortcuts import render
from .models import Movie, Director, Actor, Genre

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_movies=Movie.objects.all().count()
    num_directors=Director.objects.count()  # The 'all()' is implied by default.
    num_actors=Actor.objects.count()  # The 'all()' is implied by default.
    num_genres=Genre.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_movies':num_movies,'num_directors':num_directors, 'num_actors':num_actors, 'num_genres':num_genres  },
    )
