from django.contrib import admin

from .models import Zawodnik

@admin.register(Zawodnik)
class ZawodnikAdmin(admin.ModelAdmin):

    list_display = [ 'Imie', 'Nazwisko', 'Wiek', 'Pozycja_na_boisku', 'Druzyna',]