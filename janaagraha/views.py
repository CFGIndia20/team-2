from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import json
from AddComplaint import models, forms

def complain(request):
	complaintform=forms.ComplaintForm()
	
	if request.method=='POST':
		complaintform=forms.ComplaintForm(request.POST)
		if True:#complaintform.is_valid():
			print(1)
			print()
			print()
			complaint=complaintform.save()
			return HttpResponseRedirect('')
		#context['status']=False
	context={
        "complaintform": complaintform,
		'status': True
    }
	return render(request,'janaagraha/send_complain.html',context)
