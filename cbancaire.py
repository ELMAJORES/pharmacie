class cbancaire():

    cbs = []


    def __init__(self,nom = "xx", proprietaire = None,num_carte = "xx",exp = "xx", cvc = "xx"):
        self.nom = nom
        self.proprietaire = proprietaire
        self.num_carte = num_carte
        self.exp = exp
        self.cvc = cvc


    def isUniqueCarte(self,num_carte):
        if len(cbancaire.cbs) == 0:
            return True
        else:
            for carte in cbancaire.cbs:
                if carte.num_carte == num_carte:
                    return False
            return True 
                

if __name__ == "__main__":
    pass
"""    cb = cbancaire("xx","cx","cc","xx")
    if cb.isUniqueCarte(cb.num_carte):
        print("oui")
        cbancaire.cbs.append(cb)
    else:
        print("non") 
    
    cb1 = cbancaire("xx","efzcafvd","csdhjgavj","xx")
    if cb1.isUniqueCarte(cb1.num_carte):
        print("oui")
        cbancaire.cbs.append(cb1)
    else:
        print("non") 
    

    cb2 = cbancaire("xx","cx","cc","xx")
    if cb2.isUniqueCarte(cb2.num_carte):
        print("oui")
        cbancaire.cbs.append(cb2)
    else:
        print("non") """