
from Business.ServiceNote import ServiceNote
from Business.Service_problema_laborator import ServiceProbleme
from Business.Service_student import ServiceStudenti
from Persistenta.RepoNote import RepoNote
from Persistenta.RepoNote_file import Reponote_file
from Persistenta.RepoProblema_file import Repopb_file
from Persistenta.RepoProblema_laborator import RepoProbleme
from Persistenta.RepoStudenti import RepoStudenti
from Persistenta.RepoStudenti_file import RepoStudentifile
from Prezentare.UI import UI
from Teste.Testare_Note_lab import Teste_note
from Teste.Testare_Problema_Laborator import Teste_Lab
from Teste.Testare_Student import Teste
from Teste.test_pyunit_note import Test_nota
from Teste.test_pyunit_problema import Test_problema
from Teste.test_pyunit_student import Test_student

from Validare.Nota_problema_laborator import ValidatorNota
from Validare.Validare_Problema_Laborator import ValidatorPb
from Validare.Validator_Student import ValidatorStudent
import unittest

#D:\ProblemePython\Proiectlab10\Proiectlab10\Teste\test_pyunit_student.py in D:\ProblemePython\Proiectlab10\Proiectlab10\Teste
if __name__ == '__main__':
    teste = unittest.TestSuite()
    teste.addTests(unittest.makeSuite(Test_student))
    teste.addTests(unittest.makeSuite(Test_problema))
    teste.addTests(unittest.makeSuite(Test_nota))
    runner=unittest.TextTestRunner()
    runner.run(teste)

    #teste=Teste()
    #teste.run_teste()
    repo_studenti=RepoStudentifile("repostudent.txt")
    #repo_studenti=RepoStudenti()
    validator_student=ValidatorStudent()
    service_student=ServiceStudenti(repo_studenti,validator_student)

    #teste_pb=Teste_Lab()
    #teste_pb.run_teste()
    repo_probleme=Repopb_file("repopb.txt")
    #repo_probleme=RepoProbleme()
    validator_probleme=ValidatorPb()
    service_probleme=ServiceProbleme(repo_probleme,validator_probleme)

    #teste_note=Teste_note()
    #teste_note.run_teste()
    #repo_note=RepoNote()
    repo_note=Reponote_file("reponote.txt",repo_studenti,repo_probleme,"raport1.txt")

    validare_nota=ValidatorNota()
    service_note=ServiceNote(repo_studenti,repo_probleme,repo_note,validare_nota,"raport1.txt")
    consola=UI(service_student,service_probleme,service_note)
    consola.run_UI()


