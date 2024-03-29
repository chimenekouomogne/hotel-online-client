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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views                         # ligne ajouté

urlpatterns = [
    
    path('', include('main.urls', namespace='main')),
    path('sb_admin', views.blank, name='blank'),
    path('404', views.page404, name='404'),

    path('ajouter_personnel', views.ajouterPersonnel,name='ajouterPersonnel'),
    path('personnel', views.personnel, name='personnel'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # ligne ajouté pour pouvoir utiliser les fichiers ds media

