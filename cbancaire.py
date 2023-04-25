class cbancaire():
    cbs = []

    def __init__(self, nom="xx", proprietaire=None, num_carte="xx", exp="xx", cvc="xx"):
        self.nom = nom
        self.proprietaire = proprietaire
        self.num_carte = num_carte
        self.exp = exp
        self.cvc = cvc

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


        print(f"Paiement de {montant} € effectué avec succès avec la carte bancaire {self.num_carte}.")

if __name__ == "__main__":
    pass



