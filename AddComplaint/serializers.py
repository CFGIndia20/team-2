from rest_framework import serializers
from AddComplaint import models


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Complaint
        fields='__all__'