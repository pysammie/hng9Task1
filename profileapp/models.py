from django.db import models

# Create your models here.

class Profile(models.Model):
    slackUsername = models.CharField(max_length=10)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=10)

    def __str__(self):
        return self.slackUsername
