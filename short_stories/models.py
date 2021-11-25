from django.db import models

class Story(models.Model):
    """The published short story."""
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    synopsis = models.TextField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='media/')

    class Meta:
        verbose_name_plural = 'stories'

    def __str__(self):
        """Return the title of th story."""
        return self.title