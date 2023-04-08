class Employe:
    def __init__(self, nom, prenom, adresse, salaire_fixe):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.salaire_fixe = salaire_fixe

    def __str__(self):
        return f"{self.nom}, {self.prenom}, {self.adresse}, {self.salaire_fixe}"