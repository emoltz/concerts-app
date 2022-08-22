from django.db import models
from django.urls import reverse


class Concert(models.Model):

    artist = models.CharField(max_length=240)
    venue = models.CharField(max_length=240)
    city = models.CharField(max_length=240)
    state = models.CharField(max_length=240)
    country = models.CharField(max_length=240)
    date = models.DateTimeField()
    genre = models.CharField(max_length=240)

    def get_absolute_url(self):
        return reverse("concerts:concert-detail", kwargs={"id": self.id})

    def get_home_page(self):
        return reverse("concerts:concert-list")