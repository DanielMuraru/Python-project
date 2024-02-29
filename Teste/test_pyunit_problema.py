import unittest

from Business.Service_problema_laborator import ServiceProbleme
from Domain.Problema_laborator import Problema
from Erori.Erori_problema_laborator import ValidatorPbError, RepoPbError
from Persistenta.RepoProblema_file import Repopb_file
from Validare.Validare_Problema_Laborator import ValidatorPb


class Test_problema(unittest.TestCase):
    def setUp(self):
        self.__repo_pb=Repopb_file("Teste/probleme.txt")
        self.__validare=ValidatorPb()
        self.__service_pb=ServiceProbleme(self.__repo_pb,self.__validare)
        with open("Teste/probleme.txt","w") as f:
            pass
        self.__problema=Problema(None,None,None)
    def tearDown(self):
        with open("Teste/probleme.txt","w") as f:
            pass

    def test_domainI(self):
        self.__problema.set_nr((1,3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.assertTrue(self.__problema.get_nr()==(1,3))
        self.assertTrue(self.__problema.get_descriere()=="se face cmmdc")
        self.assertTrue(self.__problema.get_deadline()=="22/2/2000")
        self.assertTrue(str(self.__problema)=="(1, 3)  se face cmmdc  22/2/2000")
        clona_problema=Problema((1,3),"calculati","22/2/2000")
        self.assertTrue(self.__problema==clona_problema)
    def test_validare(self):
        self.__problema.set_nr((1, 3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.assertTrue(self.__validare.valideaza(self.__problema)==None)
        self.__problema.set_nr((-1,-2))
        self.__problema.set_descriere(23)
        self.__problema.set_deadline("")
        try:
            self.assertFalse(self.__validare.valideaza(self.__problema))
        except ValidatorPbError as ve:
            self.assertTrue(str(ve)=="Numar laborator invalid\nNumar problema invalid\nNu a fost introdusa descrierea\nNu a fost introdus un deadline\n")
        self.__problema.set_deadline("-1/0/-2")
        try:
            self.assertFalse(self.__validare.valideaza(self.__problema))
        except ValidatorPbError as ve:
            self.assertTrue(str(ve)=="Numar laborator invalid\nNumar problema invalid\nNu a fost introdusa descrierea\nZiua deadline invalida\nLuna deadline invalida\nAn deadline invalid\n")

    def test_repo_adaugare(self):
        self.assertEqual(len(self.__repo_pb),0)
        self.__problema.set_nr((1, 3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.assertTrue(self.__repo_pb.adauga_pb(self.__problema)==None)
        self.assertEqual(len(self.__repo_pb), 1)
        try:
            self.__repo_pb.adauga_pb(self.__problema)
            assert False
        except RepoPbError as ve:
            self.assertTrue(str(ve)=="Problema laborator existenta")

    def test_repo_stergere(self):
        self.assertEqual(len(self.__repo_pb), 0)
        self.__problema.set_nr((1, 3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.__repo_pb.adauga_pb(self.__problema)
        self.assertEqual(len(self.__repo_pb), 1)
        self.__repo_pb.sterge_pb(self.__problema.get_nr())
        self.assertEqual(len(self.__repo_pb),0)
        try:
            self.__repo_pb.sterge_pb(self.__problema.get_nr())
            assert False
        except RepoPbError as ve:
            self.assertTrue(str(ve)=="Problema laborator inexistenta")

    def test_repo_cautare(self):
        self.assertEqual(len(self.__repo_pb), 0)
        self.__problema.set_nr((1, 3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.__repo_pb.adauga_pb(self.__problema)
        self.assertEqual(len(self.__repo_pb), 1)
        pb_gasita=self.__repo_pb.cauta_pb(1,(1, 3))
        self.assertTrue(self.__problema==pb_gasita)
        try:
            self.__repo_pb.cauta_pb(1,(2,3))
            assert False
        except RepoPbError as ve:
            self.assertTrue(str(ve)=="Problema laborator inexistenta")

    def test_repo_modificare(self):
        self.assertEqual(len(self.__repo_pb), 0)
        self.__problema.set_nr((1, 3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.__repo_pb.adauga_pb(self.__problema)
        self.assertEqual(len(self.__repo_pb), 1)
        pb_cu_alte_date=Problema((1,3),"calculati","10/2/2000")
        self.__repo_pb.modifica_pb(pb_cu_alte_date)
        pb_modificata=self.__repo_pb.cauta_pb(1,(1, 3))
        self.assertTrue(pb_modificata.get_descriere()==pb_cu_alte_date.get_descriere())
        pb_inexistenta=Problema((2,3),None,None)
        try:
            self.__repo_pb.modifica_pb(pb_inexistenta)
            assert False
        except RepoPbError as ve:
            self.assertTrue(str(ve)=="Problema laborator inexistenta")

    def test_service_adaugare(self):
        self.assertEqual(len(self.__service_pb), 0)
        self.__problema.set_nr((1, 3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.__service_pb.adauga_pb_service(self.__problema.get_nr(),self.__problema.get_descriere(),self.__problema.get_deadline())
        self.assertEqual(len(self.__service_pb), 1)
        try:
            self.__service_pb.adauga_pb_service(self.__problema.get_nr(),self.__problema.get_descriere(),self.__problema.get_deadline())
        except RepoPbError as ve:
            self.assertTrue(str(ve)=="Problema laborator existenta")
        self.__problema.set_nr((-1, -3))
        self.__problema.set_descriere(23)
        self.__problema.set_deadline("")
        try:
            self.__service_pb.adauga_pb_service(self.__problema.get_nr(),self.__problema.get_descriere(),self.__problema.get_deadline())
            assert False
        except ValidatorPbError as ve:
            self.assertTrue(str(ve)=="Numar laborator invalid\nNumar problema invalid\nNu a fost introdusa descrierea\nNu a fost introdus un deadline\n")
        self.__problema.set_nr((0, -2))
        self.__problema.set_descriere("")
        self.__problema.set_deadline("-2/-1/0")
        try:
            self.__service_pb.adauga_pb_service(self.__problema.get_nr(), self.__problema.get_descriere(),self.__problema.get_deadline())
            assert False
        except ValidatorPbError as ve:
            self.assertTrue(str(ve)=="Numar laborator invalid\nNumar problema invalid\nNu a fost introdusa descrierea\nZiua deadline invalida\nLuna deadline invalida\nAn deadline invalid\n")

    def test_service_stergere(self):
        self.assertEqual(len(self.__service_pb), 0)
        self.__problema.set_nr((1, 3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.__service_pb.adauga_pb_service(self.__problema.get_nr(), self.__problema.get_descriere(),self.__problema.get_deadline())
        self.assertEqual(len(self.__service_pb), 1)
        self.__service_pb.sterge_pb_service((1,3))
        self.assertEqual(len(self.__service_pb),0)
        try:
            self.__service_pb.sterge_pb_service((1, 3))
            assert False
        except RepoPbError as ve:
            self.assertTrue(str(ve)=="Problema laborator inexistenta")

    def test_service_cautare(self):
        self.assertEqual(len(self.__service_pb), 0)
        self.__problema.set_nr((1, 3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.__service_pb.adauga_pb_service(self.__problema.get_nr(), self.__problema.get_descriere(),self.__problema.get_deadline())
        self.assertEqual(len(self.__service_pb), 1)
        pb_gasita=self.__service_pb.cauta_pb_service((1,3))
        self.assertTrue(self.__problema==pb_gasita)
        try:
            self.__service_pb.cauta_pb_service((2,3))
            assert False
        except RepoPbError as ve:
            self.assertTrue(str(ve)=="Problema laborator inexistenta")

    def test_service_modificare(self):
        self.assertEqual(len(self.__service_pb), 0)
        self.__problema.set_nr((1, 3))
        self.__problema.set_descriere("se face cmmdc")
        self.__problema.set_deadline("22/2/2000")
        self.__service_pb.adauga_pb_service(self.__problema.get_nr(), self.__problema.get_descriere(),self.__problema.get_deadline())
        self.assertEqual(len(self.__service_pb), 1)
        pb_cu_date_modificate=Problema((1,3),"calculati","10/2/2000")
        self.__service_pb.modifica_pb_service(pb_cu_date_modificate.get_nr(),pb_cu_date_modificate.get_descriere(),pb_cu_date_modificate.get_deadline())
        pb_gasita=self.__service_pb.cauta_pb_service((1,3))
        self.assertTrue(pb_gasita.get_descriere()==pb_cu_date_modificate.get_descriere())
        pb_invalida=Problema((-1,-3),23,"")
        try:
            self.__service_pb.modifica_pb_service(pb_invalida.get_nr(),pb_invalida.get_descriere(),pb_invalida.get_deadline())
            assert False
        except ValidatorPbError as ve:
            self.assertTrue(str(ve)=="Numar laborator invalid\nNumar problema invalid\nNu a fost introdusa descrierea\nNu a fost introdus un deadline\n")
        pb_invalida = Problema((-1, -3), "", "-1/0/0")
        try:
            self.__service_pb.modifica_pb_service(pb_invalida.get_nr(), pb_invalida.get_descriere(),pb_invalida.get_deadline())
            assert False
        except ValidatorPbError as ve:
            self.assertTrue(
                str(ve) == "Numar laborator invalid\nNumar problema invalid\nNu a fost introdusa descrierea\nZiua deadline invalida\nLuna deadline invalida\nAn deadline invalid\n")
        


