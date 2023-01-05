from django import forms
from users.models import User, Customer
from django.contrib.auth.forms import UserCreationForm
from . models import CustomerProfile, RetailerProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User #Customer #
        fields = ['username', 'email', 'password1', 'password2']





# for changing user basic info such as username and email
class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']





# for changing customer profile pics
class CustomerProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomerProfile
        fields = ['customer_image']











# for changing retailer profile pics
class RetailerProfileUpdateForm(forms.ModelForm):



    class Meta:
        model = RetailerProfile
        fields = ['retailer_name', 'website_url', 'retailer_image', ]