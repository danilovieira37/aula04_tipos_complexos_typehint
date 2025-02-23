# 78
# lista: list = []
# for n in range(0,5):
#     lista.append(int(input(f'Digite um valor para a Posição {n}: ')))
# print('=-' * 20)
# print(f'Você digitou os valores {lista}')
# print(f'O maior valor digitado foi {max(lista)} nas posições', end=' ')
# for p, v in enumerate(lista):
#     if v == max(lista):
#         print(f'{p}...', end=' ')
# print(f'\nO menor valor digitado foi {min(lista)} nas posições', end=' ')
# for p, v in enumerate(lista):
#     if v == min(lista):
#         print(f'{p}...', end=' ')

# correção 78:
# listanum = []
# maior: int = int(0)
# menor: int = int(0)
# for c in range(0, 5):
#     listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
#     if c == 0:
#         maior = menor = listanum[c]
#     else:
#         if listanum[c] > maior:
#             maior = listanum[c]
#         if listanum[c] < menor:
#             menor = listanum[c]
# print('=-' * 30)
# print(f'Você digitou os valores {listanum}')
# print(f'O maior valor digitado foi {maior} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if listanum[i] == maior:
#         print(f'{i}...', end='')
# print()
# print(f'O maior valor digitado foi {menor} nas posições ', end='')
# for i, v in enumerate(listanum):
#     if listanum[i] == menor:
#         print(f'{i}...', end='')
# print()



# 79
# lista: list = []
# continuar: str = 's'
# while continuar.lower() == 's':
#     while True: 
#         try: 
#             v: int = int(input(f'Digite um valor: '))
#             break
#         except ValueError:
#             print('Você não digitou um valor, por favor digite um valor: ')
#     if v in lista:
#         print('Valor duplicado! Não vou adicionar...')        
#     else:
#         lista.append(v)
#         print('Valor adicionado com sucesso...')    
#     continuar: str = input('Quer Continuar: [S/N]: ').strip()
#     while continuar not in ['S', 's', 'N', 'n']:
#         print('Opção inválida. Por favor, digite "S" para sim ou "N" para não.')
#         continuar: str = input('Quer Continuar: [S/N]: ').strip()
# lista.sort()
# print(f'Você digitou os valores {lista}')

# 80
# lista: list = []
# valor: int = int(input(f'Digite um valor: '))
# lista.append(valor)
# print('Adicionado ao final da lista...')
# for v in range(0,4):
#     valor: int = int(input(f'Digite um valor: '))
#     for n in lista:
#         if valor < n:
#             lista.insert(lista.index(n), valor)
#             print(f'Adicionado na posição {lista.index(valor)} da lista...')
#             break
#     if valor > max(lista):
#         lista.insert(max(lista), valor)
#         print(f'Adicionado na posição {lista.index(valor)} da lista...')
# print('-=' * 30)
# print(f'Os valores digitados em ordem foram {lista}')

# 81
# lista: list = []
# continuar: str = 's'
# while continuar.lower() == 's':
#     while True: 
#         try: 
#             v: int = int(input(f'Digite um valor: '))
#             break
#         except ValueError:
#             print('Você não digitou um valor, por favor digite um valor: ')
#     lista.append(v)
#     print('Valor adicionado com sucesso...')    
#     continuar: str = input('Quer Continuar: [S/N]: ').strip()
#     while continuar not in ['S', 's', 'N', 'n']:
#         print('Opção inválida. Por favor, digite "S" para sim ou "N" para não.')
#         continuar: str = input('Quer Continuar: [S/N]: ').strip()
# print('-=' * 30)
# print(f'Você digitou {len(lista)} elementos.')
# lista.sort(reverse=True)
# print(f'Os valores em ordem decrescente são {lista}')
# if 5 in lista:
#     print('O valor 5 faz parte da lista!')
# else:
#     print('O valor 5 não foi encontrado na lista!')

# 82
# lista: list = []
# continuar: str = 's'
# while continuar.lower() == 's':
#     while True: 
#         try: 
#             v: int = int(input(f'Digite um número: '))
#             break
#         except ValueError:
#             print('Você não digitou um valor, por favor digite um valor: ')
#     lista.append(v)
#     print('Valor adicionado com sucesso...')    
#     continuar: str = input('Quer Continuar: [S/N]: ').strip()
#     while continuar not in ['S', 's', 'N', 'n']:
#         print('Opção inválida. Por favor, digite "S" para sim ou "N" para não.')
#         continuar: str = input('Quer Continuar: [S/N]: ').strip()
# print('-=' * 30)
# print(f'A lista completa é {lista}')
# lista_pares: list = []
# lista_impar: list = []
# for n in lista:
#     if n % 2 == 0:
#         lista_pares.append(n)
#     else:
#         lista_impar.append(n)
# print(f'A lista de pares é {lista_pares}')
# print(f'A lista de ímpares é {lista_impar}')

