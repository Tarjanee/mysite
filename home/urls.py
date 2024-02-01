from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("",views.index,name="home"),
   path("about",views.about,name="about"),
   path("services",views.services,name="services"),
   path("contact",views.contact,name="contact"),
   path("dessert",views.dessert,name="dessert"),
   path("pizza",views.pizza,name="pizza"),
   path("drink",views.drink,name="drink"),
   path("indian",views.indian,name="indian"),
   path("indian_sweets",views.indian_sweets,name="indian_sweets"),
   path("indian_chaat",views.indian_chaat,name="indian_chaat")
]