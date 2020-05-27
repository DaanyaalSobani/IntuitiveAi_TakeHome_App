from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class WasteManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + "-" + self.organization.name


class Trash(models.Model):
    TYPE_CHOICES = (
        ('R', 'Recyclable'),
        ('P', 'Paper'),
        ('L', 'Landfill'),
        ('C', 'Compost'),
    )
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    organization = models.ManyToManyField(Organization)

    def __str__(self):
        return self.name

