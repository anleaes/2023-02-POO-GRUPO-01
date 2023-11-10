from pessoa import Pessoa

class PessoaJuridica(Pessoa):

    def __init__(self, nome, email, matricula, endereco, cnpj):
        super().__init__(nome, email, matricula, endereco)
        self._cnpj = cnpj

    def exibirNomeMatricula(self):
        print('Aluno PJ: '+ self._nome +'\nMatricula: '+ self._matricula)