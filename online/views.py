from django.shortcuts import render

from django.views.generic import TemplateView
def home(request):
	return render(request,template_name='home.html')

def signup(reuest):
	return render(request,template_name='signup.html')
	

