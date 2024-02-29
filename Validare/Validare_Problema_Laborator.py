from Erori.Erori_problema_laborator import ValidatorPbError


class ValidatorPb(object):
    def valideaza(self,problema):
        erori=""
        s=problema.get_nr()
        if s[0]<=0:
            erori+="Numar laborator invalid\n"
        if s[1]<=0:
            erori+="Numar problema invalid\n"
        if type(problema.get_descriere())==int or len(problema.get_descriere())==0:
            erori+="Nu a fost introdusa descrierea\n"
        deadline = problema.get_deadline()
        deadline.strip()
        partid = deadline.split("/")
        if len(problema.get_deadline()) == 0:
            erori += "Nu a fost introdus un deadline\n"
        else:
            if len(partid) >= 1 and (int(partid[0]) <= 0 or int(partid[0]) >= 32):
                erori += "Ziua deadline invalida\n"
            if len(partid) >= 2 and (int(partid[1]) <= 0 or int(partid[1]) >= 13):
                erori += "Luna deadline invalida\n"
            if len(partid) >= 3 and (int(partid[2]) <= 0 or int(partid[2]) > 3000):
                erori += "An deadline invalid\n"
        if len(erori)>0:
            raise ValidatorPbError(erori)
