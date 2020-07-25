from django.db import models

class Complaint(models.Model):
    CATEGORY=()
    mobileNumber=models.IntegerField()
    description=models.TextField()
    location=models.TextField()
    timeCreated=models.DateTimeField(auto_now=True)
    timeUpdated=models.DateTimeField(auto_now=True) 
    status=models.CharField(max_length=256)
    category=models.CharField(max_length=256)


    
