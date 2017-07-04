from django.db import models


class Shelter(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    hours = models.CharField(max_length=200)

    def __str__(self):
        return self.name
