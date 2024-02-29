import ast

from Erori.Erori_note import RepoNoteError, ValidatorNoteError
from Erori.Erori_problema_laborator import RepoPbError, ValidatorPbError
from Erori.Erori_student import ValidatorError, RepoError



class UI(object):

    def __init__(self, service_studenti,service_probleme,service_note):
        self.__service_studenti=service_studenti
        self.__service_probleme=service_probleme
        self.__service_note=service_note
        self.__comenzi={"adauga_student":self.__adauga_student_ui,"sterge_student":self.__sterge_student_ui,"cauta_student":self.__cauta_student_ui,"modifica_student":self.__modifica_student_ui,"print_studenti":self.__print_studenti_ui,
                        "adauga_problema_laborator":self.__adauga_problema_laborator_ui,"sterge_problema":self.__sterge_problema_laborator_ui,"cauta_problema":self.__cauta_problema_laborator_ui,"modifica_problema":self.__modifica_problema_laborator_ui,"print_probleme":self.__print_probleme_laborator_ui,
                        "adauga_nota":self.__adauga_nota_student,"print_note":self.__print_note,
                        "filtrare1":self.lista_cu_studenti_si_notele_la_o_problema_de_laborator_ui,
                        "filtrare2":self.lista_studenti_cu_media_notelor_la_laborator_mai_mica_decat_cinci_ui,
                        "filtrare3":self.lista_studenti_cu_media_notelor_la_laborator_minim_cinci_service,
                        "get_studenti":self.get_studenti,
                        "get_probleme": self.get_probleme
                        }
    def get_studenti(self):
        lista=self.__service_studenti.get_all_service()
        for student in lista:
            print(str(student[1]))
    def get_probleme(self):
        lista=self.__service_probleme.get_allpb_service()
        for problema in lista:
            print(str(problema[1]))
    def __adauga_student_ui(self):

        if len(self.__params)!=3:
            print("Numar parametrii invalid")
            return
        id=int(self.__params[0])
        nume=self.__params[1]
        grup=int(self.__params[2])
        self.__service_studenti.adauga_student_service(id,nume,grup)
        print("Student adaugat cu succes")

    def __sterge_student_ui(self):
        if len(self.__params)!=1:
            print("Numar parametrii invalid")
            return
        id=int(self.__params[0])
        self.__service_studenti.sterge_student_service(id)
        self.__service_note.sterge_nota_student_problema_service(id)
        print("Studentul a fost sters")

    def __cauta_student_ui(self):
        if len(self.__params)!=1:
            print("Numar parametrii invalid")
            return
        id=int(self.__params[0])

        student=self.__service_studenti.cauta_student_service(id)
        print(student.print_student())

    def __modifica_student_ui(self):
        if len(self.__params)!=3:
            print("Numar parametrii invalid")
            return
        id=int(self.__params[0])
        nume=self.__params[1]
        grup=int(self.__params[2])
        self.__service_studenti.modifica_student_service(id,nume,grup)
        print("Datele studentului au fost modificate")
    def __print_studenti_ui(self):
        if len(self.__params)!=0:
            print("Numar parametrii invalid")
            return
        studenti=self.__service_studenti.get_all_service()
        if len(studenti)==0:
            print("Nu exista studenti")
            return
        for student in studenti:
            print(student.print_student())

    def __adauga_problema_laborator_ui(self):
        if len(self.__params)!=3:
            print("Numar parametrii invalid")
            return
        nr=ast.literal_eval(self.__params[0])
        descriere=self.__params[1]
        deadline=self.__params[2]
        self.__service_probleme.adauga_pb_service(nr,descriere,deadline)
        print("Problema laborator adaugata cu succes")


    def __sterge_problema_laborator_ui(self):
        if len(self.__params)!=1:
            print("Numar parametrii invalid")
            return
        nr=ast.literal_eval(self.__params[0])
        self.__service_probleme.sterge_pb_service(nr)
        self.__service_note.sterge_nota_student_problema_service(nr)
        print("Problema laborator stearsa")

    def __cauta_problema_laborator_ui(self):
        if len(self.__params)!=1:
            print("Numar parametrii invalid")
            return
        nr=ast.literal_eval(self.__params[0])
        problema=self.__service_probleme.cauta_pb_service(nr)
        print(problema.print_pb())

    def __modifica_problema_laborator_ui(self):
        if len(self.__params)!=3:
            print("Numar parametrii invalid")
            return
        nr=ast.literal_eval(self.__params[0])
        descriere=self.__params[1]
        deadline=self.__params[2]
        self.__service_probleme.modifica_pb_service(nr,descriere,deadline)
        print("Datele problemei au fost modificate")

    def __print_probleme_laborator_ui(self):
        if len(self.__params)!=0:
            print("Numar parametrii invalid")
            return
        probleme=self.__service_probleme.get_allpb_service()
        if len(probleme)==0:
            print("Nu exista probleme")
        for problema in probleme:
            print(problema.print_pb())

    def __adauga_nota_student(self):
        if len(self.__params)!=3:
            print("Numar parametrii invalid")
            return
        id=int(self.__params[0])
        nr_lab_pb=ast.literal_eval(self.__params[1])
        nota=float(self.__params[2])
        self.__service_note.adauga_nota_student_service(nr_lab_pb,id,nota)
        print("Nota a fost adaugata")
    def __print_note(self):
        if len(self.__params)!=0:
            print("Numar parametrii invalid")
            return
        note=self.__service_note.get_all()
        if len(note)==0:
            print("Nu exista note")
        for nota in note:
            print(nota.print_note())
    def lista_cu_studenti_si_notele_la_o_problema_de_laborator_ui(self):
        if len(self.__params)!=1:
            print("Numar parametrii invalid")
            return
        value=ast.literal_eval(self.__params[0])
        rez=self.__service_note.lista_cu_studenti_si_notele_la_o_problema_de_laborator_service(value)
        try:
            self.__service_probleme.cauta_pb_service(value)
            if len(rez) == 0:
                print("Nu exista studenti cu nota la aceasta problema de laborator")
        except RepoPbError as ve:
            print(str(ve))
        for student in rez:
            print(student.print_note_studenti())
    def lista_studenti_cu_media_notelor_la_laborator_mai_mica_decat_cinci_ui(self):
        if len(self.__params)!=0:
            print("Numar parametrii invalid")
            return
        rez=self.__service_note.lista_studenti_cu_media_notelor_la_laborator_mai_mica_decat_cinci_service()
        if len(self.__service_studenti)==0:
            print("Nu exista studenti adaugati")
        elif len(self.__service_note)==0:
            print("Nu exista note")
        elif len(rez)==0:
            print("Nu exista studenti cu media notelor de laborator mai mica decat cinci")
        for student in rez:
            print(student)

    def lista_studenti_cu_media_notelor_la_laborator_minim_cinci_service(self):
        if len(self.__params)!=0:
            print("Numar parametrii invalid")
            return
        rez = self.__service_note.lista_studenti_cu_media_notelor_la_laborator_minim_cinci_service()
        if len(self.__service_studenti) == 0:
            print("Nu exista studenti adaugati")
        elif len(self.__service_note) == 0:
            print("Nu exista note")
        elif len(rez) == 0:
            print("Nu exista studenti cu media notelor de laborator mai mare decat cinci")
        for student in rez:
            print(student)
    def run_UI(self):
        while True:
            print(self.__comenzi)
            comanda=input(">>>")
            comanda.strip()
            if comanda=="":
                continue
            elif comanda=="exit":
                return
            parti=comanda.split("  ")
            nume_comanda=parti[0]
            self.__params=parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError as ve:
                    print(ve)
                except ValidatorError as ve:
                    print(ve)
                except RepoError as ve:
                    print(ve)
                except RepoPbError as re:
                    print(re)
                except ValidatorPbError as ve:
                    print(ve)
                except RepoNoteError as ve:
                    print(ve)
                except ValidatorNoteError as ve:
                    print(ve)

            else:
                print("Comanda invalida")


