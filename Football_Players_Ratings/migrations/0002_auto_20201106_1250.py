# Generated by Django 3.1.3 on 2020-11-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Football_Players_Ratings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zawodnik',
            name='Fotografia',
            field=models.ImageField(blank=True, null=True, upload_to='fotografie zawodnikow'),
        ),
        migrations.AlterField(
            model_name='zawodnik',
            name='Pozycja_na_boisku',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Środkowy ofensywny pomocnik'), (1, 'Środkowy obrońca'), (2, 'Boczny obrońca'), (0, 'Bramkarz'), (7, 'Napastnik'), (5, 'Boczny pomocnik'), (3, 'Środkowy defensywny pomocnik'), (6, 'Wahadłowy')]),
        ),
    ]