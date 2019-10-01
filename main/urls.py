"""monSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.indexHotel, name='indexHotel'),
    path("reservation", views.reservation, name='reservation'),
    path("historique",views.historique, name='historique'),
    path("hotels", views.differentsHotels, name='hotels'),
    #path("hotels/(?p<page>\)", views.differentsHotels, name='hotels')
    #path("hotels/<int:page>/", views.differentsHotels, name='hotels')
    path('contacts',views.contacts, name='contacts'),
    path('recherche',views.recherche, name='recherche'),

    path("page",views.mapage,name='pagea'),
    path("home",views.homepage,name="homepage"),
    path('essai',views.experience,name='experience'),
    path('donne',views.basedo, name='donnees'),
    path('contact',views.contact, name='contact')
]
