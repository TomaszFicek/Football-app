"""Football_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from Football_Players_Ratings.views import strona_zawodnicy, zawodnik, terminarz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lista_zawodnikow/', strona_zawodnicy),
    path('zawodnik/<int:id>/', zawodnik, name='zawodnik_URL' ),
    path('terminarz/', terminarz),
]
