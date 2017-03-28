from django.contrib import admin

from .models import Supplier, SupplierPart, Customer

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','URL','contact')

admin.site.register(Customer, CompanyAdmin)
admin.site.register(Supplier, CompanyAdmin)
admin.site.register(SupplierPart)