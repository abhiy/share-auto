from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class ToCNB(models.Model):
	datetime = models.DateTimeField()
  	name = models.CharField(max_length=20)
  	occupancy = models.IntegerField()
  	phoneNumber = models.CharField(max_length=11, primary_key=True)
  	def __unicode__(self):
  		return' '.join([
  			self.datetime,
  			self.name,
  			self.phoneNumber,
  			self.occupancy, 
  		])

class Users(models.Model):
	phoneNumberListing = models.IntegerField()(primary_key = True)
	userPhone = models.IntegerField()
	userName = models.CharField(max_length=20)