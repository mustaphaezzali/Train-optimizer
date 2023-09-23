'''this code is an update to the previous optimal_tickets created by Taif , 
   in order to make it compatible with the scraped data '''

def split_traject(trajectories,arrivé):
    '''this code take as input the scraped list;trajectories and split this list into paths , ila mafhmtich hadchi hanya'''
    trajects=[]
    while trajectories!=[]:
        traject=[]
        while trajectories[0][0][2]!=arrivé:
            traject.append(trajectories.pop(0))
        traject.append(trajectories.pop(0))
        trajects.append(traject)
    return trajects
    

def stringlist_to_intlist(list):
    
    #let's convert the string list to int list 
    T = []
    L = []
    for i in range(0, len(list)):
        if list == []:
            return []
        else:
            L = [list[i][0],list[i][1].split(":"),list[i][2], list[i][3].split(":"),list[i][4] ]
            
            res =[L[0],[int(x) for x in L[1]],L[2],[int(x) for x in L[3]], L[4]]
            T.append([res[0],[res[1][0], res[1][1]],res[2],[res[3][0], res[3][1]], res[4]])
        
    #print(T)
    
    #lets convert the list to hours
    L = []
    for k in T:
        temp = [k[0]]
        heure_depart = k[1][0] + k[1][1]/60
        temp.append(round(heure_depart,2))
        temp.append(k[2])
        heure_arrivée = k[3][0] + k[3][1]/60
        temp.append(round(heure_arrivée,2))
        
        temp.append(k[4])
        L.append(temp)
        
    return L






from operator import itemgetter

def time_select(heure_depart, list):
    
    # sorting the list to times that are the closest to the wanted user value
        
    temp_list = list.copy()
    
    for k in temp_list :
        
        #making a list of the time difference between the wanted time and the available time
        
        diff_temp = abs(k[1] - heure_depart)
        
        k[1] = diff_temp
        
        
    # sorting the list via the difference time
        
    T = sorted(temp_list, key = itemgetter(1))
    
    
    
    for k in T :
    
        # we add back the difference(wanted time) the difference list
        
        if (k[1] + heure_depart) > k[3]  : 
            
            temp_var = heure_depart - k[1]
            
            k[1] = temp_var
            
        else :
            
            temp_var = heure_depart + k[1]
            
            k[1] = temp_var
        
    return T




def select_combination(path_deal_1, path_deal_2, heure_depart):
    
    #converting the scraped values to usable lists (int values)
    
    list_1 = time_select(heure_depart,stringlist_to_intlist(path_deal_1))
    
    list_2 = time_select(int(time_select(heure_depart,stringlist_to_intlist(path_deal_1))[0][3]), stringlist_to_intlist(path_deal_2))

    
    final_list = []

    list_1_sorted = sorted(list_1, key = itemgetter(1))
    
    # removing times that are prior to the wanted time by the user 
    
    for l in list_1_sorted:
        
        if (l[1] < heure_depart):
            
            list_1_sorted.pop(list_1_sorted.index(l)) 
        
    
    for k in list_1_sorted :
    
        # converting the time from hours to hours&minutes 
        
        hours_k_1 = int(k[1])
        minutes_k_1 = round((k[1]*60) % 60)
                    
        temp_1 = [hours_k_1, minutes_k_1]
                    
        hours_k_2 = int(k[3])
        minutes_k_2 = round((k[3]*60) % 60)
                    
        temp_2 = [hours_k_2, minutes_k_2]
                    
        temp_final_k = [k[0],temp_1,k[2],temp_2, k[4]]
        
        for j in list_2:
            
            # lets test the available combinations :
            
            temp2 = []
            
            if (j[1] - k[3]) > (0.25) and (j[1] - k[3]) < 1:
                
                """
                0.25 : minimum waiting time in hours 
                
                1 : maximum waiting time in hours 
                
                **we can make it a parameter ?!
                
                """
                temp2.append(temp_final_k)
                var = "---->"
                temp2.append(var)
                
                    
                #converting hours to hours&minutes               
                
                hours_j_1 = int(j[1])
                minutes_j_1 = round((j[1]*60) % 60)
                    
                temp_j_1 = [hours_j_1, minutes_j_1]
                    
                hours_j_2 = int(j[3])
                minutes_j_2 = round((j[3]*60) % 60)
                    
                temp_j_2 = [hours_j_2, minutes_j_2]
                    
                temp_final_j = [j[0],temp_j_1,j[2],temp_j_2, j[4]]

                temp2.append(temp_final_j)
    
                final_list.append(temp2)
                
        
    
    return final_list