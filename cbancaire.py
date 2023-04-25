from reseau import *
class cbancaire():
    cbs = []

    def __init__(self,reseau, nom="xx", proprietaire=None, num_carte="xx", exp="xx", cvc="xx",solde = 40.2):
        self.nom = nom
        self.proprietaire = proprietaire
        self.num_carte = num_carte
        self.exp = exp
        self.cvc = cvc
        self.reseau = reseau
        self.solde = solde
    

    def isUniqueCarte(self, num_carte):
        if len(cbancaire.cbs) == 0:
            return True
        else:
            for carte in cbancaire.cbs:
                if carte.num_carte == num_carte:
                    return False
            return True

    def isValidCarte(self):
        digits = [int(d) for d in str(self.num_carte) if d.isdigit()]
        digits.reverse()
        doubled_digits = [2 * d if i % 2 != 0 else d for i, d in enumerate(digits)]
        subtracted_digits = [d - 9 if d >= 10 else d for d in doubled_digits]
        total = sum(subtracted_digits)

        return total % 10 == 0
    
    def payer(self, montant):
        if not self.isValidCarte():
            print("Impossible de traiter le paiement. La carte bancaire est invalide.")
            return

        if montant <= 0:
            print("Le montant doit être supérieur à zéro.")
            return

        self.solde -= montant
        print(f"Paiement de {montant} € effectué avec succès avec la carte bancaire {self.num_carte}.")

    def remboursser(self,pays,prix):
        self.solde += prix*self.reseau.getrembourssement(pays)


class cbpharma(cbancaire):

    def __init__(self, reseau, nom="xx", proprietaire=None, num_carte="xx", exp="xx", cvc="xx",solde = 50.0, portefeuilles = 0.0):
        super().__init__(reseau, nom, proprietaire, num_carte, exp, cvc, solde)
        self.portefeuilles = portefeuilles

        
    def setPorteFeuille(self,montant):    
        self.portefeuilles += montant


    def payerFinMois(self):
        self.solde -= self.portefeuilles 
        self.portefeuilles = 0


if __name__ == "__main__":
    cb = cbancaire( reseau = mastercard(),nom = "lcl",proprietaire = "eee",num_carte = '123121321123',exp = '12', cvc="13")
    cb2 = cbpharma( reseau = mastercard(),nom = "lcl",proprietaire = "eee",num_carte = '123121321123',exp = '12', cvc="13")

    cb2.setPorteFeuille(15)
    print(cb2.solde)
    print(cb2.portefeuilles)
    cb2.payerFinMois()
    print(cb2.solde)
    print(cb2.portefeuilles)


