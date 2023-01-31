class Medicament:
  def __init__(self, reference, prix):
    self.reference = reference
    self.prix = prix
  
  def __str__(self):
    return f"Reference: {self.reference}, Prix: {self.prix}"
  
  def set_reference(self, reference):
    self.reference = reference
  
  def set_prix(self, prix):
    self.prix = prix
  
  def get_reference(self):
    return self.reference
  
  def get_prix(self):
    return self.prix

class Pharmacie:
  def __init__(self):
    self.stock = {}
  
  def ajouter_medicament(self, medicament):
    self.stock[medicament.get_reference()] = medicament.get_prix()
  
  def afficher_stock(self):
    for reference, prix in self.stock.items():
      print(f"Reference: {reference}, Prix: {prix}")
      
  def enregistrer_stock(self):
    with open("stock.txt", "w") as f:
      for reference, prix in self.stock.items():
        f.write(f"{reference},{prix}\n")

def main():
  pharmacie = Pharmacie()
  while True:
    print("--- Menu ---")
    print("1. Ajouter un médicament")
    print("2. Afficher le stock")
    print("3. Enregistrer le stock")
    print("4. Quitter")
    choix = input("Choisissez une option (1-4) : ")
    if choix == "1":
      reference = input("Reference : ")
      prix = float(input("Prix : "))
      medicament = Medicament(reference, prix)
      pharmacie.ajouter_medicament(medicament)
    elif choix == "2":
      pharmacie.afficher_stock()
    elif choix == "3":
      pharmacie.enregistrer_stock()
    elif choix == "4":
      break
    else:
      print("Option non valide.")

if __name__ == "__main__":
  main()
