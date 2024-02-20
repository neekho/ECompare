from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . models import Laptop
from users.models import Retailer, RetailerProfile

from django.contrib.auth.decorators import login_required

@login_required
def shop_view(request):

    posts, search = _search_laptop(request)

    context = {
        'posts': posts,
        'search': search
    }

    return render(request, 'main/laptops.html', context)


def _search_laptop(request):
    search = request.GET.get("search")
    print(search) # test lng
    # page = request.GET.get("page")
    posts = Laptop.objects.all().order_by('price')
    if search:
        posts = posts.filter(model_name__icontains=search) | posts.filter(brand_name__icontains=search)



    return posts, search or ""

def list_search_view(request):
    posts, search = _search_laptop(request)
    context = {"posts": posts, "search": search}
    return render(request, "main/search_results.html", context)


def compare(request):
    to_compare = request.GET.get("item") # !!!
    print(request.GET)

    print(to_compare) # debug

    posts = Laptop.objects.all()

    comparisons = posts.filter(model_name__icontains='GF63 THIN 10SC-856PH').order_by('price')

    context = {
        'posts': comparisons
    }

    return render(request, 'main/comparison.html', context)


class LaptopListView(ListView):
    model = Laptop
    template_name = 'main/laptops.html'
    context_object_name = 'items'
    # ordering = ['-price']

class LaptopDetailView(DetailView):
    model = Laptop
    
    

class LaptopCreateView(LoginRequiredMixin, CreateView):
    model = Laptop
    fields = ['brand_name', 'model_name', 'laptop_image', 'price', 'specs', 'laptop_url']


    def form_valid(self, form):
        '''
        Tells the Laptop model that the logged in user
        will be the retailer.
        '''

        form.instance.retailer = self.request.user.retailerprofile
        return super().form_valid(form)



class LaptopUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Laptop
    fields = ['brand_name', 'model_name', 'laptop_image', 'price', 'specs', 'laptop_url']

    def form_valid(self, form):
        form.instance.retailer = self.request.user.retailerprofile
        return super().form_valid(form)

    def test_func(self):
        '''
        Checks if the current logged in user is the retailer 
        of the laptop that will be updated.
        '''
        laptop = self.get_object()

        if self.request.user.retailerprofile == laptop.retailer:
            return True
        return False 



class LaptopDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Laptop


    success_url = '/shop' # where to redirect when the item is deleted

    def test_func(self):
        '''
        Checks if the current logged in user is the retailer 
        of the laptop that will be deleted.
        '''
        laptop = self.get_object()

        if self.request.user.retailerprofile == laptop.retailer:
            return True
        return False 








class RetailerListView(ListView):
    model = Laptop
    template_name: str = 'main/retailer_laptops.html'
    context_object_name = 'laptop'


    def get_queryset(self):
        '''
        Gets all the posts made by a certain retailer, will execute if 
        tapped on their username.
        '''
        maker = get_object_or_404(RetailerProfile, retailer_name=self.kwargs.get('retailer_name'))

    
        return Laptop.objects.filter(retailer=maker)



class QRView(DetailView):
    model = Laptop
    template_name = 'main/qr_code.html'






def about(request):
    return render(request, 'main/about.html')