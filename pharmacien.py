class Pharmacien(Employe):
    def __init__(self, nom, prenom, adresse, salaire_fixe):
        super().__init__(nom, prenom, adresse, salaire_fixe)

    def calculer_prime(self, chiffre_affaires):
        return chiffre_affaires * 0.01

if __name__ == "__main__":
    pass