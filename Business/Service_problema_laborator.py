from Domain.Problema_laborator import Problema

class ServiceProbleme(object):
    def __init__(self,repo_probleme,validator_pb):
        self.__repo_probleme_fisier=repo_probleme
        self.__validator_pb=validator_pb

    def __len__(self):
        '''
        Afla lungimea listei de probleme
        :return: rez:lungimea int a listei de probleme
        '''
        return len(self.__repo_probleme_fisier)

    def adauga_pb_service(self, nr,descriere,deadline):
        '''
        Adauga problema in lista de probleme
        :param nr: numarul laboratorului si numarul problemei
        :param descriere: descrierea problemei
        :param deadline: deadline-ul problemei
        :return:
        :raises: ValidatorError daca datele introduse sunt invalide
                 RepoPbError daca exista deja problema de la laborator
        '''
        problema=Problema(nr,descriere,deadline)
        self.__validator_pb.valideaza(problema)
        self.__repo_probleme_fisier.adauga_pb(problema)

    def cauta_pb_service(self, nr):
        '''
        Cauta problema de laborator aleasa
        :param nr: numarul laboratorului si numarul problemei alese
        :return: problema aleasa
        :raises: RepoPbError daca problema de la laborator nu exista
        '''
        l=len(self.__repo_probleme_fisier)
        return self.__repo_probleme_fisier.cauta_pb(l,nr)

    def modifica_pb_service(self, nr,descriere, deadline):
        '''
        Modifica problema de laborator aleasa
        :param nr: numarul laboratorului si numarul problemei
        :param descriere: descrierea string a problemei
        :param deadline: deadline-ul string al problemei
        :return: rez:lista de probleme cu problema modificata
        :raises: RepoPbError daca problema de la laborator nu exista
        '''
        problema=Problema(nr,descriere,deadline)
        self.__validator_pb.valideaza(problema)
        return self.__repo_probleme_fisier.modifica_pb(problema)

    def sterge_pb_service(self, nr):
        '''
        Sterge problema de laborator aleasa
        :param nr: numarul laboratorului si numarul problemei
        :return:
        :raises: RepoPbError daca problema de la laborator nu exista
        '''
        self.__repo_probleme_fisier.sterge_pb(nr)

    def get_allpb_service(self):
        '''
        Creeaza o lista cu toate problemele
        :return: rez:lista cu toate problemele
        '''
        rez=[]
        l=len(self.__repo_probleme_fisier)
        self.__repo_probleme_fisier.get_allpb(l,rez)
        return rez