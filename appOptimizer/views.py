from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from functions import oncf_scraping,optimal_tickets,scraping2,confortadapt
from functions.dateformat import dateformat
from .models import Buffer, Ticket, Trajet
import psycopg2
# Create your views here.


def disponibilities(request):
    
    dateDepart=request.POST['datedepart']
    timeDepart=request.POST['heuredepart']
    gareDepart=request.POST['inputGaredepart'] 
    gareArrivel = request.POST['inputGarearrivée']
    garedepart=gareDepart
    garearrivee=gareArrivel
    confort = confortadapt.confortadapt(request.POST['btnradio'])
    conn = psycopg2.connect(
        database = 'TrainOptimizerDB', 
        user = 'postgres', 
        password = '1234',
        host = '127.0.0.1', 
        port = '5432',
    ) 
    timeDepart += ":00"
    period=oncf_scraping.periode(timeDepart)
    exist = False
    #data = Trajet.objects.all()
    cursor= conn.cursor()
    Query = 'SELECT * FROM public."appOptimizer_ticket" where ("dateDepart"=%s) and ("gareDepart"=%s) and ("timeDepart" >= %s) and (("gareArrivelCorr"=%s) OR ("gareArrivel"=%s AND correspondance=False)  )  '
    cursor.execute(Query,(dateDepart,gareDepart,timeDepart,gareArrivel,gareArrivel))
    data=cursor.fetchall()
    result=[]
    
#begun try
    for traject in data:
        result.append(traject)
        exist=True
    if exist != True:
        #scraping bloc
        dateDepart=dateDepart.split('-')
        dateDepart.reverse()
        dateDepart="/".join(dateDepart)

        list=oncf_scraping.scrap_oncf(gareDepart, gareArrivel, dateDepart, period,timeDepart)
            
        timefloat=timeDepart.split(":")
        timefloat = int(timefloat[0]) + int(timefloat[1])/60
            
        #output=optimal_tickets.select_combination(list[0][0], list[0][1], timefloat)
            
        for i in range(len(list)-1):
            corrs = optimal_tickets.select_combination(list[i][0],list[i][1],timefloat)
            for trip in corrs:
                if len(str(trip[0][1][1]))==1 :
                    continue
                if len(str(trip[2][1][1]))==1 :
                    continue  
                scraping2.scraping_voyages(trip[0],trip[2],confort)
                print('------------------->',trip)
                trip[0][6]=float((trip[0][6])[:-3])
                trip[2][6]=float((trip[2][6])[:-3])
                ticket = Ticket(dateDepart=dateformat(dateDepart),gareDepart=gareDepart,timeDepart=":".join([str(i) for i in trip[0][1]]),gareArrivel=trip[0][2],timeArrivel=":".join([str(i) for i in trip[0][3]]),link=trip[0][4],type=trip[0][5],price=trip[0][6],gareDepartCorr=trip[2][0],timeDepartCorr=":".join([str(i) for i in trip[2][1]]),gareArrivelCorr=trip[2][2],timeArrivelCorr=":".join([str(i) for i in trip[2][3]]),linkCorr=trip[2][4],typeCorr=trip[2][5],priceCorr=trip[2][6])
                ticket
                result.append(ticket)
                ticket.save()
        corrs1=list[-1] 
        for trip in corrs1:
            print(trip)
            scraping2.scraping_direct(trip,confort)
            print(trip)
            """ trip[6]=10 """
            traject = Ticket(dateDepart=dateformat(dateDepart),gareDepart=gareDepart,timeDepart=trip[1],gareArrivel=trip[2],timeArrivel=trip[3],link=trip[4],type=trip[5],price=trip[6],correspondance=False)
            result.append(traject)
            traject.save()
            #end of scraping data


    Buffer.objects.all().delete()  
    for row in result:
        row1=Buffer(dateDepart=row[1],gareDepart=row[2],timeDepart=row[3],gareArrivel=row[4],timeArrivel=row[5],link=row[6],type=row[7],price=row[8],correspondance=row[9],gareDepartCorr=row[10],timeDepartCorr=row[11],gareArrivelCorr=row[12],timeArrivelCorr=row[13],linkCorr=row[14],typeCorr=row[15],priceCorr=row[16])
        row1.save()

    if result==[]:
        return render(request,'error.html')



    #return HttpResponse(result)
    return render(request,'recherche.html',{'result':result,'gareDepart':garedepart,'gareArrivel':garearrivee,'confort':dateformat(confort)})
    #return render(request, "disponibilities.html")


def filter(request):
    priorité=request.POST["priorité"]
    gamme=request.POST["gamme"]
    corr=request.POST["corr"]
    
    conn = psycopg2.connect(
        database = 'TrainOptimizerDB', 
        user = 'postgres', 
        password = '1234',
        host = '127.0.0.1', 
        port = '5432',
    ) 
    cursor= conn.cursor()
    
    if priorité == "Prix":
        if gamme == "Tous":
            if corr == "Tous les trains":
                Query = 'SELECT * FROM public."appOptimizer_buffer"  order by "price"+"priceCorr"'
                cursor.execute(Query)
            elif corr == "Directe":
                Query = 'SELECT * FROM public."appOptimizer_buffer"  where "correspondance"=False order by "price"+"priceCorr"'
                cursor.execute(Query)
            else:
                Query = 'SELECT * FROM public."appOptimizer_buffer"  where "correspondance" = True order by "price"+"priceCorr"'
                cursor.execute(Query)

        else:
            Query = 'SELECT * FROM public."appOptimizer_buffer"  where "type"=%s or "typeCorr"=%s order by "price"+"priceCorr"'
            cursor.execute(Query,(gamme,gamme))
    else:
        if gamme== "Tous":
            if corr == "Tous les trains":
                 Query = 'SELECT * FROM public."appOptimizer_buffer"  order by "timeDepart"'
                 cursor.execute(Query)
            elif corr == "Directe":
                Query = 'SELECT * FROM public."appOptimizer_buffer"  where "correspondance"=false order by "timeDepart"'
                cursor.execute(Query)
            else:
                Query = 'SELECT * FROM public."appOptimizer_buffer"  where "correspondance" = True order by "timeDepart"'
                cursor.execute(Query)
        else:
            Query = 'SELECT * FROM public."appOptimizer_buffer"  where "type"=%s or "typeCorr"=%s order by "timeDepart"'
            cursor.execute(Query,(gamme,gamme))

    data=cursor.fetchall()
    print("---------------------->",data)
    if data == []:
        return HttpResponse("ERROR :not found")        
    if data[0][9]==True:
        garearrivee=data[0][12]
    else:
        garearrivee=data[0][4]
    

    return render(request,'recherche.html',{'result':data,'gareDepart':data[0][2],'gareArrivel':garearrivee,'confort':"confort"})



def home(request):
    return render(request, 'home.html')


