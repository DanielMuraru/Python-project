import unittest

from Business.Service_student import ServiceStudenti
from Domain.Student import Student
from Erori.Erori_student import ValidatorError, RepoError
from Persistenta.RepoStudenti_file import RepoStudentifile
from Validare.Validator_Student import ValidatorStudent


class Test_student(unittest.TestCase):
    def setUp(self):
        self.__repo_studenti = RepoStudentifile("Teste/student.txt")
        self.__validator_student = ValidatorStudent()
        self.__service_studenti = ServiceStudenti(self.__repo_studenti, self.__validator_student)
        with open("Teste/student.txt","w") as f:
            pass
    def tearDown(self):
        with open("Teste/student.txt","w") as f:
            pass
    def test_creare_student_black_box(self):
        student=Student(1,"Andrei",213)

    def test_domain(self):
        student = Student(1, "Mihai", 213)
        self.assertTrue(student.get_id()==1)
        self.assertTrue(student.get_nume()=="Mihai")
        self.assertTrue(student.get_grup()==213)
        clona_student=Student(1,"Mihai",213)
        self.assertTrue(student==clona_student)
        self.assertEqual(str(student),"1  Mihai  213")

    def test_validare(self):
        self.__validator_student = ValidatorStudent()
        self.__student_validare=Student(None,None,None)
        self.__student_validare.set_id(2)
        self.__student_validare.set_nume("Vlad")
        self.__student_validare.set_grup(215)
        self.__validator_student.ValidareStudent(self.__student_validare)

        self.__student_validare.set_id(-2)
        self.__student_validare.set_nume("")
        self.__student_validare.set_grup(0)
        try:
            self.assertFalse(self.__validator_student.ValidareStudent(self.__student_validare))
        except ValidatorError as ve:
            self.assertEqual (str(ve),"Id invalid\nNume invalid\nGrup invalid\n")
        self.__student_validare.set_id(-2)
        self.__student_validare.set_nume(23)
        self.__student_validare.set_grup(0)
        try:
            self.assertFalse(self.__validator_student.ValidareStudent(self.__student_validare))
        except ValidatorError as ve:
            self.assertEqual (str(ve),"Id invalid\nNume invalid\nGrup invalid\n")
    def test_repo_adaugare_black_box(self):
        try:
            self.__repo_studenti.adauga_student(Student(1,"Andrei",213))
        except RepoError as ve:
            self.assertTrue(str(ve)=="Student existent")
    def test_repo_adaugare(self):
        self.assertEqual(len(self.__repo_studenti),0)
        self.__student_repo = Student(None, None, None)
        self.__student_repo.set_id(1)
        self.__student_repo.set_nume("Vlad")
        self.__student_repo.set_grup(215)
        self.__repo_studenti.adauga_student(self.__student_repo)
        self.assertTrue(len(self.__repo_studenti) == 1)

        self.__acelasi_id = 1
        self.__student_repo.set_nume("Marius")
        self.__student_repo.set_grup(217)
        try:
            self.assertFalse(self.__repo_studenti.adauga_student(self.__student_repo))
        except RepoError as ve:
            self.assertTrue(str(ve) == "Student existent")
    def test_repo_cautare_black_box(self):
        try:
            self.__repo_studenti.cauta_student(0,1)
        except RepoError as ve:
            self.assertTrue(str(ve)=="Student inexistent")
    def test_repo_cautare(self):
        self.__student_repo = Student(None, None, None)
        self.__student_repo.set_id(1)
        self.__student_repo.set_nume("Vlad")
        self.__student_repo.set_grup(215)
        try:
            self.assertFalse(self.__repo_studenti.cauta_student(0,self.__student_repo.get_id()))
        except RepoError as ve:
            self.assertTrue(str(ve) == "Student inexistent")
        self.__repo_studenti.adauga_student(self.__student_repo)
        self.__repo_studenti.cauta_student(1,self.__student_repo.get_id())
    def test_repo_modificare(self):
        self.__student_repo = Student(None, None, None)
        self.__student_repo.set_id(1)
        self.__student_repo.set_nume("Vlad")
        self.__student_repo.set_grup(217)
        self.__repo_studenti.adauga_student(self.__student_repo)
        self.__repo_studenti.modifica_student(self.__student_repo)
        self.assertTrue(len(self.__repo_studenti) == 1)
        student_gasit = self.__repo_studenti.cauta_student(1,self.__student_repo.get_id())
        self.assertTrue(student_gasit.get_nume() == self.__student_repo.get_nume())

        self.__student_repo.set_id(2)
        self.__student_repo.set_nume("Razvan")
        self.__student_repo.set_grup(217)
        try:
            self.assertFalse(self.__repo_studenti.modifica_student(self.__student_repo))
        except RepoError as ve:
            self.assertTrue(str(ve) == "Student inexistent")
    def test_repo_stergere(self):
        self.__student_repo=Student(None,None,None)
        self.__student_repo.set_id(2)
        self.__student_repo.set_nume("Razvan")
        self.__student_repo.set_grup(214)
        self.__repo_studenti.adauga_student(self.__student_repo)
        self.assertTrue(len(self.__repo_studenti) == 1)
        self.__repo_studenti.sterge_student(self.__student_repo.get_id())
        self.assertTrue(len(self.__repo_studenti) == 0)
        try:
            self.assertFalse(self.__repo_studenti.sterge_student(self.__student_repo.get_id()))
        except RepoError as ve:
            self.assertTrue(str(ve) == "Student inexistent")

    def test_service_adaugare(self):
        self.assertTrue(len(self.__service_studenti) == 0)
        self.__student_service=Student(None,None,None)
        self.__student_service.set_id(1)
        self.__student_service.set_nume("Razvan")
        self.__student_service.set_grup(217)
        self.__service_studenti.adauga_student_service(self.__student_service.get_id(), self.__student_service.get_nume(), self.__student_service.get_grup())
        self.assertTrue(len(self.__service_studenti) == 1)

        self.__student_service.set_id(1)
        self.__student_service.set_nume("Andrei")
        self.__student_service.set_grup(211)
        try:
            self.assertFalse(self.__service_studenti.adauga_student_service(self.__student_service.get_id(), self.__student_service.get_nume(), self.__student_service.get_grup()))
        except RepoError as ve:
            self.assertTrue(str(ve) == "Student existent")
        self.__student_service.set_id(-1)
        self.__student_service.set_nume(23)
        self.__student_service.set_grup(0)
        try:
            self.__service_studenti.adauga_student_service(self.__student_service.get_id(),self.__student_service.get_nume(),self.__student_service.get_grup())
        except ValidatorError as ve:
            self.assertTrue(str(ve) == "Id invalid\nNume invalid\nGrup invalid\n")

    def test_service_cautare(self):

        self.__student_service = Student(None, None, None)
        self.__student_service.set_id(1)
        self.__student_service.set_nume("Andrei")
        self.__student_service.set_grup(211)
        try:
            self.assertFalse(self.__service_studenti.cauta_student_service(self.__student_service.get_id()))
        except RepoError as ve:
            self.assertTrue(str(ve) == "Student inexistent")
        self.__service_studenti.adauga_student_service(self.__student_service.get_id(),
                                                       self.__student_service.get_nume(),
                                                       self.__student_service.get_grup())
        student_gasit=self.__service_studenti.cauta_student_service(self.__student_service.get_id())
        self.assertTrue(student_gasit.get_nume()==self.__student_service.get_nume())
    def test_service_modificare(self):
        self.__student_service=Student(None,None,None)
        self.__student_service.set_id(2)
        self.__student_service.set_nume("Mihai")
        self.__student_service.set_grup(211)
        self.__service_studenti.adauga_student_service(self.__student_service.get_id(), self.__student_service.get_nume(), self.__student_service.get_grup())
        self.assertTrue(len(self.__service_studenti) == 1)

        self.__student_service.set_id(2)
        self.__student_service.set_nume("Marian")
        self.__student_service.set_grup(214)
        self.__service_studenti.modifica_student_service(self.__student_service.get_id(), self.__student_service.get_nume(), self.__student_service.get_grup())
        student_gasit = self.__service_studenti.cauta_student_service(self.__student_service.get_id())
        self.assertTrue(student_gasit.get_nume() == self.__student_service.get_nume())

        self.__student_service.set_id(4)
        self.__student_service.set_nume("Marian")
        self.__student_service.set_grup(214)
        try:
            self.assertFalse(self.__service_studenti.modifica_student_service(self.__student_service.get_id(), self.__student_service.get_nume(), self.__student_service.get_grup()))
        except RepoError as ve:
            self.assertTrue(str(ve) == "Student inexistent")
    def test_service_stergere(self):
        self.__student_service=Student(None,None,None)
        self.__student_service.set_id(1)
        self.__student_service.set_nume("Marian")
        self.__student_service.set_grup(214)
        self.__service_studenti.adauga_student_service(self.__student_service.get_id(),self.__student_service.get_nume(),self.__student_service.get_grup())
        self.__service_studenti.sterge_student_service(self.__student_service.get_id())
        self.assertTrue(len(self.__service_studenti) == 0)
        try:
            self.assertFalse(self.__service_studenti.sterge_student_service(self.__student_service.get_id()))
        except RepoError as ve:
            self.assertTrue(str(ve) == "Student inexistent")




