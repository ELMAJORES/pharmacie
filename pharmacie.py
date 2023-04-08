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