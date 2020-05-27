from django.contrib import admin
from .models import ChangeRequest, ClientManager

admin.site.register(ChangeRequest)
admin.site.register(ClientManager)