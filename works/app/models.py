from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Work(models.Model):

    TYPE = (
        ('Youtube', ('Youtube')),
        ('Instagram', ('Instagram')),
        ('Other', ('Other'))
    )


    link = models.CharField(max_length=255)
    work_type = models.CharField(
        max_length=255, choices = TYPE, default = False)


    def __str__(self):
        return self.link

class Artist(models.Model):
    name = models.CharField(max_length=255)

    work = models.ManyToManyField(Work)

    def __str__(self):
        return self.name
