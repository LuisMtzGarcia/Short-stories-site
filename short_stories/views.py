from django.shortcuts import render

from .models import Story

def index(request):
    """The home page for Short Stories."""
    return render(request, 'short_stories/index.html')

def stories(request):
    """Show all stories."""
    stories = Story.objects.order_by('-date_added')
    context = {'stories': stories}
    return render(request, 'short_stories/cuentos.html', context)

def story(request, story_id):
    """Shows a single story."""
    story = Story.objects.get(id=story_id)
    context = {'story': story}
    return render(request, 'short_stories/cuento.html', context)
