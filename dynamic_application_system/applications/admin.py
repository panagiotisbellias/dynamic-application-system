from django.contrib import admin
from . import models

# Panagiotis Bellias
class ApplicationAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'headline', 'content']
    fieldsets = [
        ('Content Information', {'fields':['headline', 'content']}),
        ('Date Information', {'fields':['pub_date']}),
    ]

admin.site.register(models.Application, ApplicationAdmin)


admin.site.register(models.Carrier)
admin.site.register(models.Citizen)
admin.site.register(models.Manager)
admin.site.register(models.PersonnelDepartment)
admin.site.register(models.SuperVisor)