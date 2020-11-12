from django.shortcuts import render, get_object_or_404

from .models import Zawodnik, ListaDruzyn

def strona_zawodnicy(request):

    lista_zawodnikow = Zawodnik.objects.all()
    return render(request, 'lista_zawodnikow.html', {'zawodnicy': lista_zawodnikow})

def zawodnik(request, id):

    zawodnik_ = get_object_or_404(Zawodnik, pk=id)
    return  render(request, 'zawodnik.html', {'zawodnik': zawodnik_})

def terminarz(request):

    tempo_bialka = ListaDruzyn.objects.get(id=1)
    halniak_makow = ListaDruzyn.objects.get(id=2)
    garbarz_zembrzyce = ListaDruzyn.objects.get(id=3)
    sucha_beskidzka = ListaDruzyn.objects.get(id=4)
    return render(request, 'terminarz.html', {'tb': tempo_bialka, 'hmp': halniak_makow, 'gz': garbarz_zembrzyce,
                                              'sb': sucha_beskidzka})