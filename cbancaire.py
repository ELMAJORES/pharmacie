class cbancaire():

    def __init__(self,nom = "xx",propietaire = "xx",num_carte = "xx",exp = "xx", cvc = "xx"):
        self.nom = nom
        self.propietaire = propietaire
        self.num_carte = num_carte
        self.exp = exp
        self.cvc = cvc

    def creationCarte(self):
        with open("resources/cb.txt","a") as f:
            if self.verificationCarte():
                f.write(self.nom+","+self.propietaire+","+self.num_carte+","+self.exp+","+self.cvc+"\n")
                return True
        return False

    def verificationCarte(self):
        with open("resources/cb.txt","r") as f:
            v = f.readlines()
            for i in v:
                i = i.split(",")
                if i[2] == self.num_carte:
                    return False
        return True
if __name__ == "__main__":
    cb = cbancaire("tlemcani","abdelhak","106065","1206","058")
    cb.creationCarte()
    cb2 = cbancaire("tlemcani","abdelhak","024220","2020","058")
    cb2.creationCarte()
