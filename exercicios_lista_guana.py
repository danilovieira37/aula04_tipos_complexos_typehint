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
lista_principal: list = [[], []]
lista_par: list = lista_principal[0]
lista_impar: list = lista_principal[1]
for p in range(0, 7):
    v: int = int(input(f'Digite o {p+1}o valor: '))
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
lista_impar.sort()
lista_par.sort()
print(f'Os valores pares digitados foram: {lista_principal[0]}')
print(f'Os valores ímpares digitados foram: {lista_principal[1]}')

# correcao 85

