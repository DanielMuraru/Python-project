import ast

from Erori.Erori_student import RepoError


class RepoStudenti(object):
    def __init__(self):
        self._studenti={}
    def __len__(self):
        '''
        Afla lungimea listei de studenti
        :return: rez:lungimea int a listei de studenti
        '''
        return len(self._studenti)

    def adauga_student(self,student):
        '''
        Adauga un student in lista de studenti
        :param student: obiect al clasei Student cu atributele: id de tip int,nume de tip string,grup de tip int
        :return:
        :raises: RepoError daca obiectul student exista deja in lista de studenti cu stringul "Student existent"
        '''
        id_student=student.get_id()
        if id_student in self._studenti:
            raise RepoError("Student existent")
        self._studenti[id_student]=student

    def modifica_student(self, student):
        '''
        Modifica datele unui student din lista de studenti
        :param student: student
        :return:
        :raises: RepoError daca studentul nu exista
        '''
        if student.get_id() not in self._studenti:
            raise RepoError("Student inexistent")
        self._studenti[student.get_id()]=student

    def get_all(self,l,rez):
        '''
        Creeaza o lista cu toti studentii
        :return: rez:lista de studenti
        '''
        return self.get_all_rec(l,rez)


    def get_all_rec(self,l,rez):
        '''
        Creeaza o lista cu toti studentii
        :return: rez:lista de studenti
        '''
        if l==0:
            return rez
        st=list(self._studenti.values())
        student=st[l-1]
        rez.append(student)
        self.get_all_rec(l-1,rez)

    def cauta_student(self, l,id):
        '''
        Cauta studentul ales in lista de studenti
        :param id: atribut de tip int obiectului student
        :return: obiectul student care are id-ul ales
        :raises: RepoError daca studentul nu exista cu stringul "Student inexistent"
        '''
        """if id not in self._studenti:
            raise RepoError("Student inexistent")
        return self._studenti[id]"""
        return self.cauta_student_rec(l,id)

    def cauta_student_rec(self,l,id):
        """
        n=lungimea listei de studenti
        Caz favorabil:studentul cautat este la coada listei de studenti
        T(n)=1 => O(1)
        Caz mediu:studentul cautat este la mijlocul listei de studenti
        T(n)=suma de la 1 la n/2 de 1=n/2=>O(n/2)
        Caz defavorabil:studentul cautat este la inceputul listei de studenti
        T(n)=suma de la 1 la n de 1=n=>O(n)
        => Complexitatea este O(n)

        :param l:
        :param id:
        :return:
        """
        if l==0:
            raise RepoError("Student inexistent")
        st=list(self._studenti.values())
        student=st[l-1]
        if student.get_id()==id:
            return student
        return self.cauta_student_rec(l-1,id)



    def sterge_student(self, id):
        '''
        Sterge un student ales din lista de studenti
        :param id: id-ul int al studentului
        :return:
        '''
        if id not in self._studenti:
            raise RepoError("Student inexistent")
        del self._studenti[id]