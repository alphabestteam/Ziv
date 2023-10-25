from django.db import models
from File.models import File 

class ChatFile(File):
    messages = models.ManyToManyField('Message.Message', related_name='chat_files', blank=True)


