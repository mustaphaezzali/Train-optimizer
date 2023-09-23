

# voici notre trajet principale :



general_path = ["MARRAKECH","BENGUERIR","SETTAT","BERRECHID","CASA OASIS","CASA VOYAGEUR",
                "AIN SBAA","MOHAMMEDIA","BOUZNIKA","SKHIRAT","TEMARA","RABAT AGDAL","RABAT VILLE","SALE","KENITRA","SIDI SLIMANE MEDINA",
                "SIDI KACEM", "MEKNES", "AIN TAOUJTATE", "FES", "OUED AMLIL", "TAZA", "GUERCIF", "TAOURIRT",
                "OUED METLILI", "EL AIOUN", "OUJDA"]



def direct_pivot_ville_auxiliaire(city):
    
    if city in ["EL ARIA", "YOUSSOUFIA", "BIDANE","BOUGUEDRA", "SAFI"]:
        
        return "BENGUERIR"
    
    elif city in ["SIDI EL AIDI", "TAMDROST", "MOUALINE EL OUED", "RAS EL AIN", "SIDI HAJAJ","KHOURIBGA", "OUED ZEM"]:
        
        return "BERRECHID"
    
    elif city in ["ENNASSIM","BOUSKOURA","AZEMMOUR","EL JADIDA"]:
        
        return "CASA OASIS"
    
    elif city in ["MECHRAA BEL KSIRI", "SOUK EL ARBAA","EL KSAR EL KEBIR", "ASILAH", "TANGER"]:
        
        return "SIDI KACEM"
    
    elif city in ["MELG EL OUIDANE", "HASSI BERKANE", "NADOR SUD", "NADOR"]:
        
        return "TAOURIRT"
    
    else :
        
        return city

        

def pivot_choice(city, ville_auxiliaire):
    
    #determiner le pivot d'une ville qui ne figure pas dans le trajet general:
    
    final_list = []

    
   
    temp = []
    
    if city in ["EL ARIA", "YOUSSOUFIA", "BIDANE","BOUGUEDRA", "SAFI"]:
        
        temp = ["EL ARIA", "YOUSSOUFIA", "BIDANE","BOUGUEDRA", "SAFI"]
            
        temp_index = temp.index(city)
        
        final_list = temp[:temp_index+1]
            
        return "BENGUERIR", final_list
        
    elif city in ["SIDI EL AIDI", "TAMDROST", "MOUALINE EL OUED", "RAS EL AIN", "SIDI HAJAJ","KHOURIBGA", "OUED ZEM"]:
        
        temp = ["SIDI EL AIDI", "TAMDROST", "MOUALINE EL OUED", "RAS EL AIN", "SIDI HAJAJ","KHOURIBGA", "OUED ZEM"]

        temp_index = temp.index(city)
        
        final_list = temp[:temp_index+1]
            
        return "BERRECHID", final_list

    elif city in ["ENNASSIM","BOUSKOURA","AZEMMOUR","EL JADIDA"]:
        
        pivot_ville_auxiliare = direct_pivot_ville_auxiliaire(ville_auxiliaire)
        
        if general_path.index(pivot_ville_auxiliare) < general_path.index("CASA OASIS") :
        
            temp = ["ENNASSIM","BOUSKOURA","AZEMMOUR","EL JADIDA"]
                
            temp_index = temp.index(city)
        
            final_list = temp[:temp_index+1]
                
            return "CASA OASIS", final_list

        elif general_path.index(pivot_ville_auxiliare) > general_path.index("CASA OASIS") and general_path.index(pivot_ville_auxiliare) < general_path.index("KENITRA") :
            
            temp = ["CASA PORT","CASA VOYAGEUR","CASA OASIS","ENNASSIM","BOUSKOURA","AZEMMOUR","EL JADIDA"]
                
            temp_index = temp.index(city)
        
            final_list = temp[:temp_index+1]
                
            return "AIN SBAA", final_list
            
        else :
                
            temp = ["ENNASSIM", "BOUSKOURA", "AZEMMOUR", "EL JADIDA"]

            temp_index = temp.index(city)
        
            final_list = temp[:temp_index+1]
                
            return "CASA OASIS", final_list


    elif city in ["MECHRAA BEL KSIRI", "SOUK EL ARBAA","EL KSAR EL KEBIR", "ASILAH", "TANGER"]:

        pivot_ville_auxiliare = direct_pivot_ville_auxiliaire(ville_auxiliaire)
        
        if general_path.index(pivot_ville_auxiliare) < general_path.index("KENITRA"):
                
            temp = ["MECHRAA BEL KSIRI", "SOUK EL ARBAA","EL KSAR EL KEBIR", "ASILAH", "TANGER"]
                
            temp_index = temp.index(city)
        
            final_list = temp[:temp_index+1]
            
            return "KENITRA", final_list
            
        else :
                
            temp = ["MECHRAA BEL KSIRI", "SOUK EL ARBAA","EL KSAR EL KEBIR", "ASILAH", "TANGER"]
                
            temp_index = temp.index(city)
                
            final_list = temp[:temp_index+1]
                
            return "SIDI KACEM"

        
    elif city in ["MELG EL OUIDANE", "HASSI BERKANE", "NADOR SUD", "NADOR"]:
        
        temp = ["MELG EL OUIDANE", "HASSI BERKANE", "NADOR SUD", "NADOR"]
            
        temp_index = temp.index(city)
        
        final_list = temp[:temp_index+1]
            
        return "TAOURIRT", final_list
            
    else :
        return None ,final_list
        
    
    

    
def reverse_path(general_list,result_list, pivot_depart, pivot_arrivée):
    
    # fonction qui va nous permettre de changer le sens de notre liste de recherche
    
    if general_list.index(pivot_depart) > general_list.index(pivot_arrivée): 
        result_list.reverse()
      
    return None
        


def path_choice(ville_depart, ville_arrivée): 
    
    # fonction qui permet de retourner le trajet de train selon les villes saisis 
    
    pivot_depart, trajet_depart = pivot_choice(ville_depart, ville_arrivée)
    pivot_arrivée, trajet_arrivée = pivot_choice(ville_arrivée, ville_depart)
    
    #cas si les villes saisis font partie du trajet general :
    
    if pivot_depart == None and pivot_arrivée != None :
        
        pivot_depart =ville_depart
        
    elif pivot_arrivée == None and pivot_depart != None:
        
        pivot_arrivée = ville_arrivée
    
    elif pivot_depart == None and pivot_arrivée == None :
        
        pivot_depart = ville_depart
        pivot_arrivée = ville_arrivée
    
        
    index_pivot_depart, index_pivot_arrivée = general_path.index(pivot_depart), general_path.index(pivot_arrivée)
    
    
    i, j = min(index_pivot_depart,index_pivot_arrivée), max(index_pivot_depart,index_pivot_arrivée)
    
    temp_path = general_path[i:j+1]
    
    reverse_path(general_path, temp_path, pivot_depart, pivot_arrivée) # choix de sens de trajet
    
    #verification pour ne pas ajouter une ville qui est deja un pivot !
    
    trajet_depart.reverse()
    
    if pivot_depart == ville_depart and pivot_arrivée != ville_arrivée :    
    
        temp_path = temp_path + trajet_arrivée
    
    elif pivot_depart != ville_depart and pivot_arrivée == ville_arrivée :
        
        
        temp_path = trajet_depart + temp_path   
            
    elif pivot_depart != ville_depart and pivot_arrivée != ville_arrivée :
    
        temp_path = trajet_depart + temp_path + trajet_arrivée
    
    return temp_path 




 


    









                
                
    
    










