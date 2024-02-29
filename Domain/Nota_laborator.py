class Nota_laborator(object):

    def __init__(self,nr_lab_pb_student,nume,nota_lab):
        '''
        Atribuie unui student nota de la laborator
        :param nr_lab: numarul laboratorului
        :param nota_lab: nota de la laborator
        :param student_id: id-ul studentului
        '''

        self.__nr_lab_pb_student=nr_lab_pb_student
        self.__nume=nume
        self.__nota_lab=nota_lab


    def get_nr_lab_si_pb_si_student(self):
        '''
        Returneaza id-ul studentului,numarul laboratorului si numarul problemei
        :return: id-ul studentului,numarul laboratorului si numarul problemei
        '''
        return self.__nr_lab_pb_student
    def get_nume(self):
        '''
        Returneaza numele studentului
        :return: numele string al studentului
        '''
        return self.__nume
    def get_nota_lab(self):
        '''
        Returneaza nota de la laborator
        :return: nota de la laborator
        '''
        return self.__nota_lab

    def get_student_id(self):
        '''
        Returneaza id-ul studentului cu nota de laborator si problema de laborator pe care o are
        :return:
        '''
        nr=self.__nr_lab_pb_student
        return int(nr[0])

    def set_nr_si_pb_si_student(self,value):
        '''
        Seteaza id-ul studentului,numarul de laborator si numarul problemei
        :param value:tuple,id-ul studentului,numarul de laborator si numarul problemei
        :return:
        '''
        self.__nr_lab_pb_student=value
    def set_nume(self,value):
        '''
        Seteaza numele studentului
        :param value:
        :return:
        '''
        self.__nume=value
    def set_nota_lab(self,value):
        '''
        Seteaza nota de la laborator
        :param value: nota de la laborator
        :return:
        '''
        self.__nota_lab=value

    def __eq__(self, other):
        '''

        :param other:
        :return:
        '''
        return self.__nr_lab_pb_student==other.__nr_lab_pb_student
    def print_note(self):
        '''
        Afiseaza nota studentului la problema de laborator
        :return:
        '''
        return f"Id student:{self.__nr_lab_pb_student[0]}, Nume student:{self.__nume}, Numar laborator:{self.__nr_lab_pb_student[1]}, Numar problema:{self.__nr_lab_pb_student[2]}, Nota:{self.__nota_lab}"
    def __str__(self):
        '''
        Afiseaza nota de la laborator
        :return:
        '''
        return f"{self.__nr_lab_pb_student[0]}  {(self.__nr_lab_pb_student[1],self.__nr_lab_pb_student[2])}  {self.__nota_lab}"
