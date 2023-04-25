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
            "Espagne" : 0.10,
            "Etats-Unis" : 0.20,
            "Portugal" : 0.15,
            "Royaume-Uni" : 0.25,
            "Reste du monde" : 0.30
        }
        
        
    def getrembourssement(self,pays):
        return self.tauxRembourssement-self.paysRembourssement[pays]
    
if __name__ == "__main__":
    master = mastercard()
    print(master.getrembourssement("Royaume-Uni"))


