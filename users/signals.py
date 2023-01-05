from django.db.models.signals import post_save
from django.dispatch import receiver

from . models import User, Customer, Retailer, CustomerProfile, RetailerProfile




@receiver(post_save, sender=User) # sender=User  #
def create_user_profile(sender, instance, created, **kwargs):
    '''
        Populates the CustomerProfile entity once 
        a User of Customer role is created
    '''
    if created and instance.role == "CUSTOMER":
        CustomerProfile.objects.create(user=instance)

    else:
        print('NOT == CUSTOMERF')

@receiver(post_save, sender=Customer) 
def save_profile(sender, instance,  **kwargs):
    instance.customerprofile.save()



















@receiver(post_save, sender=Retailer) # User # 
def create_user_profile(sender, instance, created, **kwargs):
    '''
        Populates the RetailerProfile entity once 
        a User of Retailer role is created
    '''
    if created and instance.role == "RETAILER":
        RetailerProfile.objects.create(retailer=instance)

    else:
        print('NOT == TO RETAILER')







@receiver(post_save, sender=Retailer) 
def save_profile(sender, instance,  **kwargs):
    instance.retailerprofile.save()





