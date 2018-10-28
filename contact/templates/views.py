from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from .form import contactForm

def contact(request):
	title = 'Contact'
	form = contactForm(request.POST or None)
	# context = {'title': title, 'form': form,}
	confirm_message = None

	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'Message from E-commerce'
		message = '%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
		title = "Thanks"
		confirm_message = "Thanks for the message we will get back to you" 
		form = None
		

	context = {'title': title, 'form': form, 'confirm_message': confirm_message,}

	template = 'contact.html'
	return render(request, template, context)
