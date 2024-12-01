from django.db import models

# Create your models here.
class Issue(models.Model):
    issue_name = models.CharField(max_length=100)
    issue_description = models.CharField(max_length=500)
    issue_status = models.BooleanField()
    date_created = models.DateField()

    def __str__(self):
        return f'{self.issue_name} was created on {self.date_created}'
