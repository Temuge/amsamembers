#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

MAILGUN_SECRET_KEY = 'key-5a12a0cc0bc377c7b610ee95415c078c'
MAILGUN_DOMAIN_TEST = 'mail.amsa.mn'
WHITELISTED_EMAIL_MAP = {"temuge@mit.edu" : "temuge.ez@gmail.com"}

def send_email_confirmation_mail(firstName, schoolEmailAddress, url):
        to = checkWhiteListedMail(schoolEmailAddress)
	domain = MAILGUN_DOMAIN_TEST
	fromEmail = "AMSA <registration@{0}>".format(domain)
	subject = "Confirm your email address"
	context = {'firstName': firstName, 'url': url}
	html = render_to_string('core/confirmEmailMailTemplate.html', context)
	send_mailgun_email(domain, fromEmail, [to], subject, html)


def send_acceptance_mail(firstName, schoolEmailAddress):
        to = checkWhiteListedMail(schoolEmailAddress)
        domain = MAILGUN_DOMAIN_TEST
        fromEmail = "AMSA <registration@{0}>".format(domain)
        subject = "Welcome to AMSA"
        context = {'firstName': firstName}
        html = render_to_string('core/acceptanceLetter.html', context)
        send_mailgun_email(domain, fromEmail, [to], subject, html)

def send_rejection_mail(firstName, schoolEmailAddress):
        to = checkWhiteListedMail(schoolEmailAddress)
        domain = MAILGUN_DOMAIN_TEST
        fromEmail = "AMSA <registration@{0}>".format(domain)
        subject = "АМОХ-ны гишүүнчлэлийн өргөдөл"
        context = {'firstName': firstName}
        html = render_to_string('core/rejectionLetter.html', context)
        send_mailgun_email(domain, fromEmail, [to], subject, html)

def send_pending_mail(firstName, schoolEmailAddress):
        to = checkWhiteListedMail(schoolEmailAddress)
        domain = MAILGUN_DOMAIN_TEST
        fromEmail = "AMSA <registration@{0}>".format(domain)
        subject = "АМОХ-ны гишүүнчлэлийн өргөдөл"
        context = {'firstName': firstName}
        html = render_to_string('core/pendingLetter.html', context)
        send_mailgun_email(domain, fromEmail, [to], subject, html)

def send_mailgun_email(domain, fromEmail, tos, subject, html):
        #TODO: handle ssl warning!!!
        r = requests.post(
                "https://api.mailgun.net/v3/{0}/messages".format(domain),
                auth=("api", MAILGUN_SECRET_KEY),
                data={"from": fromEmail,
                	  "to": tos,
                	  "subject": subject,
                	  "html": html})

def checkWhiteListedMail(schoolEmailAddress):
        return WHITELISTED_EMAIL_MAP[schoolEmailAddress] if schoolEmailAddress in WHITELISTED_EMAIL_MAP else schoolEmailAddress