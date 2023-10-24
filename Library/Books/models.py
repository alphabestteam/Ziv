from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, blank=True, null=True)
    publication_house = models.CharField(max_length=13)
    publication_date = models.DateField()
    rarity_level = models.CharField(max_length=20, default = "Common")


