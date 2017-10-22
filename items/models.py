from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    asset = models.ForeignKey('items.Game')
    owner = models.OneToOneField(User)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.TextField()

    def __str__(self):
        return self.name


class Block(models.Model):
    uuid = models.CharField(max_length=36)  # ref_id in blockchain
    previous_block = models.CharField(max_length=36)  # ref_id in blockchain
    contents = models.TextField()
