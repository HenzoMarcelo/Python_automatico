alunos_colegio = []

def adicionar_aluno():
    aluno = {
        'nome': input("Digite o nome do aluno: "),
        'idade': int(input("Digite a idade do aluno: ")),
        'nota_aluno': float(input("Digite a nota do aluno (entre 0 e 10): "))
    }
    return aluno


def listar_todos_alunos():
    # print(f'\n{alunos_colegio}\n')
    for aluno in alunos_colegio:
        print(f'\n{alunos_colegio.index(aluno) + 1} > Nome: {aluno['nome'].title()};\n    Idade: {aluno['idade']} anos;\n    Nota: {aluno['nota_aluno']}')

def buscar_aluno(nome):
    for aluno in alunos_colegio:
        if aluno['nome'].lower() == nome.lower():
            print(f'\n>>>Nome: {aluno['nome'].title()}\n>>>Idade: {aluno['idade']} anos\n>>>Nota: {aluno['nota_aluno']} pontos\n')
            return
    print("\n>>Erro: Aluno não encontrado<<")

def remover_aluno(nome_a_remover):
    for aluno in alunos_colegio:
        if aluno['nome'].lower() == nome_a_remover.lower():
            alunos_colegio.remove(aluno)
            print(f'\n>>>> O aluno "{aluno['nome'].title()}" foi removido.')
            return
    print("\nA informação digitada não foi encontrada no banco de cadastrados")

def calcular_media_notas():
    if alunos_colegio != []:
        soma = 0
        for aluno in alunos_colegio:
            soma+=aluno['nota_aluno']
        media = soma / len(alunos_colegio)
        print(f'\n>>> A média geral é: {media:.2f} pontos')
        
        return
    else:
        print('\n>>> Erro: Não há nenhum aluno para que a média seja calculada.')
    

while True:
    try:

        print('\nOpções:\n\n1. Adicionar aluno\n2. Listar todos os alunos\n3. Buscar aluno pelo nome\n4. Remover aluno\n5. Mostrar média geral das notas\n6. Sair')



        N = int(input('\nDigite o que deseja: '))
        
        match N:
            case 1:
                alunos_colegio.append(adicionar_aluno())
            case 2:
                if alunos_colegio == []:
                    print("\nNão há nenhum aluno cadastrado")
                else:
                    listar_todos_alunos()
            case 3:
                nome = input("\nNome do aluno: ")
                buscar_aluno(nome)
            case 4:
                if alunos_colegio == []:
                    print("\nO cadastro de alunos está vazio, não há ninguém para remover...")
                else:
                    nome_a_remover = input('Digite o nome do aluno: ')
                    remover_aluno(nome_a_remover)
            case 5:
                calcular_media_notas()
            case 6:
                print("\n      :)\n>>>Obrigado por utilizar nosso software. Até breve!\n\n>>>Equipe de desenvolvimento: ...LainRyzen...\n\n ^_^ \n\n")
                break
    
    except ValueError:
        print("\nO valor digitado foge dos padrões convenientemente requiditados.")