from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from django.core.mail import send_mail
from django.conf import settings

# from .form import contactForm

# def contact(request):
# 	title = 'Contact'
# 	form = contactForm(request.POST or None)
# 	# context = {'title': title, 'form': form,}
# 	confirm_message = None

# 	if form.is_valid():
# 		name = form.cleaned_data['name']
# 		comment = form.cleaned_data['comment']
# 		subject = 'Message from mysite'
# 		message = '%s %s' %(comment, name)
# 		emailFrom = form.cleaned_data['email']
# 		emailTo = [settings.EMAIL_HOST_USER]
# 		send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
# 		title = "Thanks"
# 		confirm_message = "Thanks for the message we willget back to you" 
# 		form = None

# 	context = {'title': title, 'form': form, 'confirm_message': confirm_message,}

# 	template = 'contact.html'
# 	return render(request, template, context)

# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request, template, context)

def login(request):
	context = {}
	template = 'account/login.html'
	return render(request, template, context)

def signup(request):
	context = {}
	template = 'account/signup.html'
	return render(request, template, context)

def about(request):
	context = {}
	template = 'about.html'
	return render(request, template, context)

def shop(request):
	context = {}
	template = 'shop/base.html'
	return render(request, template, context)

@login_required
def userProfile(request):
	context = {'user': request.user}
	template = 'profile.html'
	return render(request, template, context)

@login_required
def dashboard(request):
	template = 'dashboard.html'
	return render(request, template,)

# def contact(request):
# 	context = locals()
# 	template = 'contact.html'
# 	return render(request, template, context)