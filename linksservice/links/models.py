from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    full_link = models.URLField(max_length=200)
    short_link = models.URLField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Link, self).save(*args, **kwargs)


