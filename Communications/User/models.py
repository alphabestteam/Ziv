from django.db import models

class User(models.Model):
    id = models.PositiveIntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    unread_messages = models.ManyToManyField('Message.Message', related_name='messages', blank=True)



