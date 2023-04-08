import csv
class Client(object):
	def __init__(self, nom = "xxx",prenom = "xxx"):
		self.nom = nom
		self.prenom = prenom

	def connect(self, path):
		reader = csv.DictReader(open(path))
		for raw in reader:
			if raw["nom"] == self.nom and raw["prenom"] == self.prenom:
				return True

		return False




if __name__ == "__main__":
	connexion = Client("tlemcani","aladin")
	print(connexion.connect(path = "resources/clients.csv"))