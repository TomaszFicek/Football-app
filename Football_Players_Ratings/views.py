from django.shortcuts import render, get_object_or_404

from .models import Zawodnik

def strona_zawodnicy(request):

    lista_zawodnikow = Zawodnik.objects.all()
    return render(request, 'lista_zawodnikow.html', {'zawodnicy': lista_zawodnikow})

def zawodnik(request, id):

    zawodnik_ = get_object_or_404(Zawodnik, pk=id)
    return  render(request, 'zawodnik.html', {'zawodnik': zawodnik_})