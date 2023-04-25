class reseau(object):

    def __init__(self,nomReseau = "xx",coutReseau=0.0,tauxRembourssement=0.0):
        self.nomReseau = nomReseau
        self.coutReseau = coutReseau
        self.tauxRembourssement = tauxRembourssement

class mastercard(reseau):

    def __init__(self):
        super().__init__("mastercard",0.5,1)

    def getrembourssement(self,pays = "xx"):
        return self.tauxRembourssement
    
class visa(reseau):
    
    def __init__(self):
        super().__init__("visa", 0.25,1)
        self.paysRembourssement = {
            "Espagne" : 0.0010,
            "Etats-Unis" : 0.0020,
            "Portugal" : 0.0015,
            "Royaume-Uni" : 0.0025,
            "Reste du monde" : 0.0030
        }
        
        
    def getrembourssement(self,pays):
        return self.tauxRembourssement-self.paysRembourssement[pays]
    
if __name__ == "__main__":
    master = mastercard()
    print(master.getrembourssement("Royaume-Uni"))


