# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Member(models.Model):
	last_name = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	email_address = models.CharField(max_length=100, unique=True)
