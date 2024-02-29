from Domain.Student import Student


class ServiceStudenti(object):

    def __init__(self,__repo_studenti,__validator_student):
        self.__repo_studenti_fisier=__repo_studenti
        self.__validator_student=__validator_student


    def __len__(self):
        '''
        Afla lungimea listei de studenti
        :return: lungimea listei de studenti
        '''
        return len(self.__repo_studenti_fisier)

    def adauga_student_service(self,id,nume,grupa):
        '''
        Adauga un student in lista de studenti
        :param id: id-ul studentului
        :param nume: numele studentului
        :param grupa: grupa din care face parte studentul
        :return:
        '''
        student=Student(id,nume,grupa)
        self.__validator_student.ValidareStudent(student)
        self.__repo_studenti_fisier.adauga_student(student)

    def cauta_student_service(self, id):
        '''
        Cauta studentul ales in lista de studenti
        :param id: id-ul int al studentului
        :return: studentul ales
        raises: RepoError daca studentul nu exista
        '''
        l=len(self.__repo_studenti_fisier)
        return self.__repo_studenti_fisier.cauta_student(l,id)

    def sterge_student_service(self, id):
        '''
        Sterge studentul ales din lista de studenti
        :param id: id-ul int al studentului
        :return:
        :raises: RepoError daca studentul nu exista
        '''
        self.__repo_studenti_fisier.sterge_student(id)

    def modifica_student_service(self, id,nume,grup):
        '''
        Modifica datele unui student din lista de studenti
        :param id: id-ul int al studentului
        :param nume: numele string al studentului
        :param grup: grupa int din care face parte studentul
        :return:
        :raises RepoError daca studentul nu exista
        '''
        student=Student(id,nume,grup)
        self.__validator_student.ValidareStudent(student)
        self.__repo_studenti_fisier.modifica_student(student)



    def get_all_service(self):
        '''
        Creeaza o lista cu toti studentii
        :return: rez:lista de studenti
        '''
        rez = []
        lee=len(self.__repo_studenti_fisier)
        self.__repo_studenti_fisier.get_all(lee,rez)
        return rez

