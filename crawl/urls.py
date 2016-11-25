from django.conf.urls import url,include
from . import views
urlpatterns=[
	url(r'^$',views.home,name="home"),
	url(r'^login/$',views.user_login,name="user_login"),
	url(r'^crawl$',views.crawl,name="crawl"),
	url(r'^start$',views.start_crawling,name="start_crawling"),
]