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

class CarrierAdmin(admin.ModelAdmin):
    fields = ['full_name', 'job_object']

admin.site.register(models.Carrier, CarrierAdmin)

class ApplicationInline(admin.TabularInline):
    model = models.Application
    extra = 1

class CitizenAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields':['full_name', 'job'], 'classes':['collapse']}),
    ]
    inlines = [ApplicationInline]

admin.site.register(models.Citizen, CitizenAdmin)

admin.site.register(models.Manager)

admin.site.register(models.PersonnelDepartment)
admin.site.register(models.SuperVisor)