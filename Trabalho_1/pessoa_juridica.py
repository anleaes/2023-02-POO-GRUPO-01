from pessoa import Pessoa

class PessoaJuridica(Pessoa):

    def __init__(self, nome, endereco, cnpj, razao_social, data_abertura):
        super().__init__(nome, endereco)
        self._cnpj = cnpj
        self._razao_social = razao_social
        self._data_abertura = data_abertura

    def exibirDados(self):
        print(f"Pessoa Jurídica\n{self._cnpj} - {self._razao_social}\n{self._endereco}")
        