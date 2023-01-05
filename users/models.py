from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

class User(AbstractUser):
    class Role(models.TextChoices):

        CUSTOMER = "CUSTOMER", "Customer"   
        RETAILER = "RETAILER", "Retailer"

    base_role = Role.CUSTOMER

    role = models.CharField(max_length=50, choices=Role.choices) ###########

    def save(self, *args, **kwargs):
        
            # ! Mon Dec 12 20:00:54 CST 2022
            # ! DI NAG UUPDATE YUNG DB PAG DI NAKA return super.save() ###### 

            # ! Mon Dec 12 20:15:16 CST 2022
            # ! KAYA WALANG NAGAGAWA NA RETAILER_RPROFILE KASI NAGIGING CUSTOMER YUNG ROLE NG RETAILER 

            ###### Mon Dec 12 20:31:51 CST 2022
            # ** NAKAKAGAWA NA NG RETAILER PROFILE, PERO VICE VERSA SCENARIO NA NANGYARI 
            # ! CUSTOMER_PROFILE, DI NAKAKAGAWA NG CUSTOMER_PROFILE BAKA NAGIGING RETAILER ROLE NG CUSTOMER???

            # ! Mon Dec 12 20:48:15 CST 2022
            # ! NAKAKAGAWA NA NG CUSTOMER AND RETAILER, AND AUTOMATIC NA YUNG PAG CREATE NG
            # ! CUSTOMER_PROFILE AT RETAILER_PROFILE PERO DI NANAMAN NAKAKA UPDATE YUNG DB

            # ** Mon Dec 12 20:52:50 CST 2022
            # ** oks na, bawal na galawin

            
        if not self.pk:
            self.role = self.base_role
            print(self.role)
        super().save(*args, **kwargs)



















class CustomerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CUSTOMER)

class Customer(User):

    base_role = User.Role.CUSTOMER

    print(base_role)


    customer = CustomerManager()
 
    class Meta:
        proxy = True



    


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    customer_image = models.ImageField(default='default-profile.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Customer Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.customer_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            img.save(self.customer_image.path)








































class RetailerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.RETAILER)



class Retailer(User):

    base_role = User.Role.RETAILER

    print(base_role)

    retailer = RetailerManager()
 
    class Meta:
        proxy = True
    



class RetailerProfile(models.Model):

    retailer = models.OneToOneField(Retailer, on_delete=models.CASCADE)

    retailer_name = models.CharField(max_length=50, default='Enter Retailer Name')

    website_url = models.URLField(default='Unvaible URL', max_length=500)

    retailer_votes = models.IntegerField(default=0)

    retailer_image = models.ImageField(default='default-profile.jpg', upload_to='retailer_pics')


    def __str__(self):
        return f'{self.retailer.username} Retailer Profile'


    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.retailer_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            img.save(self.retailer_image.path)

    










