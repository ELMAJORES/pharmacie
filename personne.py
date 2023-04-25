from cbancaire import * 
class personne():

    def __init__(self,carteBancaire1 ,carteBancaire2,nom = "xx",prenom = "xx",date_naissance = "xx"):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.carteBancaire1 = carteBancaire1
        self.carteBancaire2 = carteBancaire2

    def payer(self,montant):
        print(self.carteBancaire2.payer(montant))
    def contesterPayment():
        return True
    

if __name__ == "__main__":
    
    pers = personne( carteBancaire1=cbancaire(visa()),carteBancaire2=cbpharma(mastercard()),nom = "tlemcani",prenom = "abdelhak",date_naissance="1207")
    pers.payer(5)
    print(pers.carteBancaire2.solde)
    print(pers.carteBancaire2.portefeuilles)