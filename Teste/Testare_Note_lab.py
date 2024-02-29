from Business.ServiceNote import ServiceNote
from Domain.Nota_laborator import Nota_laborator
from Domain.Problema_laborator import Problema
from Domain.Student import Student
from Erori.Erori_note import ValidatorNoteError, RepoNoteError
from Erori.Erori_student import RepoError
from Persistenta.RepoNote import RepoNote
from Persistenta.RepoNote_file import Reponote_file
from Persistenta.RepoProblema_file import Repopb_file
from Persistenta.RepoProblema_laborator import RepoProbleme
from Persistenta.RepoStudenti import RepoStudenti
from Persistenta.RepoStudenti_file import RepoStudentifile
from Validare.Nota_problema_laborator import ValidatorNota


class Teste_note(object):
    def __init__(self):
        self.__nr_lab_pb_student=(1,1,3)
        self.__nota_lab=10
        self.__nota_lab_domain = Nota_laborator(self.__nr_lab_pb_student,None,self.__nota_lab)
        self.__repo_studenti = RepoStudentifile("Teste/student.txt")
        self.__repo_lab = Repopb_file("Teste/probleme.txt")
        self.__repo_note = Reponote_file("Teste/note.txt", self.__repo_studenti, self.__repo_lab)

    def __run_teste_domain(self):
        assert(self.__nota_lab==self.__nota_lab_domain.get_nota_lab())
        assert(self.__nr_lab_pb_student==self.__nota_lab_domain.get_nr_lab_si_pb_si_student())
        clona_nota=Nota_laborator((1,1,3),None,7)
        assert(self.__nota_lab_domain==clona_nota)
        assert(str(self.__nota_lab_domain)=="1  (1, 3)  10")
    def __run_teste_validare(self):
        self.__validator_note=ValidatorNota()
        self.__validator_note.validare_nota(self.__nota_lab_domain)
        self.__nota_lab_domain.set_nota_lab(-1)
        try:
            self.__validator_note.validare_nota(self.__nota_lab_domain)
            assert False
        except ValidatorNoteError as ve:
            assert(str(ve)=="Nota problema de laborator invalida")
    def __run_teste_repo(self):
        self.__nota_lab_domain.set_nota_lab(10)
        assert(len(self.__repo_note)==0)
        self.__repo_note.adauga_nota_repo(self.__nota_lab_domain)
        assert(len(self.__repo_note)==1)
        try:
            self.__repo_note.adauga_nota_repo(self.__nota_lab_domain)
            assert False
        except RepoNoteError as ve:
            assert(str(ve)=="Studentul are deja o nota la o problema de laborator")
        nr=self.__nota_lab_domain.get_nr_lab_si_pb_si_student()
        id_pb=(nr[1],nr[2])
        id_student=int(nr[0])
        self.__repo_note.sterge_nota_repo_dupa_problema(id_pb)
        self.__repo_note.adauga_nota_repo(self.__nota_lab_domain)
        self.__repo_note.sterge_nota_repo_dupa_student(id_student)
        note = self.__repo_note.get_all()
        for nota in note:
            print(nota)
        assert(len(self.__repo_note)==0)

    def __run_teste_service(self):
        self.__service_teste=ServiceNote(self.__repo_studenti,self.__repo_lab,self.__repo_note,self.__validator_note)
        self.__student_note=Student(1,"Marius",213)
        self.__repo_studenti.adauga_student_fisier(self.__student_note)
        self.__lab_note=Problema((2,3),"se face cmmdc","22/7/2022")
        self.__repo_lab.adauga_pb(self.__lab_note)
        self.__nota_lab=10
        assert(len(self.__service_teste)==0)
        self.__service_teste.adauga_nota_student_service(self.__lab_note.get_nr(),self.__student_note.get_id(),self.__nota_lab)
        assert(len(self.__service_teste)==1)
        try:
            self.__service_teste.adauga_nota_student_service(self.__lab_note.get_nr(), self.__student_note.get_id(),self.__nota_lab)
            assert False
        except RepoNoteError as ve:
            assert(str(ve)=="Studentul are deja o nota la o problema de laborator")



        lista_nr=self.__lab_note.get_nr()

        self.__service_teste.sterge_nota_student_problema_service(lista_nr)

        assert(len(self.__service_teste)==0)



        self.__nota_lab=-2
        try:
            self.__service_teste.adauga_nota_student_service(self.__lab_note.get_nr(), self.__student_note.get_id(),
                                                        self.__nota_lab)
            assert False
        except ValidatorNoteError as ve:
            assert(str(ve)=="Nota problema de laborator invalida")


    def run_teste(self):
        self.__run_teste_domain()
        print("Teste domain note trecute cu succes")
        self.__run_teste_validare()
        print("Teste validare note trecute cu succes")
        self.__run_teste_repo()
        print("Teste repo note trecute cu succes")
        self.__run_teste_service()
        print("Teste service note trecute cu succes")