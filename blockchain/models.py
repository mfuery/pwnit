from django.db import models


class Asset(models.Model):
    item_name = models.CharField(max_length=255)
    item_desc = models.TextField()


class User(models.Model):
    username = models.CharField(max_length=100)
