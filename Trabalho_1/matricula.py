class Matricula:

    def __init__(self, numero_matricula, data_matricula, curso, aluno, contratante):
        self._numero_matricula = numero_matricula
        self._data_matricula = data_matricula
        self._curso = curso
        self._aluno = aluno
        self._contratante = contratante

    def criarMatricula(numero_matricula, data_matricula, curso, aluno, contratante):
        Matricula._aluno = aluno
        Matricula._contratante = contratante
        Matricula._curso = curso
        Matricula._data_matricula = data_matricula
        Matricula._numero_matricula = numero_matricula