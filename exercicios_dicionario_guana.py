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
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking: list = list()
print('Valores sorteados:')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
        sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
        print(f'  {i+1}° lugar: {v[0]} com {v[1]}.')
        sleep(1)