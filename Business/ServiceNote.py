import operator

from Domain.DTO import DTO
from Domain.Nota_laborator import Nota_laborator
from Sortari.Sorts import sortare, cmp, cmpnou


class ServiceNote(object):
    def __init__(self,repo_studenti,repo_lab,repo_note,validare_nota,cale_raport):
        self.__repo_studenti_file=repo_studenti
        self.__repo_lab_fisier=repo_lab
        self.__repo_note_fisier=repo_note
        self.__validare_nota=validare_nota
        self.__raport1=cale_raport
    def __len__(self):
        '''
        Afla lungimea listei de note
        :return: lungimea listei de note
        '''
        return len(self.__repo_note_fisier)

    def adauga_nota_student_service(self,nr_lab_pb,id_student,nota):
        '''
        Adauga nota unui student la un laborator
        :param nr_lab_pb_student:id student ,numarul laboratorului si numarul problemei
        :param nota: int,nota adaugata studentului
        :return:
        '''

        student=self.__repo_studenti_file.cauta_student(len(self.__repo_studenti_file),id_student)
        self.__repo_lab_fisier.cauta_pb(len(self.__repo_lab_fisier),nr_lab_pb)
        l=[]
        l.append(id_student)
        lista_nr_lab_pb=list(nr_lab_pb)
        l=l+lista_nr_lab_pb
        nr_lab_pb_student=tuple(l)
        nume=student.get_nume()
        notare=Nota_laborator(nr_lab_pb_student,nume,nota)
        self.__validare_nota.validare_nota(notare)
        self.__repo_note_fisier.adauga_nota_repo(notare)

    def sterge_nota_student_problema_service(self,notare):
        '''
        Sterge notele unui student sters din lista de studenti sau la o problema de laborator stearsa din lista
        :param notare: id-ul int al studentului sau tuple de numarul laboratorului si numarul problemei de laborator
        :return:
        :raises:RepoError daca obiectul student cu atributul id de tip int nu exista in lista de studenti cu stringul"Student inexistent"
                RepoNoteError daca obiectul student cu atributul id de tip int nu are note cu stringul"Studentul nu are note"
                RepoPbError daca obiectul problema cu atribulul tuple(numar laborator,numar problema de laborator) nu exista in lista de probleme cu stringul"Problema laborator inexistenta"
                RepoNoteError daca obiectul problema cu atribulul tuple(numar laborator,numar problema de laborator) nu are atribuite note cu stringul"Nu exista note pentru problema respectiva"
        '''
        if type(notare)==int:
            self.__repo_note_fisier.sterge_nota_repo_dupa_student(notare)
        if type(notare)==tuple:
            self.__repo_note_fisier.sterge_nota_repo_dupa_problema(notare)
    def lista_cu_studenti_si_notele_la_o_problema_de_laborator_service(self,nr_pb_lab):
        '''
        n=lungimea listei de note
        m=numarul de note al problemei
        Caz favorabil=caz mediu=caz defavorabil
        T(n)=suma de la 1 la n de 1 + suma de la 1 la m de 1=n+m=> Complexiteatea este O(n+m)
        Creeaza statistica cu lista de studenti si notele lor la o problema de laborator dat,ordonat alfabetic dupa nume si scor
        :return:lista de studenti si notele lor la o problema de laborator dat,ordonat alfabetic dupa nume si scor
        '''
        toate_notele=self.__repo_note_fisier.get_all()
        situatie_studenti={}
        for nota in toate_notele:
            id_nota=nota.get_nr_lab_si_pb_si_student()
            nr_pb=(id_nota[1],id_nota[2])
            if nr_pb==nr_pb_lab:
                id_student=id_nota[0]
                if id_student not in situatie_studenti:
                    situatie_studenti[id_student]=nota.get_nota_lab()
        rez=[]
        for id_student in situatie_studenti:
            student1=self.__repo_studenti_file.cauta_student(len(self.__repo_studenti_file),id_student)
            nume=student1.get_nume()
            nota_student=situatie_studenti[id_student]
            student2=DTO(id_student,nume,nota_student)
            rez.append(student2)
        #rez_sort=sorted(rez,key=lambda x:(x.get_nume(),x.media))

        #sortare(rez,"gnome_sort",comparator=cmp,key=("get_nume","get_media"),reverse=False)
        sortare(rez,"quick_sort",comparator=cmpnou,key=lambda x:(x.get_nume(),x.media),reverse=False)
        #self.__repo_note_fisier.sortare(rez,"gnome_sort",reverse=False)
        #self.__repo_note_fisier.scrie_raport1(rez_sort)
        #return rez_sort
        return rez

    def lista_studenti_cu_media_notelor_la_laborator_mai_mica_decat_cinci_service(self):
        '''
        n=lungimea listei de note
        m=numarul de studenti care au nota
        Caz favorabil=caz mediu=caz defavorabil
        T(n)=suma de la 1 la n de 1 + suma de la 1 la m de 1=n+m=> Complexiteatea este O(n+m)

        Creeaza statistica cu studentii cu media notelor la laborator mai mica decat 5
        :return:lista de studenti cu media notelor la laborator mai mica decat 5
        '''
        toate_notele=self.__repo_note_fisier.get_all()
        situatie_studenti={}
        for nota in toate_notele:
            id_nota=nota.get_nr_lab_si_pb_si_student()
            id_student=id_nota[0]
            if id_student not in situatie_studenti:
                situatie_studenti[id_student]=[]
            situatie_studenti[id_student].append(nota.get_nota_lab())
        rez=[]
        for id_student in situatie_studenti:
            student1=self.__repo_studenti_file.cauta_student(len(self.__repo_studenti_file),id_student)
            nume=student1.get_nume()
            medie=float(sum(situatie_studenti[id_student])/len(situatie_studenti[id_student]))
            student2=DTO(id_student,nume,round(medie,2))
            if medie<5.0:
                rez.append(student2)
        return rez

    def lista_studenti_cu_media_notelor_la_laborator_minim_cinci_service(self):
        '''
        Creeaza o lista cu studentii care au media notelor mai mare decat cinci
        :return:lista studenti cu media notelor la laborator mai mare decat 5
        '''
        toate_notele = self.__repo_note_fisier.get_all()
        situatie_studenti = {}
        for nota in toate_notele:
            id_nota = nota.get_nr_lab_si_pb_si_student()
            id_student = id_nota[0]
            if id_student not in situatie_studenti:
                situatie_studenti[id_student] = []
            situatie_studenti[id_student].append(nota.get_nota_lab())
        rez = []
        for id_student in situatie_studenti:
            student1 = self.__repo_studenti_file.cauta_student(len(self.__repo_studenti_file),id_student)
            nume = student1.get_nume()
            medie = float(sum(situatie_studenti[id_student]) / len(situatie_studenti[id_student]))
            student2 = DTO(id_student, nume, round(medie, 2))
            if medie >= 5.0:
                rez.append(student2)
        return rez
    def get_all(self):
        '''
        Creeaza lista cu toate notele studentilor
        :return:
        '''
        return self.__repo_note_fisier.get_all()