from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'', views.startup),
    url(r'([0-9]+)', views.listings)
 ]