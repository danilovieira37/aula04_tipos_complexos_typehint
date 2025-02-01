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
lista: list = []
continuar: str = 's'
while continuar.lower() == 's':
    while True: 
        try: 
            v: int = int(input(f'Digite um valor: '))
            break
        except ValueError:
            print('Você não digitou um valor, por favor digite um valor: ')
    if v in lista:
        print('Valor duplicado! Não vou adicionar...')        
    else:
        lista.append(v)
        print('Valor adicionado com sucesso...')    
    continuar: str = input('Quer Continuar: [S/N]: ').strip()
    while continuar not in ['S', 's', 'N', 'n']:
        print('Opção inválida. Por favor, digite "S" para sim ou "N" para não.')
        continuar: str = input('Quer Continuar: [S/N]: ').strip()
lista.sort()
print(f'Você digitou os valores {lista}')

