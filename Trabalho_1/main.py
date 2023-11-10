from matricula import Matricula
from curso import Curso
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

def main():

    curso = Curso('Curso de Python POO', 100)
    aluno = PessoaFisica('Nome do aluno', 'Rua A, 123', '000.000.000-00', '01/01/2000')
    contratante = PessoaJuridica('Empresa contratante','Rua B, 456','00.000.000/0000-00', 'Empresa Contratante LTDA', '01/01/1980')
    
    matricula = Matricula('123', '09/11/2023', curso, aluno, contratante)

    print("-----------------------------------------")
    matricula.exibirMatricula()
    print("-----------------------------------------")
    contratante.exibirDados()
    print("-----------------------------------------")
    aluno.exibirDados()
    


if __name__ == "__main__":
    main()