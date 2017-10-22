from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.TextField()

    def __str__(self):
        return self.name
