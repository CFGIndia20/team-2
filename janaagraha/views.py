from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import json
from AddComplaint import models, forms

def complain(request):
	complaintform=forms.ComplaintForm()
	if request.method=='POST':
		complaintform=forms.ComplaintForm(request.POST)
		complaint=complaintform.save()
		return HttpResponseRedirect('')
	context={
        "complaintform": complaintform,
		'status': True
    }
	return render(request,'janaagraha/send_complain.html',context)
