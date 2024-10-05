from django.db import models

# Create your models here.

class Article(models.Model): 
    title = models.CharField(max_length=64, blank=False, unique=False)
    year = models.PositiveSmallIntegerField(default=2024)

    # zwraca w panelu admina tytuł i dzięki temu się tak tam wyświetla
    def __str__(self):
        return self.title