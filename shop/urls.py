from django.contrib import admin
from django.urls import path,include

from.import views

urlpatterns = [
    path("",views.index,name="shophome"),
    path('aboutus/',views.about , name="aboutUs"),
    path('contactus/',views.contact , name="contactUs"),
    path('tracker/',views.tracker , name="tracker"),
    path('productView/',views.productView , name="productViews"),
    path('search/',views.search , name="search"),
    path('checkout/',views.checkout , name="checkout")
]