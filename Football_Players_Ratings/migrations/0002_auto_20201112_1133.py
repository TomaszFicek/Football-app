# Generated by Django 3.1.3 on 2020-11-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Football_Players_Ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zawodnik',
            name='Pozycja_na_boisku',
            field=models.PositiveSmallIntegerField(choices=[(7, 'Napastnik'), (5, 'Boczny pomocnik'), (6, 'Wahadłowy'), (1, 'Środkowy obrońca'), (4, 'Środkowy ofensywny pomocnik'), (3, 'Środkowy defensywny pomocnik'), (2, 'Boczny obrońca'), (0, 'Bramkarz')]),
        ),
    ]
