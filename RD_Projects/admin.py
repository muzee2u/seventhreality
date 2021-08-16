from django.contrib import admin
from .models import Project, Service, productDomain, serviceDomain
# Register your models here.


class ProductDomainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ServiceDomainAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','description')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name','description')


admin.site.register(productDomain, ProductDomainAdmin)
admin.site.register(serviceDomain, ServiceDomainAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
