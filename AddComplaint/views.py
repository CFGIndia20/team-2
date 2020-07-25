from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )
from AddComplaint import serializers, models

class createComplaint(ListCreateAPIView):
    queryset= models.Complaint.objects.all()
    serializer_class=serializers.ComplaintSerializer

class updateComplaint(RetrieveUpdateDestroyAPIView):
    queryset= models.Complaint.objects.all()
    serializer_class=serializers.ComplaintSerializer