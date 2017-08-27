import requests
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse

MAILGUN_SECRET_KEY = 'key-5a12a0cc0bc377c7b610ee95415c078c'
MAILGUN_DOMAIN_TEST = 'sandbox8b895169a282427d892eae1142f022fc.mailgun.org'
WHITELISTED_EMAIL_MAP = {"temuge@mit.edu" : "temuge.ez@gmail.com"}

def send_email_confirmation_mail(firstName, schoolEmailAddress, url):
        to = WHITELISTED_EMAIL_MAP[schoolEmailAddress] if schoolEmailAddress in WHITELISTED_EMAIL_MAP else schoolEmailAddress
	domain = MAILGUN_DOMAIN_TEST
	fromEmail = "AMSA <mailgun@{0}>".format(domain)
	subject = "Confirm your email address"
	context = {'firstName': firstName, 'url': url}
	html = render_to_string('core/confirmEmailMailTemplate.html', context)
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