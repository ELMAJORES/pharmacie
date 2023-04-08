class PreparateurCommande(Employe):
    def __init__(self, nom, prenom, adresse, salaire_fixe, duree_anciennete):
        super().__init__(nom, prenom, adresse, salaire_fixe)
        self.duree_anciennete = duree_anciennete

    def calculer_salaire(self):
        if self.duree_anciennete < 3:
            return self.salaire_fixe
        elif 3 <= self.duree_anciennete < 6:
            return self.salaire_fixe * 1.1
        else:
            return self.salaire_fixe * 1.
    

if __name__ == "__main__":
    pass