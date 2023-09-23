def dateformat(date):
    date=date.split('/')
    date.reverse()
    date='-'.join(date)
    return date

print(dateformat("06/06/2022"))    


""" conditon1=((traject.dateDepart).strftime("%m/%d/%Y") == dateDepart)
        conditon2= ((traject.timeDepart).strftime("%H:%M:%S") == timeDepart)
        conditon3=(traject.gareDepart == gareDepart)
        if traject.correspondance:
            conditon4=(traject.gareArrivelCorr == gareArrivel)
        else:
            conditon4=(traject.gareArrivel == gareArrivel)
        if conditon1 & conditon2 & conditon3 & conditon4:
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
                traject = Trajet(dateDepart=dateformat(dateDepart),gareDepart=gareDepart,timeDepart=":".join([str(i) for i in trip[0][1]]),gareArrivel=trip[0][2],timeArrivel=":".join([str(i) for i in trip[0][3]]),link=trip[0][4],gareDepartCorr=trip[2][0],timeDepartCorr=":".join([str(i) for i in trip[2][1]]),gareArrivelCorr=trip[2][2],timeArrivelCorr=":".join([str(i) for i in trip[2][3]]),linkCorr=trip[2][4])
                result.append(traject)
                traject.save()
        corrs1=list[-1]
        for trip in corrs1:
            traject = Trajet(dateDepart=dateformat(dateDepart),gareDepart=gareDepart,timeDepart=trip[1],gareArrivel=trip[2],timeArrivel=trip[3],link=trip[4],correspondance=False)
            result.append(traject)
            traject.save()
            #end of scraping data """