from django.db import models

class Complaint(models.Model):
    STATUS=(
        ('s','in sysyem'),
        ('f', 'registered'),
        ('e', 'executed')
    )
    CATEGORY=()
    mobileNumber=models.IntegerField()
    description=models.TextField()
    location=models.TextField()
    timeCreated=models.DateTimeField(auto_now=True)
    timeUpdated=models.DateTimeField(auto_now=True) 
    status=models.CharField(choices=STATUS)
    category=models.CharField(max_length=1, choices=CATEGORY)
