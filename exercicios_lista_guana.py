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
lista: list = []
continuar: str = 's'
while continuar.lower() == 's':
    while True: 
        try: 
            v: int = int(input(f'Digite um número: '))
            break
        except ValueError:
            print('Você não digitou um valor, por favor digite um valor: ')
    lista.append(v)
    print('Valor adicionado com sucesso...')    
    continuar: str = input('Quer Continuar: [S/N]: ').strip()
    while continuar not in ['S', 's', 'N', 'n']:
        print('Opção inválida. Por favor, digite "S" para sim ou "N" para não.')
        continuar: str = input('Quer Continuar: [S/N]: ').strip()
print('-=' * 30)
print(f'A lista completa é {lista}')
lista_pares: list = []
lista_impar: list = []
for n in lista:
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impar.append(n)
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_impar}')