# 83
# e: str = input(f'Digite a expressão: ')
# qtde_caracteres: int = int(len(e))
# lista_abre: list = []
# lista_fecha: list = []
# for c in range (0, qtde_caracteres):
#     if e[c] in ('(', '{', '['):
#         lista_abre.append(e[c])
#     elif e[c] in (')', '}', ']'):
#         lista_fecha.append(e[c])
# if len(lista_abre) == len(lista_fecha):
#     print('Sua expressão está correta!')
# else:
#     print('Sua expressão está errada!')

# 84
# nome_peso: list = []
# lista_completa: list = []
# continuar: str = 's'
# maior_peso: float = float(0)
# menor_peso: float = float(0)
# while continuar.lower() == 's':
#     while True:
#         try:
#             nome: str = input('Nome: ')
#             nome_peso.append(nome)    
#             peso: float = float(input('Peso: '))
#             nome_peso.append(peso)
#             lista_completa.append(nome_peso[:])
#             nome_peso.clear()
#             break
#         except ValueError:
#             print('Você não digitou nenhum nome ou peso, ou digitou uma letra no campo peso, por favor tente novamente.')
#     continuar: str = input('Quer continuar: [S/N]: ').strip()
#     while continuar not in ['S', 's', 'N', 'n']:
#         print('Opção inválida. Por favor, digite "S" para Sim ou "N" para não.')
#         continuar: str = input('Quer continuar: [S/N]: ').strip()
# ## lista_completa = [['Maria', 70], ['João', 100], ['Claudio', 100]]
# for p, v in enumerate(lista_completa):    
#     if p == 0:
#         maior_peso = menor_peso = lista_completa[0][1]
#     else:
#         if v[1] > maior_peso:
#             maior_peso: float = float(v[1])
#         if v[1] < menor_peso:
#             menor_peso: float = float(v[1])        
# print('-=' * 30)
# print(f'Ao todo, você cadastrou {len(lista_completa[0])} pessoas.')
# print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
# for p, v in enumerate(lista_completa):    
#     if v[1] == maior_peso:
#         print(f'{v[0]}', end='... ')
# print()
# print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
# for p, v in enumerate(lista_completa):
#     if v[1] == menor_peso:
#         print(f'{v[0]}', end='... ')
        
# Correção 84
# temp: list = []
# princ: list = []
# mai = men = 0

# while True:
#     temp.append(str(input('Nome: ')))
#     temp.append(float(input('Peso: ')))
#     if len(princ) == 0:
#         mai = men = temp[1]
#     else:
#         if temp[1] > mai:
#             mai = temp[1]
#         if temp[1] < men:
#             men = temp[1]
#     princ.append(temp[:])
#     temp.clear()
#     resp: str = str(input('Quer continuar? [S/N] '))
#     if resp in 'Nn':
#         break
# print('-=' * 30)
# print(f'Ao todo, você cadastrou {len(princ)} pessoas. ')
# print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == mai:
#         print(f'[{p[0]}]', end=' ')
# print()
# print(f'O menor peso foi de {men}Kg. Peso de ', end='')
# for p in princ:
#     if p[1] == men:
#         print(f'[{p[0]}]', end=' ')

# 85
# lista_principal: list = [[], []]
# lista_par: list = lista_principal[0]
# lista_impar: list = lista_principal[1]
# for p in range(0, 7):
#     v: int = int(input(f'Digite o {p+1}o valor: '))
#     if v % 2 == 0:
#         lista_par.append(v)
#     else:
#         lista_impar.append(v)
# lista_impar.sort()
# lista_par.sort()
# print(f'Os valores pares digitados foram: {lista_principal[0]}')
# print(f'Os valores ímpares digitados foram: {lista_principal[1]}')

# correcao 85
# num: list = [[], []]
# valor: int = 0
# for c in range (1, 8):
#     valor: int = int(input(f'Digite o {c}o. valor: '))
#     if valor % 2 == 0:
#         num[0].append(valor)
#     else:
#         num[1].append(valor)
# print('-=' * 30)
# num[0].sort()
# num[1].sort()
# print(f'Os valores pares digitados foram: {num[0]}')
# print(f'Os valores ímpares digitados foram: {num[0]}')

# 86 não consegui fazer
# 86 correcao
# matriz: list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range (0, 3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
        # print(f'[{matriz[l][c]:^5}]', end='')
#     print()

