from django.db import models

class Location(models.Model):
    name=models.CharField(max_length=200, blank=True, null=True)
    description=models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.name