graph = {
    "TANGER" : {"KENITRA"},
    "KENITRA" :{"RABAT AGDAL","MEKNES","TANGER"},
    "RABAT AGDAL":{"KENITRA","CASA VOYAGEURS"},
    "CASA VOYAGEURS":{"RABAT AGDAL","JDIDA", "SETTAT"},
    "JDIDA":{"CASA VOYAGEURS", "SETTAT"},
    "SETTAT":{"CASA VOYAGEURS","JDIDA","BENGUERIR","OUED ZEM"},
    "BENGUERIR":{"SETTAT","SAFI","MARRAKECH"},
    "SAFI":{"BENGUERIR"},
    "MARRAKECH":{"BENGUERIR"},
    "OUED ZEM" : {"SETTAT"},
    "MEKNES":{"FES","KENITRA"},
    "FES":{"MEKNES","TAZA"},
    "TAZA":{"FES","OUJDA","NADOR"},
    "OUJDA":{"TAZA"},
    "NADOR":{"TAZA"}
}

def shortest_path(graph, depart, arrivee):

    explored = []
    queue = [[depart]]
    if depart == arrivee:
        return
     
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        if node not in explored:
            neighbours = graph[node]
             
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                if neighbour == arrivee:
                    return new_path
            explored.append(node)
    return


