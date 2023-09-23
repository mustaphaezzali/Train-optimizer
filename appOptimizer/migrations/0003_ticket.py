# Generated by Django 4.0.4 on 2022-06-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOptimizer', '0002_alter_trajet_garearrivelcorr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDepart', models.DateField(default='2000-12-31')),
                ('gareDepart', models.CharField(default='gare', max_length=100)),
                ('timeDepart', models.TimeField(default='00:00:00')),
                ('gareArrivel', models.CharField(default='gare', max_length=100)),
                ('timeArrivel', models.TimeField(default='00:00:00')),
                ('link', models.CharField(max_length=200)),
                ('type', models.CharField(default='type', max_length=100)),
                ('price', models.FloatField(default=0)),
                ('correspondance', models.BooleanField(default=True)),
                ('gareDepartCorr', models.CharField(blank=True, max_length=100, null=True)),
                ('timeDepartCorr', models.TimeField(blank=True, null=True)),
                ('gareArrivelCorr', models.CharField(blank=True, max_length=100, null=True)),
                ('timeArrivelCorr', models.TimeField(blank=True, null=True)),
                ('linkCorr', models.CharField(blank=True, max_length=200, null=True)),
                ('typeCorr', models.CharField(blank=True, max_length=100, null=True)),
                ('priceCorr', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]