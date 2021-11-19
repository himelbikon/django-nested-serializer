from django.db import models


class Universe(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    universe = models.ForeignKey(
        Universe, related_name='movies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
