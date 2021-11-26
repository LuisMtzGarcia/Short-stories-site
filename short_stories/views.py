from django.shortcuts import render

from .models import Story, Genre

def index(request):
    """The home page for Short Stories, displays all available genres."""
    genres = Genre.objects.order_by('date_added')
    context = {'genres': genres}
    return render(request, 'short_stories/index.html', context)

def stories(request):
    """Shows all stories."""
    stories = Story.objects.order_by('-date_added')
    context = {'stories': stories}
    return render(request, 'short_stories/cuentos.html', context)

def story(request, story_id):
    """Shows a single story."""
    story = Story.objects.get(id=story_id)
    context = {'story': story}
    return render(request, 'short_stories/cuento.html', context)

def genres(request):
    """Shows all genres."""
    genres = Genre.objects.order_by('date_added')
    context = {'genres': genres}
    return render(request, 'short_stories/generos.html', context)

def genre(request, genre_id):
    """Shows a single genre and the stories related to it."""
    genre = Genre.objects.get(id=genre_id)
    stories = genre.story_set.order_by('-date_added')
    context = {'genre': genre, 'stories': stories}
    return render(request, 'short_stories/genero.html', context)