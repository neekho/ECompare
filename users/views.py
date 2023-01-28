from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


from users.forms import UserRegisterForm, UserUpdateForm, CustomerProfileUpdateForm, RetailerProfileUpdateForm

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Account created for {username}')
            print(form.cleaned_data)

            return redirect('login')

    else:
        form = UserRegisterForm()
        

    return render(request, 'users/register.html', {'form':form})















@login_required
def profile(request):

    if request.method == 'POST':

        user_update = UserUpdateForm(request.POST, instance=request.user)

        customer_profile_update = CustomerProfileUpdateForm(request.POST, request.FILES, instance=request.user.customerprofile)

        if user_update.is_valid() and customer_profile_update.is_valid():
            user_update.save()
            customer_profile_update.save()

            messages.success(request, f'Account has been updated')
            return redirect('profile')


    else:
        user_update = UserUpdateForm(instance=request.user)

        customer_profile_update = CustomerProfileUpdateForm(instance=request.user.customerprofile)

    context = {
        'user_update': user_update,
        'customer_profile_update': customer_profile_update
    }

    return render(request, 'users/profile.html', context)








@login_required
def retailer_profile(request):
    if request.method == 'POST':

        user_update = UserUpdateForm(request.POST, instance=request.user)

        retailer_profile_update = RetailerProfileUpdateForm(request.POST, request.FILES, instance=request.user.retailerprofile)

        if user_update.is_valid() and retailer_profile_update.is_valid():
            user_update.save()
            retailer_profile_update.save()

            messages.success(request, f'Retail account has been updated')
            return redirect('retailer-profile')


    else:
        user_update = UserUpdateForm(instance=request.user)

        retailer_profile_update = RetailerProfileUpdateForm(instance=request.user.retailerprofile)

    context = {
        'user_update': user_update,
        'retailer_profile_update': retailer_profile_update
    }

    return render(request, 'users/retailer.html', context)


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_message = 'Password Updated!'
    success_url = reverse_lazy('main-home')

