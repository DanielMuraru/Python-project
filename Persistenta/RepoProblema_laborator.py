from Domain.Problema_laborator import Problema
from Erori.Erori_problema_laborator import RepoPbError


class RepoProbleme(object):
    def __init__(self):
        self._probleme={}

    def __len__(self):
        '''
        Afla lungimea listei de probleme
        :return: rez:int
        '''
        return len(self._probleme)

    def adauga_pb(self,pb_de_adaugat):
        '''
        Adauga problema de laborator in lista de probleme de laborator
        :param pb_de_adaugat: problema de laborator
        :return:
        :raises: RepoPbError daca exista deja problema de la laborator
        '''
        if pb_de_adaugat.get_nr() in self._probleme:
            raise RepoPbError("Problema laborator existenta")
        self._probleme[pb_de_adaugat.get_nr()]=pb_de_adaugat

    def modifica_pb(self, pb_de_modificat):
        '''
        Modifica datele unei probleme de laborator
        :param pb_de_modificat: problema de laborator
        :return:
        :raises RepoPbError daca problema de la laborator nu exista
        '''
        if pb_de_modificat.get_nr() not in self._probleme:
            raise RepoPbError("Problema laborator inexistenta")
        self._probleme[pb_de_modificat.get_nr()]=pb_de_modificat

    def cauta_pb(self, l,pb_de_cautat):
        '''
        Cauta o problema de laborator dupa numarul de laborator si numarul problemei
        :param pb_de_cautat: numarul de laborator si numarul problemei
        :return:
        :raises RepoPbError daca problema de la laborator nu exista
        '''
        """if pb_de_cautat not in self._probleme:
            raise RepoPbError("Problema laborator inexistenta")
        return self._probleme[pb_de_cautat]"""
        return self.cauta_pb_rec(l,pb_de_cautat)

    def cauta_pb_rec(self,l,pb_de_cautat):
        if l==0:
            raise RepoPbError("Problema laborator inexistenta")
        pb=list(self._probleme.values())
        problema=pb[l-1]
        if problema.get_nr()==pb_de_cautat:
            return problema
        return self.cauta_pb_rec(l-1,pb_de_cautat)

    def sterge_pb(self, pb_de_cautat):
        '''
        Sterge o problema aleasa
        :param pb_de_cautat: numarul de laborator si numarul problemei
        :return:
        :raises RepoPbError daca problema de la laborator nu exista
        '''
        if pb_de_cautat not in self._probleme:
            raise RepoPbError("Problema laborator inexistenta")
        del self._probleme[pb_de_cautat]

    """def get_allpb(self):
        '''
        Creeaza lista de probleme
        :return: rez:lista de probleme
        '''
        l=[]
        for k in self._probleme:
            problema=self._probleme[k]
            l.append(problema)
        return l"""
    def get_allpb(self,l,rez):
        '''
        Creeaza o lista cu toti studentii
        :return: rez:lista de studenti
        '''
        return self.get_allpb_rec(l,rez)


    def get_allpb_rec(self,l,rez):
        '''
        Creeaza o lista cu toti studentii
        :return: rez:lista de studenti
        '''
        if l==0:
            return rez
        pb=list(self._probleme.values())
        problema=pb[l-1]
        rez.append(problema)
        self.get_allpb_rec(l-1,rez)