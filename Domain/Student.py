import ast


class Student(object):

    def __init__(self,id,nume,grup):
        '''
        Adauga un nou student
        :param id: id-ul int al studentului
        :param nume: numele string al studentului
        :param grup: grupul int din care face parte studentul
        '''
        self.__id = id
        self.__nume = nume
        self.__grup=grup

    def get_id(self):
        '''
        Returneaza id-ul int al studentului
        :return: id-ul int al studentului
        '''
        return self.__id
    def get_nume(self):
        '''
        Returneaza numele studentului
        :return: numele string al studentului
        '''
        return self.__nume
    def get_grup(self):
        '''
        Returneaza numarul int al grupului din care face parte studentul
        :return: numarul int al grupului
        '''
        return self.__grup
    def set_id(self,value):
        '''
        Seteaza id-ul studentului
        :param value:
        :return:
        '''
        self.__id=value
    def set_nume(self,value):
        '''
        Modifica numele unui student
        :param value: numele string nou
        :return:
        '''
        self.__nume=value
    def set_grup(self,value):
        '''
        Modifica numarul grupului din care face parte un student
        :param value: numarul int al grupului
        :return:
        '''
        self.__grup=value
    def print_student(self):
        '''
        Afiseaza datele studentului
        :return: sir string cu datele studentului
        '''
        return f"Id:{self.__id}, Nume:{self.__nume}, Grupa:{self.__grup}"
    def egal_id(self,other):
        '''
        Verifica daca doi studenti au acelasi id
        :param other: al doilea student
        :return: rez:int
        '''
        return self.__id==other.__id
    def __eq__(self, other):
        '''
        Verifica daca doi studenti au acelasi id
        :param other: al doilea student
        :return: rez:int
        '''
        return self.__id==other.__id
    def __str__(self):
        '''
        Afiseaza datele studentului
        :return: sir string cu datele studentului
        '''
        return f"{self.__id}  {self.__nume}  {self.__grup}"


