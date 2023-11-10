from matricula import Matricula
from curso import Curso
from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

def main():

    curso = Curso('Curso de Python POO', 100)
    aluno1 = PessoaFisica('Nome do aluno', 'Rua A, 123', '000.000.000-00', '01/01/2000')
    
    matricula = Matricula.criarMatricula('123', '09/11/2023', curso, aluno1)



    pf1 = PessoaFisica('Pessoa fisica 1', 'teste1@teste.com', '1', 'Rua A, 1000', '000.000.000-00', '01/01/2001')
    pf2 = PessoaFisica('Pessoa fisica 2', 'teste2@teste.com', '2', 'Rua B, 500', '000.000.000-00', '10/05/2005')

    pj1 = PessoaJuridica('Pessoa juridica 1', 'teste1@empresa.com', '3', 'Rua da empresa, 100', '00.000.000/0000-00')
    pj2 = PessoaJuridica('Pessoa juridica 2', 'teste2@empresa.com', '4', 'Rua da empresa, 100', '00.000.000/0000-00')

    cursoPf1 = Curso('Curso PF 1', 10, 'Presencial', pf1)
    cursoPf2 = Curso('Curso PF 2', 10, 'Presencial', pf2)
    
    cursoPj1 = Curso('Curso PJ 1', 50, 'EAD', pj1)
    cursoPj2 = Curso('Curso PJ 2', 50, 'EAD', pj2)


    pf1.exibirNomeMatricula()
    pf2.exibirNomeMatricula()

    pj1.exibirNomeMatricula()
    pj2.exibirNomeMatricula()

if __name__ == "__main__":
    main()