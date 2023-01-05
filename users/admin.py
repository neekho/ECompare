from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from . models import User, Customer, Retailer, CustomerProfile, RetailerProfile
# Register your models here.

# admin.site.register(User, UserAdmin)
# admin.site.register(Customer, UserAdmin)
admin.site.register(Retailer, UserAdmin)
# admin.site.register(CustomerProfile)
admin.site.register(RetailerProfile)
