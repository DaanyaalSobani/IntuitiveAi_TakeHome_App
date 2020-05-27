from django.contrib import admin

from .models import WasteManager, Organization

admin.site.register(WasteManager)
admin.site.register(Organization)