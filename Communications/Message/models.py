from django.db import models
from User.models import User
from ChatFile.models import ChatFile


class Message(models.Model):
    id =  models.AutoField(primary_key=True) 
    text = models.TextField()
    sending_date = models.DateField()
    chat_file = models.ForeignKey(ChatFile, on_delete=models.CASCADE, null=True, blank=True, related_name="message")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
