from django.db import models
from django.utils import timezone

# Create your models here.
class Issue(models.Model):
    issue_name = models.CharField(max_length=100)
    issue_description = models.CharField(max_length=500)
    issue_status = models.CharField(default="Open")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.issue_name} was created on {self.date_created}'
