from django.db import models

class Complaint(models.Model):
    mobileNumber=models.BigIntegerField()
    description=models.TextField()
    location=models.CharField(max_length=256)
    timeCreated=models.DateTimeField(auto_now=True)
    timeUpdated=models.DateTimeField(auto_now=True ) 
    status=models.CharField(max_length=256, default='progress',null=True, blank=True)
    category=models.CharField(max_length=256, default='',null=True, blank=True)


    
