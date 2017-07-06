from django.db import models


class ServiceType(models.Model):
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Organizations provide services
class Organization(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    hours_open = models.TimeField('open time')
    hours_close = models.TimeField('close time')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    type = models.ForeignKey(ServiceType)
    pub_date = models.DateTimeField('date published')
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    hours_open = models.TimeField('open time')
    hours_close = models.TimeField('close time')

    def __str__(self):
        return self.name

