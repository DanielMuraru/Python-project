from Business.Service_student import ServiceStudenti
from Domain.Student import Student
from Erori.Erori_student import ValidatorError, RepoError
from Persistenta.RepoStudenti import RepoStudenti
from Persistenta.RepoStudenti_file import RepoStudentifile
from Validare.Validator_Student import ValidatorStudent


class Teste(object):
    def __init__(self):
        self.__id=1
        self.__nume="Andrei"
        self.__grup=214
        self.__student=Student(self.__id,self.__nume,self.__grup)
        self.__repo_studenti = RepoStudentifile("Teste/student.txt")
    def goleste_fisier(self,fisier):
        with open(fisier,"w") as f:
            pass
    def __run_teste_domain(self):
        assert(self.__student.get_id()==self.__id)
        assert(self.__student.get_nume()==self.__nume)
        assert(self.__student.get_grup()==self.__grup)
        clona_student=Student(self.__id,None,None)
        assert(self.__student==clona_student)
        assert(self.__student.egal_id(clona_student))
        assert(str(self.__student)=="1  Andrei  214")

    def run_teste_validare(self):
        self.__validator_student = ValidatorStudent()
        self.__id_nou=2
        self.__nume_nou="Vlad"
        self.__grup_nou=215
        self.__e_sters=0
        self.__student_de_validat=Student(self.__id_nou,self.__nume_nou,self.__grup_nou)
        self.__validator_student.ValidareStudent(self.__student_de_validat)

        self.__id_nou= -2
        self.__nume_nou = ""
        self.__grup_nou = 0
        self.__student_de_validat_invalid=Student(self.__id_nou, self.__nume_nou, self.__grup_nou)
        try:
            self.__validator_student.ValidareStudent(self.__student_de_validat_invalid)
            assert False
        except ValidatorError as ve:
            assert(str(ve)=="Id invalid\nNume invalid\nGrup invalid\n")

    def run_teste_repo(self):
        self.goleste_fisier("Teste/student.txt")
        assert(len(self.__repo_studenti)==0)
        self.__id=1
        self.__nume="Andrei"
        self.__grup=214
        self.__student=Student(self.__id,self.__nume,self.__grup)
        self.__repo_studenti.adauga_student_fisier(self.__student)
        assert (len(self.__repo_studenti) == 1)

        self.__acelasi_id = 1
        self.__nume_dif = "Marius"
        self.__grup_dif = 217
        self.__student_acelasi_id = Student(self.__acelasi_id, self.__nume_dif, self.__grup_dif)
        l=self.__repo_studenti.get_all()
        try:
            self.__repo_studenti.adauga_student_fisier(self.__student_acelasi_id)

            assert False
        except RepoError as ve:
            assert(str(ve)=="Student existent")

        self.__id_inexistent=2
        try:
            self.__repo_studenti.cauta_student(self.__id_inexistent)
            assert False
        except RepoError as ve:
            assert(str(ve)=="Student inexistent")

        self.__id = 1
        self.__nume_nou = "Vlad"
        self.__grup = 217
        self.__student_modificat = Student(self.__id , self.__nume_nou, self.__grup)
        self.__repo_studenti.modifica_student_fisier(self.__student_modificat)
        assert(len(self.__repo_studenti)==1)
        student_gasit=self.__repo_studenti.cauta_student_in_fisier(self.__id)
        assert(student_gasit.get_nume()==self.__nume_nou)

        self.__id_inexistent=2
        self.__nume_nou="Razvan"
        self.__student_modificat_inexistent=Student(self.__id_inexistent,self.__nume_nou,None)
        try:
            self.__repo_studenti.modifica_student_fisier(self.__student_modificat_inexistent)
            assert False
        except RepoError as ve:
            assert(str(ve)=="Student inexistent")

        self.__alt_id=2
        self.__alt_nume="Razvan"
        self.__alt_grup=214
        self.__alt_student=Student(self.__alt_id,self.__alt_nume,self.__alt_grup)
        self.__repo_studenti.adauga_student_fisier(self.__alt_student)
        assert(len(self.__repo_studenti)==2)
        self.__repo_studenti.sterge_student_fisier(self.__id)
        assert(len(self.__repo_studenti)==1)
        try:
            self.__repo_studenti.sterge_student(self.__id)
            assert False
        except RepoError as ve:
            assert(str(ve)=="Student inexistent")


    def run_teste_business(self):

        self.goleste_fisier("Teste/student.txt")
        self.__validator_student=ValidatorStudent()
        self.__service_studenti=ServiceStudenti(self.__repo_studenti,self.__validator_student)
        assert (len(self.__service_studenti) == 0)
        self.__id = 1
        self.__nume = "Andrei"
        self.__grup = 214
        self.__service_studenti.adauga_student_service(self.__id,self.__nume,self.__grup)
        assert (len(self.__service_studenti) == 1)

        self.__acelasi_id = 1
        self.__alt_nume = "Razvan"
        self.__alt_grup = 214
        try:
            self.__service_studenti.adauga_student_service(self.__acelasi_id,self.__alt_nume,self.__alt_grup)
        except RepoError as ve:
            assert(str(ve)=="Student existent")

        self.__id_inexistent=2
        try:
            self.__service_studenti.cauta_student_service(self.__id_inexistent)
            assert False
        except RepoError as ve:
            assert(str(ve)=="Student inexistent")

        self.__alt_id = 2
        self.__alt_nume = "Razvan"
        self.__alt_grup = 214
        self.__service_studenti.adauga_student_service(self.__alt_id, self.__alt_nume, self.__alt_grup)
        assert(len(self.__service_studenti)==2)

        self.__id=2
        self.__nume_nou="Marian"
        self.__grup_nou=211
        self.__service_studenti.modifica_student_service(self.__id,self.__nume_nou,self.__grup_nou)
        student_gasit=self.__service_studenti.cauta_student_service(self.__id)
        assert(student_gasit.get_nume()==self.__nume_nou)

        self.__id = 4
        self.__nume_nou = "Marian"
        self.__grup_nou = 211
        try:
            self.__service_studenti.modifica_student_service(self.__id, self.__nume_nou, self.__grup_nou)
        except RepoError as ve:
            assert(str(ve)=="Student inexistent")

        self.__id=1
        self.__service_studenti.sterge_student_service(self.__id)
        assert(len(self.__service_studenti)==1)
        try:
            self.__service_studenti.sterge_student_service(self.__id)
            assert False
        except RepoError as ve:
            assert(str(ve)=="Student inexistent")

    def run_teste(self):
        self.__run_teste_domain()
        print("Teste domain trecute cu succes")
        self.run_teste_validare()
        print("Teste validare trecute cu succes")
        self.run_teste_repo()
        print("Teste repository trecute cu succes")
        self.run_teste_business()
        print("Teste service trecute cu succes")
