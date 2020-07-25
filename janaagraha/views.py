from django.shortcuts import render
from django.http import HttpResponse


def complain(request):
	return render(request, 'janaagraha/send_complain.html')