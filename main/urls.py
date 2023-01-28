from django.urls import path, include

from . import views

from .views import LaptopListView, LaptopDetailView, LaptopCreateView, LaptopUpdateView, LaptopDeleteView, RetailerListView, QRView


urlpatterns = [

    path('',  views.shop_view, name='main-home'), 
    path("search/", views.list_search_view, name="search"),

    path("compare/", views.compare, name="compare"),


    path('retailer/<str:retailer_name>/', RetailerListView.as_view(), name='retailer-posts'),


    path('laptop/<str:pk>/',  LaptopDetailView.as_view(), name='laptop-detail'), #!

    path('manage/new/',  LaptopCreateView.as_view(), name='laptop-create'), 

    path('laptop/<str:pk>/update/',  LaptopUpdateView.as_view(), name='laptop-update'),  #!

    path('laptop/<str:pk>/delete/',  LaptopDeleteView.as_view(), name='laptop-delete'), #!


    path('laptop/qr/<str:pk>/', QRView.as_view(), name='laptop-qr'), #!


    path('about/', views.about, name='main-about'),


]


# ###### Wed Dec 28 22:08:17 CST 2022
# ** to do
# ** populate laptop models (change price field into integer) OK
# ** comparison logic MEDJ OK


# ** measure query return time for chapter 4
# ** re-write chapter 1 (scope)