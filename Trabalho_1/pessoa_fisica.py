from pessoa import Pessoa

class PessoaFisica(Pessoa):

    def __init__(self, nome, endereco, cpf, data_nascimento):
        super().__init__(nome, endereco)
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        
    def exibirDados(self):
        print(f"Pessoa Física\n{self._nome} - {self._cpf}")