class Problema(object):
    def __init__(self,nr,descriere,deadline):
        '''
        Adauga o problema de laborator
        :param nr:numarul laboratorului si numarul problemei
        :param descriere:descrierea string a problemei
        :param deadline:daedline-ul problemei
        '''
        self.__nr=nr
        self.__descriere=descriere
        self.__deadline=deadline

    def get_nr(self):
        '''
        Returneaza numarul laboratorului si numarul problemei
        :return: rez:int :numarul al laboratorului si numarul al problemei
        '''
        return self.__nr

    def get_descriere(self):
        '''
        Returneaza descrierea problemei
        :return: rez:string :descrierea problemei
        '''
        return self.__descriere

    def get_deadline(self):
        '''
        Returneaza deadline-ul problemei
        :return: rez:string:deadline-ul problemei
        '''
        return self.__deadline

    def set_nr(self,value):
        '''
        Seteaza un numarul de laborator si numarul problemei
        :param value: tuple:numarul de laborator si numarul problemei
        :return:
        '''
        self.__nr=value

    def set_descriere(self,value):
        '''
        Seteaza descrierea unei probleme
        :param value: string: descrierea problemei
        :return:
        '''
        self.__descriere=value

    def set_deadline(self,value):
        '''
        Seteaza deadline-ul unei probleme
        :param value: string: deadline-ul problemei
        :return:
        '''
        self.__deadline=value

    def __eq__(self, other):
        '''
        Verifica daca doua probleme cu acelasi numar apar la acelasi laborator
        :param other: a doua problema
        :return: rez:int
        '''
        return self.__nr==other.__nr

    def __str__(self):
        '''
        Afiseaza datele problemei
        :return: sirul string cu datele unei probleme
        '''
        return f"{self.__nr}  {self.__descriere}  {self.__deadline}"

    def print_pb(self):
        '''
        Afiseaza datele problemei
        :return: sirul string cu datele problemei
        '''
        return f"Numar laborator:{self.__nr[0]}, Numar problema:{self.__nr[1]}, Descriere:{self.__descriere}, Dealine:{self.__deadline}"