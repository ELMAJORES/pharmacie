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

if __name__ == "__main__":
    pass