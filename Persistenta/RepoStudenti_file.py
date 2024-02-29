import ast
from shlex import join

from Domain.Student import Student
from Persistenta.RepoStudenti import RepoStudenti
from Validare.Validator_Student import ValidatorStudent


class RepoStudentifile(RepoStudenti):
    def __init__(self,numetxt):
        RepoStudenti.__init__(self)
        self.__fisier_repo_studenti=numetxt
        self.__validare_student=ValidatorStudent()
    def __citeste_fisier(self):
        '''
        Citeste din fisier datele studentilor
        :return:
        '''
        with open(self.__fisier_repo_studenti,"r") as f:
            linii=f.readlines()
            self._studenti.clear()
            for linie in linii:
                linie=linie.strip()
                if linie!="":
                    parti=linie.split("  ")
                    id_student=int(parti[0])
                    nume=parti[1]
                    grupa=int(parti[2])
                    student=Student(id_student,nume,grupa)
                    try:
                        self.__validare_student.ValidareStudent(student)
                        self._studenti[id_student]=student
                    except:
                        pass
    def __scrie_in_fisier(self):
        '''
        Rescrie in fisier lista de studenti cu datele fiecaruia
        :return:
        '''
        with open(self.__fisier_repo_studenti,"w") as f:
            for student in self._studenti.values():
                f.write(str(student)+"\n")

    def adauga_student(self,student):
        '''
        Adauga un student in lista de studenti
        :param student: obiect al clasei Student cu atributele: "id" de tip int,"nume" de tip string,"grup" de tip int
        :return:
        :raises: RepoError daca obiectul student exista deja in lista de studenti cu stringul "Student existent"
        '''
        self.__citeste_fisier()
        RepoStudenti.adauga_student(self,student)
        self.__scrie_in_fisier()

    def sterge_student(self,id):
        '''
        Sterge un student din lista de studenti
        :param id: id-ul int al studentului
        :return:
        :raises: RepoError daca studentul nu exista in lista cu stringul "Student inexistent"
        '''
        self.__citeste_fisier()
        RepoStudenti.sterge_student(self,id)
        self.__scrie_in_fisier()
    def cauta_student(self,l,value):
        '''
        Cauta un student in lista de studenti
        :param value: id-ul int al studentului
        :return: Obiectul student
        :raises: RepoError daca studentul nu exista in lista de studenti cu stringul "Student inexistent"
        '''
        self.__citeste_fisier()
        return RepoStudenti.cauta_student(self,l,value)

    def modifica_student(self,student):
        '''
        Modifica datele unui student din fisier
        :param student: obicetul student al clasei Student
        :return:
        :raises: RepoError daca studentul nu exista in lista de studenti cu stringul "Student inexistent"
        '''
        self.__citeste_fisier()
        RepoStudenti.modifica_student(self,student)
        self.__scrie_in_fisier()
    def __len__(self):
        '''
        Afla lungimea listei de studenti
        :return: lungimea listei de studenti
        '''
        self.__citeste_fisier()
        return len(self._studenti)
    def get_all(self,l,rez):
        '''
        Creeaza lista de studenti
        :return: lista de studenti
        '''
        self.__citeste_fisier()
        return RepoStudenti.get_all(self,l,rez)
