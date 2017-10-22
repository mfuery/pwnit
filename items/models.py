from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    uuid = models.CharField(max_length=36)  # ref_id in blockchain

    def __str__(self):
        return self.name


class Block(models.Model):
    uuid = models.CharField(max_length=36)  # ref_id in blockchain
    previous_block = models.CharField(max_length=36)  # ref_id in blockchain
    contents = models.TextField()
