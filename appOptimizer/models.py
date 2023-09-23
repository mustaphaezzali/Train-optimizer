from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Trajects(models.Model):
    depart = models.CharField(max_length = 100)
    arrivel = models.CharField(max_length =100)
    traject = models.TextField()

class Trajet(models.Model):
    dateDepart =models.DateField(default='2000-12-31')    
    gareDepart = models.CharField(max_length = 100,default='gare')
    timeDepart =models.TimeField(default='00:00:00')
    gareArrivel = models.CharField(max_length = 100,default='gare')
    timeArrivel = models.TimeField(default='00:00:00')
    link = models.CharField(max_length = 200)
    correspondance = models.BooleanField(default=True)
    gareDepartCorr = models.CharField(max_length = 100,null=True,blank=True)
    timeDepartCorr = models.TimeField(null=True,blank=True)
    gareArrivelCorr = models.CharField(max_length = 100,null=True,blank=True)
    timeArrivelCorr = models.TimeField(null=True,blank=True)
    linkCorr = models.CharField(max_length = 200,null=True,blank=True)
class Ticket(models.Model):
    dateDepart =models.DateField(default='2000-12-31')    
    gareDepart = models.CharField(max_length = 100,default='gare')
    timeDepart =models.TimeField(default='00:00:00')
    gareArrivel = models.CharField(max_length = 100,default='gare')
    timeArrivel = models.TimeField(default='00:00:00')
    link = models.CharField(max_length = 200)
    type = models.CharField(max_length=100,default='type')
    price = models.FloatField(default=0)
    correspondance = models.BooleanField(default=True)
    gareDepartCorr = models.CharField(max_length = 100,null=True,blank=True)
    timeDepartCorr = models.TimeField(null=True,blank=True)
    gareArrivelCorr = models.CharField(max_length = 100,null=True,blank=True)
    timeArrivelCorr = models.TimeField(null=True,blank=True)
    linkCorr = models.CharField(max_length = 200,null=True,blank=True)
    typeCorr = models.CharField(max_length=100,null=True,blank=True)
    priceCorr = models.FloatField(null=True,blank=True)


class Buffer(models.Model):
    dateDepart =models.DateField(default='2000-12-31')    
    gareDepart = models.CharField(max_length = 100,default='gare')
    timeDepart =models.TimeField(default='00:00:00')
    gareArrivel = models.CharField(max_length = 100,default='gare')
    timeArrivel = models.TimeField(default='00:00:00')
    link = models.CharField(max_length = 200)
    type = models.CharField(max_length=100,default='type')
    price = models.FloatField(default=0)
    correspondance = models.BooleanField(default=True)
    gareDepartCorr = models.CharField(max_length = 100,null=True,blank=True)
    timeDepartCorr = models.TimeField(null=True,blank=True)
    gareArrivelCorr = models.CharField(max_length = 100,null=True,blank=True)
    timeArrivelCorr = models.TimeField(null=True,blank=True)
    linkCorr = models.CharField(max_length = 200,null=True,blank=True)
    typeCorr = models.CharField(max_length=100,null=True,blank=True)
    priceCorr = models.FloatField(null=True,blank=True)
