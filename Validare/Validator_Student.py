from Erori.Erori_student import ValidatorError


class ValidatorStudent(object):

    def ValidareStudent(self,student):
        erori=""
        if student.get_id()<0:
            erori+="Id invalid\n"
        if type(student.get_nume())==int or len(student.get_nume())==0 :
            erori+="Nume invalid\n"
        if student.get_grup()<=0:
            erori+="Grup invalid\n"
        if len(erori)>0:
            raise ValidatorError(erori)