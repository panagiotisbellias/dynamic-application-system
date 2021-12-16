from django.contrib import admin
from . import models

# Panagiotis Bellias
admin.site.register(models.Application)
admin.site.register(models.Carrier)
admin.site.register(models.Citizen)
admin.site.register(models.Manager)
admin.site.register(models.PersonnelDepartment)
admin.site.register(models.SuperVisor)