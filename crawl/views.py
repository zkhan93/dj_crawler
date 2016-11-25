from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import *

# Create your views here.
def home(request):
	if request.user.is_authenticated():
		return redirect('/crawl')
	return render(request,'crawl/user_login.html');

def user_login(request):
	data=dict()
	if request.user.is_authenticated():
		return redirect('/crawl')
	if request.method!='POST':
		data['error']=True
		data['msg']='Invalid request type'
		return render(request,'crawl/user_login.html',data)	
	username=request.POST['username']
	password=request.POST['password']
	user=authenticate(username=username,password=password)
	if user:
		login(request,user)
		return redirect('/crawl')
	else:
		data['error']=True
		data['msg']='Invalid username'
	return render(request,'crawl/user_login.html',data)

@login_required
def crawl(request):
	data=dict()
	return render(request,'crawl/crawl.html',data)

@login_required
def start_crawling(request):
	return render(request,'okay ')