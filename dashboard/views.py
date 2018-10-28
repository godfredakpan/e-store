from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def dashboard(request):
	template = 'dashboard.html'
	return render(request, template,)


@login_required
def user(request):
	template = 'user.html'
	return render(request, template,)
