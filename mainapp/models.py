from __future__ import unicode_literals

from django.db import models
import datetime

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

class ToCampus(models.Model):
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
  uid = models.CharField(primary_key=True, max_length=40)
  phoneNumberListing = models.CharField(max_length=20, primary_key=False)
  userPhone = models.CharField(max_length=20)
  userName = models.CharField(max_length=20)
  def __unicode__(self):
    return self.userName