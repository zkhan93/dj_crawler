from django.conf.urls import url,include
from . import views
urlpatterns=[
	url(r'^$',views.home,name="home"),
	url(r'^login/$',views.user_login,name="user_login"),
	url(r'^crawl$',views.crawl_home,name="crawl_home"),
	url(r'^start$',views.start_crawling,name="start_crawling"),
]