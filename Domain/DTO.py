class DTO(object):
     def __init__(self,id_student,nume,media):
         self.id_student=id_student
         self.nume_prenume=nume
         self.media=media

     def get_id_student(self):
         '''
         Returneaza id-ul studentului
         :return:
         '''
         return self.id_student
     def get_nume_prenume(self):
         '''
         Returneaza numele si prenumele studentului
         :return:
         '''
         return self.nume_prenume
     def get_nume(self):
         '''
         Returneaza numele studentului
         :return:
         '''
         self.nume_prenume.strip()
         parti=self.nume_prenume.split()
         return parti[0]
     def get_media(self):
         '''
         Returneaza media notelor studentului
         :return:
         '''
         return self.media
     def print_note_studenti(self):
         '''
         Afiseaza datele unui student
         :return:
         '''
         return f"Id student: {self.id_student}, Nume:{self.nume_prenume}, Nota: {self.media}"
     def __str__(self):
         '''
         Afiseaza datele studentului
         :return:
         '''
         return f"Id student: {self.id_student}, Nume:{self.nume_prenume}, Media: {self.media}"