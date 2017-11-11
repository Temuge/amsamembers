# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class University(models.Model):
	school_name = models.CharField(max_length=100)
	school_domain_name = models.CharField(max_length=100, unique=True)
	approved = models.BooleanField(default=False)

# Create your models here.
class Member(models.Model):
	last_name = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	address1 = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	zip_code = models.CharField(max_length=10)
	phone_number = models.CharField(max_length=20)
	personal_email_address = models.CharField(max_length=250, unique=True)
	facebook_link = models.CharField(max_length=250)
	linked_in_link = models.CharField(max_length=250, null=True)
	# PENDING means student filled out the application but not confirmed the amil
	PENDING = 'PE'
	ACCEPTED = 'AC'
	REJECTED = 'RE'
	# HOLDING means the student approved the email but the student is not accepted nor rejected
	HOLDING = 'HO'
	ACCEPTANCE_STATUS_CHOICES = (
		(PENDING, 'Pending'),
		(ACCEPTED, 'Accepted'),
		(REJECTED, 'Rejected'),
		(HOLDING, 'Holding'),
	)
	acceptance_status = models.CharField(
		max_length =2,
    	choices = ACCEPTANCE_STATUS_CHOICES,
    	default = PENDING,
	)
	external_id = models.CharField(max_length=100, unique=True)
	school_name = models.CharField(max_length=100, null=True)

	def __str__( self ):
		return "{0} {1} ({2})".format(self.first_name, self.last_name, self.personal_email_address)

class MemberUniversity(models.Model):
	member = models.ForeignKey(Member)
	university_assigned = models.ForeignKey(University, null=True)
	school_email_address = models.CharField(max_length=250, unique=True)
	BACHELOR = 'BA'
	MASTER = 'MA'
	DOCTOR = 'DR'
	SCHOOL_DEGREE_CHOICES = (
    	(BACHELOR, 'Bachelor\'s'),
		(MASTER, 'Master\'s'),
		(DOCTOR, 'Doctoral'),
	)
	degree_level = models.CharField(
		max_length=2,
    	choices=SCHOOL_DEGREE_CHOICES)
	graduation_year = models.IntegerField()
	major = models.CharField(max_length=250)
	second_major = models.CharField(max_length=250, null=True)
