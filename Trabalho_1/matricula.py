from curso import Curso
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica
class Matricula:

    def __init__(self, numero_matricula, data_matricula, curso = Curso, aluno = PessoaFisica, contratante = PessoaJuridica):
        self._numero_matricula = numero_matricula
        self._data_matricula = data_matricula
        self._curso = curso
        self._aluno = aluno
        self._contratante = contratante

    def exibirMatricula(self):
        print(f"Matricula: {self._numero_matricula} \nCurso: {self._curso._nome} \nAluno: {self._aluno._nome} \nContratante: {self._contratante._razao_social}")
        