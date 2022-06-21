from curses import panel
from dataclasses import Field
from django.db import models
from wagtail.admin.panels import FieldPanel

class Genre(models.Model):
    """Genre to classify the short stories or other kinds of texts."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('date_added'),
    ]

    class Meta:
        verbose_name_plural = 'genres'

    def __str__(self):
        """Return the name of the genre."""
        return self.name

class Story(models.Model):
    """The published short story."""
    title = models.CharField(max_length=200)
    genre =  models.ForeignKey(Genre, on_delete=models.CASCADE)
    synopsis = models.TextField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    cover = models.URLField(max_length=200)

    panels = [
        FieldPanel('title'),
        FieldPanel('genre'),
        FieldPanel('synopsis'),
        FieldPanel('text'),
        FieldPanel('date_added'),
        FieldPanel('cover'),
    ]

    class Meta:
        verbose_name_plural = 'stories'

    def __str__(self):
        """Return the title of the story."""
        return self.title