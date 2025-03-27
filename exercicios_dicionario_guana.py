# correcao 90
# aluno = {}
# aluno['nome']: str = str(input('Nome: '))
# aluno['media']: float = float(input(f'Média de {aluno["nome"]}: '))
# if aluno['media'] >= 7:
#         aluno['situacao'] = 'Aprovado'
# elif 5 <= aluno['media'] < 7:
#         aluno['situacao'] = 'Recuperação'
# else:
#         aluno['situacao'] = 'Reprovado'
# print('-=' * 30)
# for k, v in aluno.items():
#         print(f'  - {k} é igual a {v}')

# ex 91
# from random import randint
# from time import sleep
# num: dict = {}
# ordem: int = 0
# for v in range(1, 5):
#         num[f'jogador{v}'] = randint(1,6)
#         print(f'  O jogador{v} tirou {num[f'jogador{v}']}')
#         sleep(1)
# print('O ranking dos jogadores: ')
# ordenado: dict = dict(sorted(num.items(), key=lambda item: item[1], reverse=True))
# for k, v in ordenado.items():
#         ordem += 1
#         print(f'  {ordem}° lugar: {k} com {v}')
#         sleep(1)

# correcao ex 91
# from random import randint
# from time import sleep
# from operator import itemgetter
# jogo = {'jogador1': randint(1, 6),
#         'jogador2': randint(1, 6),
#         'jogador3': randint(1, 6),
#         'jogador4': randint(1, 6)}
# ranking: list = list()
# print('Valores sorteados:')
# for k, v in jogo.items():
#         print(f'{k} tirou {v} no dado.')
#         sleep(1)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print('-=' * 30)
# print(' == RANKING DOS JOGADORES ==')
# for i, v in enumerate(ranking):
#         print(f'  {i+1}° lugar: {v[0]} com {v[1]}.')
#         sleep(1)

# ex 92
# import datetime

# ficha_trabalho: dict = {}
# ficha_trabalho['nome']: str = str(input('Nome: '))
# ano_nascimento: int = int(input('Ano de Nascimento: '))
# ficha_trabalho['idade']: int = datetime.datetime.now().year - ano_nascimento
# ficha_trabalho['ctps']: str = str(input('Número da Carteira de Trabalho (Digite 0 quando não tiver): '))
# if not ficha_trabalho['ctps'] == '0':
#     ficha_trabalho['contratacao']: int = int(input('Ano de contratação: '))
#     ficha_trabalho['salario']: float = float(input('Salário: R$ '))
#     ficha_trabalho['aposentadoria']: int = datetime.datetime.now().year - ficha_trabalho['contratacao']
# print('-=' * 30)
# for k, v in ficha_trabalho.items():
#     print(f'{k} tem o valor {v}')

# correcao ex 92
# from datetime import datetime
# dados = dict()
# dados['nome'] = str(input('Nome: '))
# nasc = int(input('Ano de Nascimento: '))
# dados['idade'] = datetime.now().year - nasc
# dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
# if dados['ctps'] != 0:
#     dados['contratacao'] = int(input('Ano de Contratação: '))
#     dados['salario'] = float(input('Salário: R$' ))
#     dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
# print('-=' * 30)
# for k, v in dados.items():
#     print(f'  - {k} tem o valor {v}')

# ex 93
# dados: dict = {}
# gols: list = []
# dados['nome']: str = str(input('Nome do Jogador: '))
# partidas: int = int(input(f'Quantas partidas {dados['nome']} jogou: '))
# for g in range(0, partidas):
#     gols.append(int(input(f'Quantos gols na partida {g + 1}?')))
# dados['gols']: list = gols
# dados['total']: int = sum(gols)
# print('-=' * 30)   
# print(dados)
# for k, v in dados.items():
#     print(f'O campo {k} tem o valor {v}.')
# print('-='*30)
# print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
# for p, v in enumerate(gols):
#      print(f'   => Na partida {p + 1}, fez {v} gols.')
# print(f'Foi um total de {dados["total"]} gols.')

# correcao ex 93
# jogador = dict()
# partidas = list()
# jogador['nome'] = str(input('Nome do jogador: '))
# tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
# for c in range(0, tot):
#     partidas.append(int(input(f'        Quantos gols na partida {c}? ')))
# jogador['gols'] = partidas[:]
# jogador['total'] = sum(partidas)
# print('-=' * 30)
# print(jogador)
# print('-=' * 30)
# for k, v in jogador.items():
#     print(f'O campo {k} tem o valor {v}')
# print('-=' * 30)
# print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
# for i, v in enumerate(jogador['gols']):
#     print(f'    => Na partida {i}, fez {v} gols.')
# print(f'Foi um total de {jogador["total"]} gols.')

# correcao ex 94
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 60)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
