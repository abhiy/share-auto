from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'userlist', views.myListings),
    url(r'', views.startup),
    url(r'showlist', views.showListings),
 ]