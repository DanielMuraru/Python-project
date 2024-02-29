from Business.Service_problema_laborator import ServiceProbleme
from Domain.Problema_laborator import Problema
from Erori.Erori_problema_laborator import ValidatorPbError, RepoPbError
from Persistenta.RepoProblema_file import Repopb_file
from Persistenta.RepoProblema_laborator import RepoProbleme
from Validare.Validare_Problema_Laborator import ValidatorPb


class Teste_Lab(object):
    def __init__(self):
        self.__nr=(1,3)
        self.__descriere="Nota 10"
        self.__deadline="12/12/2022"
        self.__problema=Problema(self.__nr,self.__descriere,self.__deadline)
    def goleste_fisier(self,fisier):
        with open(fisier,"w") as f:
            pass
    def __run_teste_domain(self):
        assert(self.__problema.get_nr()==(1,3))
        assert(self.__problema.get_descriere()=="Nota 10")
        assert(self.__deadline=="12/12/2022")
        clone_pb=Problema((1,3),None,None)
        assert(self.__problema==clone_pb)
        assert(self.__problema.get_nr()==clone_pb.get_nr())
        assert(str(self.__problema)=="(1, 3)  Nota 10  12/12/2022")

    def __run_teste_validator(self):
        self.__validator_pb=ValidatorPb()
        self.__nr_nou=(2,5)
        self.__descriere_noua="Nota 7"
        self.__deadline_nou="25/11/2022"
        self.__problema_de_validat=Problema(self.__nr_nou,self.__descriere_noua,self.__deadline_nou)
        self.__validator_pb.valideaza(self.__problema_de_validat)

        self.__nr_nou=(-11,0)
        self.__descriere_noua = ""
        self.__deadline_nou = ""
        self.__problema_de_validat = Problema(self.__nr_nou, self.__descriere_noua, self.__deadline_nou)
        try:
            self.__validator_pb.valideaza(self.__problema_de_validat)
            assert False
        except ValidatorPbError as ve:
            assert(str(ve)=="Numar laborator invalid\nNumar problema invalid\nNu a fost introdusa descrierea\nNu a fost introdus un deadline\n")

    def __run_teste_repo_pb(self):
        self.__repopb=RepoProbleme()
        assert(len(self.__repopb)==0)
        self.__nr_nou=(2,5)
        self.__descriere_noua = "Nota 7"
        self.__deadline_nou = "25/11/2022"
        self.__pb_de_adaugat=Problema(self.__nr_nou,self.__descriere_noua,self.__deadline_nou)
        self.__repopb.adauga_pb(self.__pb_de_adaugat)
        assert (len(self.__repopb) == 1)

        self.__acelasi_nr = (2, 5)
        self.__descriere_noua = "Nota 7"
        self.__deadline_nou = "25/11/2022"
        self.__pb_de_adaugat = Problema(self.__acelasi_nr, self.__descriere_noua, self.__deadline_nou)
        try:
            self.__repopb.adauga_pb(self.__pb_de_adaugat)
            assert False
        except RepoPbError as re:
            assert(str(re)=="Problema laborator existenta")

        self.__nr_nou=3
        try:
            self.__repopb.cauta_pb(self.__nr_nou)
        except RepoPbError as re:
            assert(str(re)=="Problema laborator inexistenta")

        self.__acelasi_nr = (2, 5)
        self.__descriere_noua = "Nota 9"
        self.__deadline_nou = "25/12/2022"
        self.__pb_de_modificat=Problema(self.__acelasi_nr,self.__descriere_noua,self.__deadline_nou)
        self.__repopb.modifica_pb(self.__pb_de_modificat)
        assert(len(self.__repopb)==1)
        pb_gasita=self.__repopb.cauta_pb(self.__acelasi_nr)
        assert(pb_gasita.get_descriere()==self.__descriere_noua)

        self.__acelasi_nr=(2,5)
        assert (len(self.__repopb) == 1)
        self.__repopb.sterge_pb(self.__acelasi_nr)
        assert (len(self.__repopb) == 0)

    def __run_teste_service_pb(self):
        self.__repopb=Repopb_file("Teste/probleme.txt")
        self.__validator_pb=ValidatorPb()
        self.__servicepb= ServiceProbleme(self.__repopb,self.__validator_pb)
        self.goleste_fisier("Teste/probleme.txt")
        assert (len(self.__servicepb) == 0)
        self.__nr_nou = (2, 5)
        self.__descriere_noua = "Nota 7"
        self.__deadline_nou = "25/11/2022"
        self.__servicepb.adauga_pb_service(self.__nr_nou,self.__descriere_noua,self.__deadline_nou)
        assert (len(self.__servicepb) == 1)

        self.__acelasi_nr = (2, 5)
        self.__descriere_noua = "Nota 7"
        self.__deadline_nou = "25/11/2022"
        try:
            self.__servicepb.adauga_pb_service(self.__acelasi_nr, self.__descriere_noua, self.__deadline_nou)
            assert False
        except RepoPbError as re:
            assert (str(re) == "Problema laborator existenta")

        self.__nr_nou = 3
        try:
            self.__servicepb.cauta_pb_service(self.__nr_nou)
        except RepoPbError as re:
            assert (str(re) == "Problema laborator inexistenta")

        self.__acelasi_nr = (2, 5)
        self.__descriere_noua = "Nota 9"
        self.__deadline_nou = "25/12/2022"
        self.__pb_de_modificat = Problema(self.__acelasi_nr, self.__descriere_noua, self.__deadline_nou)
        self.__servicepb.modifica_pb_service(self.__acelasi_nr, self.__descriere_noua, self.__deadline_nou)
        assert (len(self.__servicepb) == 1)
        pb_gasita = self.__servicepb.cauta_pb_service(self.__acelasi_nr)
        assert (pb_gasita.get_descriere() == self.__descriere_noua)

        self.__acelasi_nr = (2, 5)
        assert (len(self.__servicepb) == 1)
        self.__servicepb.sterge_pb_service(self.__acelasi_nr)
        assert (len(self.__servicepb) == 0)




    def run_teste(self):
       self.__run_teste_domain()
       print("Teste domain probleme trecute cu succes")
       self.__run_teste_validator()
       print("Teste validare probleme trecute cu succes")
       self.__run_teste_repo_pb()
       print("Teste repository probleme trecute cu succes")
       self.__run_teste_service_pb()
       print("Teste service probleme trecute cu succes")


