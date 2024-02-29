import ast

from Domain.Nota_laborator import Nota_laborator
from Persistenta.RepoNote import RepoNote


class Reponote_file(RepoNote):
    def __init__(self,repo_note,repo_studenti,repo_pb,cale_raport):
        RepoNote.__init__(self)
        self.__repo_note_fisier=repo_note
        self.__repo_studenti=repo_studenti
        self.__repo_pb=repo_pb
        self.__raport1=cale_raport
    def __len__(self):
        '''
        Afla lungimea listei de note(numarul notelor)
        :return: lungimea listei de note(numarul notelor)
        '''
        self.citeste_din_fisier()
        return len(self._note)
    def citeste_din_fisier(self):
        '''
        Citeste datele notelor din fisier
        :return:
        '''
        with open(self.__repo_note_fisier,"r") as f:
            linii=f.readlines()
            for linie in linii:
                linie=linie.strip()
                if linie!="":
                    parti=linie.split("  ")
                    id_student=int(parti[0])
                    id_pb=ast.literal_eval(parti[1])
                    nota=float(parti[2])
                    try:
                        l_st=len(self.__repo_studenti)
                        student=self.__repo_studenti.cauta_student(l_st,id_student)
                        l_pb=len(self.__repo_pb)
                        self.__repo_pb.cauta_pb(l_pb,id_pb)
                        l = []
                        l.append(id_student)
                        lista_id_pb = list(id_pb)
                        l = l + lista_id_pb
                        id_pb = tuple(l)
                        notaf = Nota_laborator(id_pb, student.get_nume(), nota)
                        self._note[id_pb] = notaf
                    except:
                        pass

    def scrie_in_fisier(self):
        '''
        Rescrie datele notelor in fisier
        :return:
        '''
        with open(self.__repo_note_fisier,"w") as f:
            for nota in self._note.values():
                f.write(str(nota)+"\n")

    def adauga_nota_repo(self,nota):
        '''
        Adauga o nota in lista de note
        :param nota: obiectul nota al clasei Nota_laborator
        :return:
        '''
        self.citeste_din_fisier()
        RepoNote.adauga_nota_repo(self,nota)
        self.scrie_in_fisier()
    def sterge_nota_repo_dupa_student(self,value):
        '''
        Sterge notele unui student sters
        :pamams value: id-ul studentului
        :return:
        :raises: RepoNoteError daca studentul nu are note cu stringul "Studentul nu are note"
        '''
        self.citeste_din_fisier()
        RepoNote.sterge_nota_repo_dupa_student(self,value)
        self.scrie_in_fisier()
    def sterge_nota_repo_dupa_problema(self,value):
        '''
        Sterge notele unui student la o probleama stearsa
        :return:
        :raises: RepoNoteError daca nu exista studenti care sa aiba note la problema respectiva cu stringul "Nu exista note pentru problema respectiva"
        '''
        self.citeste_din_fisier()
        RepoNote.sterge_nota_repo_dupa_problema(self,value)
        self.scrie_in_fisier()
    def scrie_raport1(self,rez_sort):
        with open(self.__raport1,"w") as f:
            for student in rez_sort:
                f.write(student.print_note_studenti()+"\n")

    def get_all(self):
        '''
        Creeaza lista cu toate notele
        :return: lista cu toate notele
        '''
        self.citeste_din_fisier()
        return RepoNote.get_all(self)

    """"def cmp(self, a, b, reverse):
        if a==b:
            return "egal"
        if reverse == False:
            return a > b
        if reverse == True:
            return a < b



    def poz(self, v, li, ls, key,reverse):
        ok = 0

        while li < ls:
            # if v[li].get_nume() > v[ls].get_nume():

            if self.cmp(getattr(v[li],key[0])(), getattr(v[ls],key[0])(), reverse) == True:
                v[li], v[ls] = v[ls], v[li]
                if ok != 0:
                    ok = 0
                else:
                    ok = 1
            else:
                # if v[li].get_nume() == v[ls].get_nume():
                # if v[li].get_media()>v[ls].get_media():
                if self.cmp(getattr(v[li],key[0])(), getattr(v[ls],key[0])(), reverse) == "egal" and self.cmp(getattr(v[li],key[1])(), getattr(v[ls],key[1])(), reverse) == True:
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


    def quicksort(self, v, li, ls, key,reverse):
        if li < ls:
            p = self.poz(v, li, ls,key, reverse)
            self.quicksort(v, li, p - 1, key,reverse)
            self.quicksort(v, p + 1, ls, key,reverse)

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
            elif self.cmp(lista[poz].get_nume(), lista[poz - 1].get_nume(),reverse) == "egal":
                if self.cmp(lista[poz].get_media(), lista[poz - 1].get_media(), not (reverse)) == True:
                    lista[poz], lista[poz - 1] = lista[poz - 1], lista[poz]
                    poz = poz - 1
                else:
                    poz = poz + 1

    def sortare(self, rez,cmp, metoda,key, reverse):

        if metoda == "quick_sort":
            self.quicksort(rez, 0, len(rez) - 1, key,reverse)
        elif metoda == "gnome_sort":
            self.gnomesort(rez, reverse)


    def cmp(self,a,b,reverse):
        if reverse==False:
            return a>b
        if reverse==True:
            return a<b

    def cmpegal(self,a,b):
        return a==b

    def poz(self,v, li, ls,reverse):
        ok = 0
        while li < ls:
            #if v[li].get_nume() > v[ls].get_nume():
            if self.cmp(v[li].get_nume(),v[ls].get_nume(),reverse)==True:
                v[li], v[ls] = v[ls], v[li]
                if ok != 0:
                    ok = 0
                else:
                    ok = 1
            else:
                #if v[li].get_nume() == v[ls].get_nume():
                #if v[li].get_media()>v[ls].get_media():
                if self.cmpegal(v[li].get_nume(),v[ls].get_nume())==True and self.cmp(v[li].get_media(),v[ls].get_media(),reverse)==True:
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

    def quicksort(self,v, li, ls,reverse):
        if li < ls:
            p = self.poz(v, li, ls,reverse)
            self.quicksort(v, li, p - 1,reverse)
            self.quicksort(v, p + 1, ls,reverse)

    def gnomesort(self,lista,reverse):
        poz=0
        while poz<len(lista):
            #if poz==0 or lista[poz].get_nume()>lista[poz-1].get_nume()
            if poz==0 or self.cmp(lista[poz].get_nume(), lista[poz-1].get_nume(), reverse)==True:
                poz=poz+1
            elif self.cmp(lista[poz].get_nume(),lista[poz-1].get_nume(),not(reverse)):
                    lista[poz], lista[poz - 1] = lista[poz - 1], lista[poz]
                    poz=poz-1

            #if lista[poz].get_nume()==lista[poz-1].get_nume()
            #if lista[poz].get_media()<lista[poz-1].get_media()
            elif self.cmpegal(lista[poz].get_nume(),lista[poz-1].get_nume())==True:
                    if self.cmp(lista[poz].get_media(),lista[poz-1].get_media(),not(reverse))==True:
                        lista[poz], lista[poz - 1] = lista[poz - 1], lista[poz]
                        poz=poz-1
                    else:
                        poz=poz+1



    def sortare(self,rez,metoda,reverse):
        if metoda=="quick_sort":
            self.quicksort(rez,0,len(rez)-1,reverse)
        elif metoda=="gnome_sort":
            self.gnomesort(rez,reverse)"""

