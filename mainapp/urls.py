from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'userlist', views.myListings),
	url(r'showlist', views.showListings),
	url(r'addtolist', views.addToListing),
	url(r'goToCreateListing', views.goToCreateListing),
	url(r'createlist', views.createListing),
    url(r'', views.startup),
 ]