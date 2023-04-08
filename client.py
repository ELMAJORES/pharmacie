class Produit:
    def __init__(self, nom_generique, produit_type, prix_achat, prix_vente, date_peremption):
        self.nom_generique = nom_generique
        self.produit_type = produit_type
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.date_peremption = date_peremption
        self.pharmacies = []

    def add_pharmacie(self, pharmacie):
        self.pharmacies.append(pharmacie)

    def remove_pharmacie(self, pharmacie):
        self.pharmacies.remove(pharmacie)

    def __str__(self):
        return f"{self.nom_generique}, {self.produit_type}, {self.prix_achat}, {self.prix_vente}, {self.date_peremption}"


class Pharmacie:
    def __init__(self, nom, nombre_employes, surface_commerciale, siret=None):
        self.nom = nom
        self.nombre_employes = nombre_employes
        self.surface_commerciale = surface_commerciale
        self.siret = siret
        self.employes = []
        self.produits = []

    def add_employe(self, employe):
        self.employes.append(employe)

    def remove_employe(self, employe):
        self.employes.remove(employe)

    def add_produit(self, produit):
        self.produits.append(produit)
        produit.add_pharmacie(self)

    def remove_produit(self, produit):
        self.produits.remove(produit)
        produit.remove_pharmacie(self)

    def __str__(self):
        return f"{self.nom}, {self.nombre_employes}, {self.surface_commerciale}, {self.siret}"


class Employe:
    def __init__(self, nom, prenom, adresse, salaire_fixe):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.salaire_fixe = salaire_fixe

    def __str__(self):
        return f"{self.nom}, {self.prenom}, {self.adresse}, {self.salaire_fixe}"


class Pharmacien(Employe):
    def __init__(self, nom, prenom, adresse, salaire_fixe):
        super().__init__(nom, prenom, adresse, salaire_fixe)

    def calculer_prime(self, chiffre_affaires):
        return chiffre_affaires * 0.01


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