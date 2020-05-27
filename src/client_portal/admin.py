from django.contrib import admin

from .models import WasteManager, Organization,Trash

admin.site.register(WasteManager)
admin.site.register(Organization)
admin.site.register(Trash)