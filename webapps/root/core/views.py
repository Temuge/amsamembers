from django.shortcuts import render
from models import Member


# Create your views here.

def index(request):
    return render(request, 'core/index.html', None)

def submitRegistration(request):
	firstName = request.POST['firstName']
	lastName = request.POST['lastName']
	emailAddress = request.POST['emailAddress']
	print firstName
	print lastName
	print emailAddress
	context={'firstName' : firstName}
	Member(first_name=firstName, last_name=lastName, email_address=emailAddress).save()
	return render(request, 'core/submitRegistration.html', context)
