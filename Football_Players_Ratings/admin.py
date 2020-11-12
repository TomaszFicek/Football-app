from django.contrib import admin

from .models import Zawodnik, ListaDruzyn

@admin.register(Zawodnik)
class ZawodnikAdmin(admin.ModelAdmin):

    list_display = [ 'Imie', 'Nazwisko', 'Wiek', 'Pozycja_na_boisku', 'Druzyna',]

@admin.register(ListaDruzyn)
class ListaDruzynAdmin(admin.ModelAdmin):

    search_fields = ["nazwa_druzyny",]

