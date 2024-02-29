import ast

from Erori.Erori_note import RepoNoteError


class RepoNote(object):
    def __init__(self):
        self._note={}

    def __len__(self):
        return len(self._note)
    def adauga_nota_repo(self,notare):
        '''
        Adauga o nota in lista de note
        :param notare: nota
        :return:
        '''
        if notare.get_nr_lab_si_pb_si_student() in self._note:
            raise RepoNoteError("Studentul are deja o nota la o problema de laborator")
        self._note[notare.get_nr_lab_si_pb_si_student()]=notare

    def sterge_nota_repo_dupa_student(self,id):
        '''
        Sterge notele unui student sters
        :pamams id: id-ul studentului
        :return:
        '''
        l=[]
        ok=0
        for k in self._note:
            nota = self._note[k]
            nr = nota.get_nr_lab_si_pb_si_student()
            id_cautat=int(nr[0])
            if id_cautat == id:
                ok = 1
                l.append(nota.get_nr_lab_si_pb_si_student())
        if ok == 1:
            for h in l:
                del self._note[h]
        if ok==0:
            raise RepoNoteError("Studentul nu are note")

    def sterge_nota_repo_dupa_problema(self,id):
        '''
        Sterge notele unui student la o probleama stearsa
        :return:
        '''
        l=[]
        ok=0
        for k in self._note:
            nota = self._note[k]
            nr=nota.get_nr_lab_si_pb_si_student()
            id_cautat=(nr[1],nr[2])
            if id_cautat==id:
                ok=1
                l.append(nota.get_nr_lab_si_pb_si_student())
        if ok==1:
            for h in l:
                del self._note[h]
        if ok==0:
            raise RepoNoteError("Nu exista note pentru problema respectiva")

    """def scrie_raport1(self,rez_sort):
        with open("raport1.txt","w") as f:
            for nota in rez_sort:
                f.write(str(nota)+"\n")"""
    def get_all(self):
        '''
        n=numarul de note
        Caz favorabil=caz mediu=caz defavorabil
        T(n)=Suma de la 1 la n=n => Complexitatea este O(n)
        Returneaza lista de note
        :return:
        '''
        l=[]
        for k in self._note:
            nota=self._note[k]
            l.append(nota)
        return l

    """def cmp(self, a, b, reverse):
        if reverse == False:
            return a > b
        if reverse == True:
            return a < b

    def cmpegal(self, a, b):
        return a == b

    def poz(self, v, li, ls, reverse):
        ok = 0
        while li < ls:
            # if v[li].get_nume() > v[ls].get_nume():
            if self.cmp(v[li].get_nume(), v[ls].get_nume(), reverse) == True:
                v[li], v[ls] = v[ls], v[li]
                if ok != 0:
                    ok = 0
                else:
                    ok = 1
            else:
                # if v[li].get_nume() == v[ls].get_nume():
                # if v[li].get_media()>v[ls].get_media():
                if self.cmpegal(v[li].get_nume(), v[ls].get_nume()) == True and self.cmp(v[li].get_media(),
                                                                                         v[ls].get_media(),
                                                                                         reverse) == True:
                    v[li], v[ls] = v[ls], v[li]
                    if ok != 0:
                        ok = 0
                    else:
                        ok = 1
            if ok == 0:
                li = li + 1
            else:
                ls = ls - 1
        return li

    def quicksort(self, v, li, ls, reverse):
        if li < ls:
            p = self.poz(v, li, ls, reverse)
            self.quicksort(v, li, p - 1, reverse)
            self.quicksort(v, p + 1, ls, reverse)

    def gnomesort(self, lista, reverse):
        poz = 0
        while poz < len(lista):
            # if poz==0 or lista[poz].get_nume()>lista[poz-1].get_nume()
            if poz == 0 or self.cmp(lista[poz].get_nume(), lista[poz - 1].get_nume(), reverse) == True:
                poz = poz + 1
            elif self.cmp(lista[poz].get_nume(), lista[poz - 1].get_nume(), not (reverse)):
                lista[poz], lista[poz - 1] = lista[poz - 1], lista[poz]
                poz = poz - 1

            # if lista[poz].get_nume()==lista[poz-1].get_nume()
            # if lista[poz].get_media()<lista[poz-1].get_media()
            elif self.cmpegal(lista[poz].get_nume(), lista[poz - 1].get_nume()) == True:
                if self.cmp(lista[poz].get_media(), lista[poz - 1].get_media(), not (reverse)) == True:
                    lista[poz], lista[poz - 1] = lista[poz - 1], lista[poz]
                    poz = poz - 1
                else:
                    poz = poz + 1

    def sortare(self, rez, metoda, reverse):
        if metoda == "quick_sort":
            self.quicksort(rez, 0, len(rez) - 1, reverse)
        elif metoda == "gnome_sort":
            self.gnomesort(rez, reverse)"""

