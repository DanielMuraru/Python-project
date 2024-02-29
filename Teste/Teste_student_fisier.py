from Persistenta.RepoStudenti_file import RepoStudentifile


class Teste_din_fisier_student():

    def teste_repo_fisier(self):
        fisier="Teste/student.txt"
        repo=RepoStudentifile(fisier)
        assert len(repo)==0
    def run_teste(self):
        self.teste_repo_fisier()

