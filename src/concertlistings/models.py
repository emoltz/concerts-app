from django.db import models
from django.urls import reverse


class Concert(models.Model):

    id = models.CharField(primary_key=True, max_length=240)
    title = models.CharField(max_length=240)
    artist = models.CharField(max_length=240)
    venue = models.CharField(max_length=240)
    date = models.DateTimeField()
    genre = models.CharField(max_length=240)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    ticket_url = models.TextField()
    image = models.ImageField(upload_to='uploaded_images/', default=None, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("concerts:concert-detail", kwargs={"id": self.id})
