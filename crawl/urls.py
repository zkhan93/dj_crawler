from django.conf.urls import url,include
from . import views
urlpatterns=[
	url(r'^$',views.user_login,name="user_login"),
]