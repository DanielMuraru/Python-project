import ast

from Domain.Problema_laborator import Problema
from Persistenta.RepoProblema_laborator import RepoProbleme


class Repopb_file(RepoProbleme):
    def __init__(self,pbtxt):
        RepoProbleme.__init__(self)
        self.__repo_pb_fisier=pbtxt

    def __citeste_din_fisier(self):
        '''
        Citeste datele fiecarei probleme din fisier
        :return:
        '''
        with open(self.__repo_pb_fisier,"r") as f:
            linii=f.readlines()
            for linie in linii:
                linie=linie.strip()
                if linie!="":
                    parti=linie.split("  ")
                    id_pb=ast.literal_eval(parti[0])
                    descriere=parti[1]
                    deadline=parti[2]
                    try:
                        problema=Problema(id_pb,descriere,deadline)
                        self._probleme[id_pb]=problema
                    except:
                        pass
    def __scrie_in_fisier(self):
        '''
        Rescrie datele fiecarei probleme in fisier
        :return:
        '''
        with open(self.__repo_pb_fisier,"w") as f:
            for problema in self._probleme.values():
                f.write(str(problema)+"\n")

    def adauga_pb(self,problema):
        '''
        Adauga problema de laborator in lista de probleme de laborator
        :param problema: problema de laborator
        :return:
        :raises: RepoPbError daca exista deja problema de la laborator cu stringul "Problema laborator existenta"
        '''
        self.__citeste_din_fisier()
        RepoProbleme.adauga_pb(self,problema)
        self.__scrie_in_fisier()
    def sterge_pb(self,value):
        '''
        Sterge o problema aleasa
        :param value: numarul de laborator si numarul problemei (de tip tuple)
        :return:
        :raises RepoPbError daca problema de la laborator nu exista cu stringul "Problema laborator inexistenta"
        '''
        self.__citeste_din_fisier()
        RepoProbleme.sterge_pb(self,value)
        self.__scrie_in_fisier()
    def modifica_pb(self,problema):
        '''
        Modifica datele unei probleme de laborator
        :param problema: problema de laborator cu datele modificate
        :return:
        :raises RepoPbError daca problema de la laborator nu exista cu stringul "Problema laborator inexistenta"
        '''
        self.__citeste_din_fisier()
        RepoProbleme.modifica_pb(self,problema)
        self.__scrie_in_fisier()
    def cauta_pb(self,l,value):
        '''
        Cauta o problema de laborator dupa numarul de laborator si numarul problemei
        :param value: numarul de laborator si numarul problemei de tip tuple
        :return:
        :raises RepoPbError daca problema de la laborator nu exista cu stringul "Problema laborator inexistenta"
        '''
        self.__citeste_din_fisier()
        return RepoProbleme.cauta_pb(self,l,value)
    def __len__(self):
        '''
        Afla lungimea listei de probleme
        :return:
        '''
        self.__citeste_din_fisier()
        return len(self._probleme)
    def get_allpb(self,l,rez):
        '''
        Creeaza lista de probleme
        :return: lista de probleme
        '''
        self.__citeste_din_fisier()
        return RepoProbleme.get_allpb(self,l,rez)


