from django import forms
from AddComplaint import models

class ComplaintForm(forms.ModelForm):
    class Meta:
        model=models.Complaint
        fields='__all__'