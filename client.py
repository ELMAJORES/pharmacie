import csv
class Client(object):
	def __init__(self, nom = "xxx",prenom = "xxx", age = "xx"):
		self.nom = nom
		self.prenom = prenom
		self.age = age

	def connect(self, path):
		reader = csv.DictReader(open(path))
		for raw in reader:
			if raw["nom"] == self.nom and raw["prenom"] == self.prenom:
				return True

		return False
		
	def addClient(self,path):
		with open(path, 'a', newline='') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow([self.nom]+[self.prenom]+[self.age])






if __name__ == "__main__":
	connexion = Client("tlemcani","sa","16")
	new_client = [{"nom" : ["tlemcani","bouazouni","mohand"],
				   "prenom" : ["abdelhak","walid","mohamed"] }]
	print(connexion.addClient(path = "resources/clients.csv"))