class ResponsablePharmacie(Employe):
    def __init__(self, nom, prenom, adresse, salaire_fixe, anciennete, bonus):
        super().__init__(nom, prenom, adresse, salaire_fixe)
        self.anciennete = anciennete
        self.bonus = bonus

    def calculer_salaire(self):
        prime_anciennete = 0.05 * self.salaire_fixe * self.anciennete
        return self.salaire_fixe + prime_anciennete + self.bonus

    def calculer_bonus(self, chiffre_affaires):
        if chiffre_affaires < 10000:
            return 0
        elif 10000 <= chiffre_affaires < 20000:
            return 500
        else:
            return 1000