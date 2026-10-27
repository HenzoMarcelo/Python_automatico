# from modulos.funcoes import saudacao, somar, subtrair
# saudacao('Henzo')
# print(somar(4,67))
# print(subtrair(33,13))

# from modulos import matematica, mensagens

# n = int(input('Digite um número inteiro: '))

# print(f'dobro: {matematica.dobro(n):.2f}')
# print(f'\nmetade: {matematica.metade(n):.2f}\n')

# nome = input('Digite seu nome: ')
# mensagens.boas_vindas(nome)

# from meu_pacote import formatador, numeros

# print(formatador.caixa_alta('Ana Maria Braga'))
# print(f'O número é par ?  {numeros.eh_par(6)}')


from perfil import usuario, validacao

nome = input()
idade = int(input())

idade_aprovada = validacao.idade_valida(idade)

if idade_aprovada:
    perfil = usuario.criar_perfil(nome, idade)
    print('\nPerfil criado!!\n')
    for chave, valor in perfil.items():
        print(f'{chave}: {valor}')
else: 
    print('Você não tem a idade mínima para criar um perfil.')
    