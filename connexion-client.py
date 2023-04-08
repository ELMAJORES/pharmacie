import csv
class connexion_client(object):
	def __init__(self, nom = "xxx",prenom = "xxx"):
		self.nom = nom
		self.prenom = prenom

	def connect(self):
		reader = csv.DictReader(open(r"C:\Users\tlemc\OneDrive\Bureau\pharma/data2.csv"))
		for raw in reader:
			if raw["nom"] == self.nom and raw["prenom"] == self.prenom:
				return True

		return False




if __name__ == "__main__":
	connexion = connexion_client("tlemcani","abdelhak")
	print(connexion.connect())