from django.db import models

class ListaDruzyn(models.Model):

    nazwa_druzyny = models.CharField(max_length=64, null=False)

    def __str__(self):

        return "{}".format(self.nazwa_druzyny)


class Zawodnik(models.Model):

    POZYCJA_NA_BOISKU = {
        (0, 'Bramkarz'),
        (1, 'Środkowy obrońca'),
        (2, 'Boczny obrońca'),
        (3, 'Środkowy defensywny pomocnik'),
        (4, 'Środkowy ofensywny pomocnik'),
        (5, 'Boczny pomocnik'),
        (6, 'Wahadłowy'),
        (7, 'Napastnik'),
    }
    Imie = models.CharField(max_length=64, null=True)
    Nazwisko = models.CharField(max_length=64, null=True)
    Druzyna = models.ForeignKey(ListaDruzyn, on_delete=models.CASCADE)
    Wiek = models.PositiveSmallIntegerField(null=False)
    Pozycja_na_boisku = models.PositiveSmallIntegerField(choices=POZYCJA_NA_BOISKU)
    Fotografia = models.ImageField(upload_to="fotografie_zawodnikow", null=True, blank=True)





