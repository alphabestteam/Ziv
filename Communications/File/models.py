from django.db import models
from User.models import User

class File(models.Model):
    OPEN = 'Open'
    CLOSED = 'Closed'
    WAITING_RESPONSE = 'Waiting for Response'
    WAITING_TREATMENT = 'Waiting for Treatment'

    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
        (WAITING_RESPONSE, 'Waiting for Response'),
        (WAITING_TREATMENT, 'Waiting for Treatment'),
    )
    id = models.AutoField(primary_key=True)
    opening_date = models.DateField()
    closing_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_files')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=OPEN)
    collaborators = models.ManyToManyField(User, related_name='collaborated_files')
    filing_capacity = models.BooleanField(default=False)
    draft_capacity = models.BooleanField(default=False)

   