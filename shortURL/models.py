from django.db import models

# Create your models here.
class UrlHandler(models.Model):
    longurl = models.CharField(max_length=200)
    shorturl = models.CharField(max_length=200)

    def __str__(self):
        return self.longurl
