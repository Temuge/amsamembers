from django.shortcuts import render
from django.db import transaction
from models import *
from dateHelper import *
import uuid
from emailUtils import *
import re

def index(request):
	context = {}
	return render(request, 'core/index.html', context)

def registration(request):
	schoolEmail= "{}.edu".format(request.GET['schoolEmailPrefix'])
	context = {"schoolEmail": schoolEmail}
	domainName = re.search("@[\w.]+", schoolEmail).group()[1:]
	uni = loadUniversityIfExists(domainName)
	if uni != None:
		context['university'] = uni
	context.update(getDateTimeContext())
	context['degreeLevels'] = MemberUniversity.SCHOOL_DEGREE_CHOICES
	return render(request, 'core/registration.html', context)

@transaction.atomic
def submitRegistration(request):
	firstName = request.POST['firstName']
	context={'firstName' : firstName}
	externalId = uuid.uuid4().hex
	schoolEmail = request.POST['schoolEmail']
	schoolDomainName = retrieveDomain(schoolEmail)
	university = loadUniversityIfExists(schoolDomainName)
	if university != None:
		schoolName = university.school_name
	else:
		schoolName = request.POST['schoolName']
	newApplicant = Member(first_name = request.POST['firstName'],	
						  last_name = request.POST['lastName'],
						  date_of_birth = datetime.date(
						  	year=int(request.POST['birthYear']), 
						  	month=int(request.POST['birthMonth']),
						  	day=int(request.POST['birthDay'])),
						  address1 = request.POST['address1'],
						  address2 = request.POST['address2'],
						  city = request.POST['city'],	
						  state = request.POST['state'],
						  zip_code = request.POST['zip'],
						  phone_number = request.POST['phoneNumber'],
						  personal_email_address = request.POST['personalEmail'],
						  facebook_link = request.POST['facebookLink'],
						  linked_in_link = request.POST['linkedInLink'],
						  external_id = externalId,
						  school_name = schoolName)
	newApplicant.save()
	memberUni = MemberUniversity(
			member = newApplicant,
			university_assigned = university if university != None else None,
			school_email_address = schoolEmail,
			degree_level = request.POST['degreeLevel'],
			graduation_year = int(request.POST['graduationYear']),
			major = request.POST['major'],
			second_major = request.POST['secondMajor'])
	memberUni.save()
	redirect_url = url = request.build_absolute_uri(reverse(
		'core:confirmEmail', 
		kwargs={'externalId': externalId, 'id' : newApplicant.id}))
	send_email_confirmation_mail(
		firstName,
		schoolEmail,
		redirect_url)
	return render(request, 'core/submitRegistration.html', context)


def confirmEmail(request, externalId, id):
	print externalId
	print id
	member = Member.objects.get(id=id)
	confirmed = (member.external_id == externalId)

	if (confirmed and member != None):
		uniMember = MemberUniversity.objects.get(member=member)
		member.acceptance_status = Member.ACCEPTED if uniMember.university_assigned != None else Member.HOLDING
		member.save()
	isAccepted = (member.acceptance_status==Member.ACCEPTED)
	return render(request, 'core/emailConfirmed.html', {'isAccepted':isAccepted})

# Helper
def loadOrCreateUniversity(domainName, schoolName):
	existing = loadUniversityIfExists(domainName)
	if existing == None:
		uni = University(school_name = schoolName, school_domain_name = domainName)
		uni.save()
		return uni
	else:
		return existing

# Helper
def loadUniversityIfExists(domainName):
	universities = University.objects.filter(school_domain_name=domainName)
	if len(universities) > 0:
		return universities[0]
	else:
		return None
# Helper
def retrieveDomain(schoolEmail):
	return re.search("@[\w.]+", schoolEmail).group()[1:]
