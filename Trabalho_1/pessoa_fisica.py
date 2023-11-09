from pessoa import Pessoa

class PessoaFisica(Pessoa):

    def __init__(self, nome, email, matricula, endereco, cpf, data_nascimento):
        super().__init__(nome, email, matricula, endereco)
        self._cpf = cpf
        self._data_nascimento = data_nascimento
    
    def exibirNomeMatricula(self):
        print('Aluno PF: '+ self._nome +'\nMatricula: '+ self._matricula)