from django.db import models
from django.contrib.auth.models import User
from client_portal.models import Organization, WasteManager


class ChangeRequest(models.Model):
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    wastemanager = models.ForeignKey(WasteManager, on_delete=models.CASCADE)
    #TO DO - Make Change model and use many to many for changes.
    change_request_JSON = models.TextField()
    status = models.CharField(max_length=1, choices=(("P", "Pending"), ("C", "Closes")))
    created_date = models.DateTimeField(auto_now_add=True)
    closed_date = models.DateTimeField(null=True)


class ClientManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organizations = models.ManyToManyField(Organization)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
