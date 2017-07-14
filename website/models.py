from django.db import models


# Create your models here.
# Organizations provide services
class Organization(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  website = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  hours_open = models.TimeField('open time')
  hours_close = models.TimeField('close time')
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.name


class Shelter(models.Model):
  organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  website = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  hours_open = models.TimeField('open time')
  hours_close = models.TimeField('close time')
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.name
