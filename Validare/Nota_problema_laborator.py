from Erori.Erori_note import ValidatorNoteError


class ValidatorNota(object):
    def validare_nota(self,nota):
        erori=""
        if nota.get_nota_lab()<=0 or nota.get_nota_lab()>=11:
            erori+="Nota problema de laborator invalida"

        if len(erori)!=0:
            raise ValidatorNoteError(erori)
