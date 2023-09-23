def confortadapt(confort):
    if confort == "classe1":
        confort="1èreclasse"
    elif confort == "classe2":
        confort="2èmeclasse"        
    else:
        confort = "Lit single"
    return confort    