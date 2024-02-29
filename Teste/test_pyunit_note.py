
from Business.ServiceNote import ServiceNote
from Domain.Nota_laborator import Nota_laborator
from Domain.Problema_laborator import Problema
from Domain.Student import Student
from Erori.Erori_note import ValidatorNoteError, RepoNoteError
from Erori.Erori_problema_laborator import RepoPbError
from Erori.Erori_student import RepoError
from Persistenta.RepoNote_file import Reponote_file
from Persistenta.RepoProblema_file import Repopb_file
from Persistenta.RepoStudenti_file import RepoStudentifile
from Validare.Nota_problema_laborator import ValidatorNota

import unittest

class Test_nota(unittest.TestCase):
    def setUp(self):
        self.__repo_st=RepoStudentifile("Teste/student.txt")
        self.__repo_pb=Repopb_file("Teste/probleme.txt")
        self.__repo_note=Reponote_file("Teste/note.txt",self.__repo_st,self.__repo_pb,"Teste/raport1_teste.txt")
        self.__validare_note=ValidatorNota()
        self.__service_note=ServiceNote(self.__repo_st,self.__repo_pb,self.__repo_note,self.__validare_note,"Teste/raport1_teste.txt")
        self.__nota=Nota_laborator(None,None,None)
        self.__student=Student(None,None,None)
        self.__pb=Problema(None,None,None)
        with open("Teste/note.txt","w") as f:
            pass
        with open("Teste/student.txt","w") as g:
            pass
        with open("Teste/probleme.txt","w") as h:
            pass
    def tearDown(self):
        with open("Teste/note.txt","w") as f:
            pass
        with open("Teste/student.txt","w") as g:
            pass
        with open("Teste/probleme.txt","w") as h:
            pass

    def test_domain(self):
        self.__nota.set_nr_si_pb_si_student((1,1,3))
        self.__nota.set_nume("Andrei Dragos")
        self.__nota.set_nota_lab(10)
        self.assertTrue(self.__nota.get_nr_lab_si_pb_si_student()==(1,1,3))
        self.assertTrue(self.__nota.get_nota_lab()==10)
        clona_nota=Nota_laborator((1,1,3),"Andrei Dragos",10)
        self.assertTrue(self.__nota==clona_nota)
        self.assertTrue(str(self.__nota)=="1  (1, 3)  10")

    def test_validare(self):
        self.__nota.set_nr_si_pb_si_student((1, 1, 3))
        self.__nota.set_nume("Andrei Dragos")
        self.__nota.set_nota_lab(10)
        self.__validare_note.validare_nota(self.__nota)
        self.__nota.set_nr_si_pb_si_student((1, 1, 3))
        self.__nota.set_nume("Andrei Dragos")
        self.__nota.set_nota_lab(-1)
        try:
            self.__validare_note.validare_nota(self.__nota)
            assert False
        except ValidatorNoteError as ve:
            self.assertTrue(str(ve)=="Nota problema de laborator invalida")

    def test_repo_adaugare(self):
        self.assertEqual(len(self.__repo_note),0)
        self.__student.set_id(1)
        self.__student.set_nume("ANDREI")
        self.__student.set_grup(213)
        self.__repo_st.adauga_student(self.__student)
        self.__pb.set_nr((1,3))
        self.__pb.set_descriere("se face cmmdc")
        self.__pb.set_deadline("10/2/2000")
        self.__repo_pb.adauga_pb(self.__pb)
        self.__nota.set_nr_si_pb_si_student((1, 1, 3))
        self.__nota.set_nume("Andrei Dragos")
        self.__nota.set_nota_lab(10)
        self.__repo_note.adauga_nota_repo(self.__nota)
        self.assertEqual(len(self.__repo_note),1)
        try:
            self.__repo_note.adauga_nota_repo(self.__nota)
            assert False
        except RepoNoteError as ve:
            self.assertTrue(str(ve)=="Studentul are deja o nota la o problema de laborator")
    def test_repo_stergere_dupa_student(self):
        self.assertEqual(len(self.__repo_note), 0)
        self.__student.set_id(1)
        self.__student.set_nume("Andrei Dragos")
        self.__student.set_grup(213)
        self.__repo_st.adauga_student(self.__student)
        self.__pb.set_nr((1, 3))
        self.__pb.set_descriere("se face cmmdc")
        self.__pb.set_deadline("10/2/2000")
        self.__repo_pb.adauga_pb(self.__pb)
        self.__nota.set_nr_si_pb_si_student((1, 1, 3))
        self.__nota.set_nume("Andrei Dragos")
        self.__nota.set_nota_lab(10)
        self.__repo_note.adauga_nota_repo(self.__nota)
        problema2 = Problema((2, 1), "calculati", "10/2/2002")
        self.__repo_pb.adauga_pb(problema2)
        nota2=Nota_laborator((1,2,1),"Andrei Dragos",10)
        self.__repo_note.adauga_nota_repo(nota2)
        self.assertEqual(len(self.__repo_note), 2)
        self.__repo_st.sterge_student(self.__student.get_id())
        self.__repo_note.sterge_nota_repo_dupa_student(self.__student.get_id())
        self.assertEqual(len(self.__repo_note), 0)
    def test_repo_stergere_dupa_problema(self):
        self.assertEqual(len(self.__repo_note), 0)
        self.__student.set_id(1)
        self.__student.set_nume("Andrei Dragos")
        self.__student.set_grup(213)
        self.__repo_st.adauga_student(self.__student)
        self.__pb.set_nr((1, 3))
        self.__pb.set_descriere("se face cmmdc")
        self.__pb.set_deadline("10/2/2000")
        self.__repo_pb.adauga_pb(self.__pb)
        self.__nota.set_nr_si_pb_si_student((1, 1, 3))
        self.__nota.set_nume("Andrei Dragos")
        self.__nota.set_nota_lab(10)
        self.__repo_note.adauga_nota_repo(self.__nota)
        student2 = Student(2,"Marius",213)
        self.__repo_st.adauga_student(student2)
        nota2 = Nota_laborator((2, 1, 3), "Marius", 10)
        self.__repo_note.adauga_nota_repo(nota2)
        self.assertEqual(len(self.__repo_note), 2)
        self.__repo_pb.sterge_pb(self.__pb.get_nr())
        self.__repo_note.sterge_nota_repo_dupa_problema(self.__pb.get_nr())
        self.assertEqual(len(self.__repo_note), 0)

    def test_service_adaugare(self):
        self.assertEqual(len(self.__service_note), 0)
        self.__student.set_id(1)
        self.__student.set_nume("Andrei Dragos")
        self.__student.set_grup(213)
        self.__repo_st.adauga_student(self.__student)
        self.__pb.set_nr((1, 3))
        self.__pb.set_descriere("se face cmmdc")
        self.__pb.set_deadline("10/2/2000")
        self.__repo_pb.adauga_pb(self.__pb)
        nota=10
        self.__service_note.adauga_nota_student_service(self.__pb.get_nr(),self.__student.get_id(),nota)
        self.assertEqual(len(self.__service_note),1)
        try:
            self.__service_note.adauga_nota_student_service(self.__pb.get_nr(),self.__student.get_id(),nota)
            assert False
        except RepoNoteError as ve:
            self.assertTrue(str(ve)=="Studentul are deja o nota la o problema de laborator")
        self.__pb.set_nr((5, 3))
        self.__pb.set_descriere("se face cmmdc")
        self.__pb.set_deadline("10/2/2000")
        try:
            self.__service_note.adauga_nota_student_service(self.__pb.get_nr(), self.__student.get_id(), nota)
            assert False
        except RepoPbError as ve:
            self.assertTrue(str(ve) == "Problema laborator inexistenta")
        self.__repo_pb.adauga_pb(self.__pb)
        self.__student.set_id(3)
        self.__student.set_nume("Andrei Dragos")
        self.__student.set_grup(213)
        try:
            self.__service_note.adauga_nota_student_service(self.__pb.get_nr(),self.__student.get_id(),nota)
            assert False
        except RepoError as ve:
            self.assertTrue(str(ve)=="Student inexistent")
        self.__repo_st.adauga_student(self.__student)
        nota=0
        try:
            self.__service_note.adauga_nota_student_service(self.__pb.get_nr(), self.__student.get_id(), nota)
            assert False
        except ValidatorNoteError as ve:
            self.assertTrue(str(ve)=="Nota problema de laborator invalida")
    def test_service_sterge_blackbox(self):
        try:
            self.__service_note.sterge_nota_student_problema_service(1)
        except RepoError as ve:
            self.assertTrue(str(ve)=="Student inexistent")
        except RepoNoteError as ve:
            self.assertTrue(str(ve)=="Studentul nu are note")
        try:
            self.__service_note.sterge_nota_student_problema_service((1,3))
        except RepoPbError as ve:
            self.assertTrue(str(ve)=="Problema laborator inexistenta")
        except RepoNoteError as ve:
            self.assertTrue(str(ve)=="Nu exista note pentru problema respectiva")
    def test_service_sterge_dupa_student(self):
        self.assertEqual(len(self.__service_note), 0)
        self.__student.set_id(1)
        self.__student.set_nume("Andrei Dragos")
        self.__student.set_grup(213)
        self.__repo_st.adauga_student(self.__student)
        self.__pb.set_nr((1, 3))
        self.__pb.set_descriere("se face cmmdc")
        self.__pb.set_deadline("10/2/2000")
        self.__repo_pb.adauga_pb(self.__pb)
        nota = 10
        self.__service_note.adauga_nota_student_service(self.__pb.get_nr(), self.__student.get_id(), nota)
        self.assertEqual(len(self.__service_note), 1)
        problema2=Problema((2,1) ,"calculati","1/2/2000")
        self.__repo_pb.adauga_pb(problema2)
        nota2=9
        self.__service_note.adauga_nota_student_service(problema2.get_nr(), self.__student.get_id(), nota2)
        self.assertEqual(len(self.__service_note), 2)
        self.__service_note.sterge_nota_student_problema_service(self.__student.get_id())
        self.assertEqual(len(self.__service_note), 0)
        try:
            self.__service_note.sterge_nota_student_problema_service(self.__student.get_id())
            assert False
        except RepoNoteError as ve:
            self.assertTrue(str(ve)=="Studentul nu are note")

    def test_service_sterge_dupa_problema(self):
        self.assertEqual(len(self.__service_note), 0)

        self.__student.set_id(1)
        self.__student.set_nume("Andrei Dragos")
        self.__student.set_grup(213)
        self.__repo_st.adauga_student(self.__student)

        self.__pb.set_nr((1, 3))
        self.__pb.set_descriere("se face cmmdc")
        self.__pb.set_deadline("10/2/2000")
        self.__repo_pb.adauga_pb(self.__pb)

        nota = 10
        self.__service_note.adauga_nota_student_service(self.__pb.get_nr(), self.__student.get_id(), nota)

        student2=Student(2,"Mihai",211)
        self.__repo_st.adauga_student(student2)

        nota2=9
        self.__service_note.adauga_nota_student_service(self.__pb.get_nr(),student2.get_id(),nota2)
        self.assertEqual(len(self.__service_note), 2)

        self.__service_note.sterge_nota_student_problema_service(self.__pb.get_nr())
        self.assertEqual(len(self.__service_note), 0)
        try:
            self.__service_note.sterge_nota_student_problema_service(self.__pb.get_nr())
            assert False
        except RepoNoteError as ve:
            self.assertTrue(str(ve)=="Nu exista note pentru problema respectiva")

    def test_lista_cu_studenti_si_notele_la_o_problema_de_laborator_service(self):
        self.assertEqual(len(self.__service_note), 0)
        self.__student.set_id(1)
        self.__student.set_nume("Andrei Dragos")
        self.__student.set_grup(213)
        self.__repo_st.adauga_student(self.__student)
        self.__pb.set_nr((1, 3))
        self.__pb.set_descriere("se face cmmdc")
        self.__pb.set_deadline("10/2/2000")
        self.__repo_pb.adauga_pb(self.__pb)
        nota = 10.0
        self.__service_note.adauga_nota_student_service(self.__pb.get_nr(), self.__student.get_id(), nota)
        rez=self.__service_note.lista_cu_studenti_si_notele_la_o_problema_de_laborator_service(self.__pb.get_nr())
        self.assertTrue(rez[0].print_note_studenti()=="Id student: 1, Nume:Andrei Dragos, Nota: 10.0")
    def test_lista_studenti_cu_media_notelor_la_laborator_mai_mica_decat_cinci_service(self):
        self.assertEqual(len(self.__service_note), 0)
        self.__student.set_id(1)
        self.__student.set_nume("Andrei Dragos")
        self.__student.set_grup(213)
        self.__repo_st.adauga_student(self.__student)
        self.__pb.set_nr((1, 3))
        self.__pb.set_descriere("se face cmmdc")
        self.__pb.set_deadline("10/2/2000")
        self.__repo_pb.adauga_pb(self.__pb)
        nota = 4.0
        self.__service_note.adauga_nota_student_service(self.__pb.get_nr(), self.__student.get_id(), nota)
        rez = self.__service_note.lista_studenti_cu_media_notelor_la_laborator_mai_mica_decat_cinci_service()
        self.assertTrue(str(rez[0]) == "Id student: 1, Nume:Andrei Dragos, Media: 4.0")
