from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import *
from bs4 import BeautifulSoup
import requests
from urlparse import urlparse,urljoin

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
def crawl_home(request):
	data=dict()
	try:
		data['inputs']=Input.objects.all()
	except Exception as ex:
		data['error']=True
		data['msg']=str(ex)
	return render(request,'crawl/crawl_home.html',data)

@login_required
def start_crawling(request):
	for input in Input.objects.all().filter(processed=False):
		insert_categories(get_posts(input),input)
		input.processed=True;
	return redirect('/crawl')

def get_posts(input):
	headings=['h1','h2','h3','h4','h5','h6']
	parsed_uri = urlparse(input.url)
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	soup=BeautifulSoup(requests.get(input.url).text,"html.parser")
	categories=[]
	# print 'container:',input.container_identifier
	for cat in soup.find_all(input.category_container_identifier.dom,class_=input.category_container_identifier.css_selector):
		category=dict()
		category_title=cat.find(class_=input.category_title_identifier.css_selector)
		if category_title:
			category_title=category_title.get_text()
		category['title']=category_title

		posts=[]
		for story in cat.find_all(input.post_container_identifier.dom,class_=input.post_container_identifier.css_selector):
			tmp_post=dict()	

			story_title=story.find(input.post_title_identifier.dom,class_=input.post_title_identifier.css_selector)
			if story_title:
				story_title=story_title.get_text()
			else:
				story_title=''
			# print story_title
			tmp_post['title']=story_title;

			# print 'post_summary=',input.post_summary_identifier
			story_summary=story.find(str(input.post_summary_identifier.dom),class_=str(input.post_summary_identifier.css_selector))
			if story_summary:
				story_summary=story_summary.get_text()
			else:
				story_summary=''
			# print story_summary
			tmp_post['summary']=story_summary;

			story_link=story.find("a")
			if story_link:
				story_link=story_link["href"]
				if not story_link.startswith('http'):
					story_link=urljoin(domain,story_link)
			else:
				story_link=''
			tmp_post['link']=story_link;
			posts.append(tmp_post)
		category['posts']=posts
		categories.append(category)
	return categories

def insert_posts(posts,category,input):
	if not category:
		print 'no category skipped inserting posts: ',posts
		return
	if not input:
		print 'no input skipped inserting posts:\n',posts
		return
	for p in posts:
		if set(['title','summary','link']).issubset(p.keys()):
			post=Post()
			post.title=p['title']
			post.summary=p['summary']
			post.link=p['link']
			post.input=input
			post.save()
			category.posts.add(post)
		else:
			print 'invalid post skipping:',p

def insert_categories(categories,input):
	if not categories:
		print 'no category skipped inserting categories: ',categories
		return
	if not input:
		print 'no input skipped inserting posts:\n',posts
		return
	for category in categories:
		cat=None
		if 'title' in category.keys() and category['title'] and len(category['title'].strip()) > 0:
			try:
				cat=Category.objects.get(name=category['title'])
			except:
				cat=Category()
				cat.name=category['title']
				cat.title=category['title']
				cat.summary=category['title']
			cat.save()
			insert_posts(category['posts'],cat,input)
		else:
			print 'invalid category skipping:',category