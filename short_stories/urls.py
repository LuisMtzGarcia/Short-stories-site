"""Defines URL patterns for short_stories."""

from django.urls import path

from . import views

app_name = "short_stories"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all stories
    path('cuentos/', views.stories, name="stories"),
    # Page for a single story
    path('cuentos/<int:story_id>/', views.story, name="story")
]