# 87
# matriz: list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range (0, 3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()
# print('-=' * 30)
# p: int = 0
# for l in range(0, 3):
#     for c in range(0, 3):
#         if matriz[l][c] % 2 == 0:
#             p: int = p + matriz[l][c]
# print(f'A soma dos valores pares é {p}.')
# print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.')
# print(f'O maior valor da segunda linha é {max([matriz[1][0], matriz[1][1], matriz[1][2]])}')

# correcao 87
# matriz: list = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# # matriz: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# spar = mai = scol = 0
# for l in range (0, 3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#         if matriz[l][c] % 2 == 0:
#             spar += matriz[l][c]
#     print()
# print('-=' * 30)
# print(f'A soma dos valores pares é {spar}.')
# for l in range(0, 3):
#     scol += matriz[l][2]
# print(f'A soma dos valores da terceira coluna é {scol}.')
# for c in range(0, 3):
#     if c == 0:
#         mai = matriz[1][c]
#     elif matriz[1][c] > mai:
#         mai = matriz[1][c]
# print(f'A soma dos valores da terceira coluna é {mai}.')

# 88
# import random
# import time
# lista_sorteada: list = []
# print('-' * 30)
# print(f'{'JOGO NA MEGA SENA' :^30}')
# print('-' * 30)
# qtde_jogos: int = int(input('Quantos jogos você quer que eu sorteie? '))
# print(f'{'SORTEANDO 'f'{qtde_jogos} JOGOS' :^30}')
# for j in range(0, qtde_jogos):
#         lista: list = list(range(0, 61))
#         random.shuffle(lista)
#         lista_sorteada.append(lista[:6])
#         lista_sorteada[0].sort()
#         print(f'Jogo {j + 1}: {lista_sorteada[0]}')
#         lista_sorteada.clear()
#         time.sleep(1)
# print(f'{'Boa sorte' :^30}')

# correcao 88
# from random import randint
# from time import sleep
# lista = list()
# jogos = list()
# print('-' * 30)
# print(f'{'JOGO NA MEGA SENA' :^30}')
# print('-' * 30)
# quant = int(input('Quantos jogos você quer que eu sorteie? '))
# tot = 1
# while tot <= quant:
#         cont = 0
#         while True:
#                 num = randint(1,60)
#                 if num not in lista:
#                         lista.append(num)
#                         cont += 1
#                 if cont >= 6:
#                         break
#         lista.sort()
#         jogos.append(lista[:])
#         lista.clear()
#         tot += 1
# print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
# for i, l in enumerate(jogos):
#         print(f'Jogo {i+1}: {l}')
#         sleep(1)
# print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

# 89
# lista: list = []
# aluno: list = []
# notas: list = []
# continuar: str = 's'
# selecao_notas: int = 0
# while continuar.lower() == 's':
#     while True:
#         try:
#             nome: str = input('Nome: ')
#             aluno.append(nome)
#             notas_1: float = float(input('Nota 1: '))
#             notas.append(notas_1)
#             notas_2: float = float(input('Nota 2: '))
#             notas.append(notas_2)
#             media_notas: float = (notas_1 + notas_2) / 2
#             notas.append(media_notas)
#             aluno.append(notas[:])
#             lista.append(aluno[:])
#             aluno.clear()
#             notas.clear()
#             break
#         except ValueError:
#             print('Você não digitou nenhum nome ou peso, ou digitou uma letra no campo peso, por favor tente novamente.')
#     continuar: str = input('Quer continuar: [S/N]: ').strip()
#     while continuar not in ['S', 's', 'N', 'n']:
#         print('Opção inválida. Por favor, digite "S" para Sim ou "N" para não.')
#         continuar: str = input('Quer continuar: [S/N]: ').strip()
# print('-=' * 30)
# print('No.' + f'{'Nome' :^15}' + f'{'Média' :>15}')
# print('-' * 40)
# for p, n in enumerate(lista):
#     print(f'{p}' + f'{n[0] :^15}' + f'{n[1][2] :>15}')
# print('-' * 40)
# while not selecao_notas == 999:
#     selecao_notas: int = int(input('Mostrar notas de qual aluno? (Digite o No. dele ou 999 para interromper): '))
#     if selecao_notas == 999:
#         break    
#     else:
#         print(f'Notas de {lista[selecao_notas][0]} são {lista[selecao_notas][1][:2]}')
# print('FINALIZANDO...')
# print('<' * 3 + ' VOLTE SEMPRE ' + '>' * 3)

# correcao 89
ficha: list = list()
while True:
    nome: str = str(input('Nome: '))
    nota1: float = float(input('Nota 1: '))
    nota2: float = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append( [nome, [nota1, nota2], media])
    resp: str = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc: int = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
