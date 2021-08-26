from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#Comment rawn luhna tur

class Comment(models.Model):
    hming = models.CharField(max_length=30)
    # comment_tu = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)

    def __str__(self):
        return self.hming

    def get_absolute_url(self):
        return reverse('success')

