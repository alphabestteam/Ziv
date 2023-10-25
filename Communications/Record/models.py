from django.db import models
from User.models import User
from File.models import File 

class Record(File):
    file_ptr = models.OneToOneField(File, parent_link=True, on_delete=models.CASCADE, related_name='record', default= None)
    upload_date = models.DateField()
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='records/')