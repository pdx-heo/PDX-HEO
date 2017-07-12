from django.db import models


# Organizations provide services
class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    hours_open = models.TimeField('open time')
    hours_close = models.TimeField('close time')

    def __str__(self):
        return self.name


class Shelter(models.Model):
    name = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    hours_open = models.TimeField('open time')
    hours_close = models.TimeField('close time')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
