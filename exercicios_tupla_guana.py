# lanche = ('hamburger', 'suco', 'pizza', 'pudim', 'batata frita')

# for comida in lanche:
#     print(f'Eu vou comer {comida} ')

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont} ')

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posicao {pos}')

# print ('Comi pra caramba')

# 72
numeros: tuple = tuple(range(0, 21))
numeros_maximo: int = max(numeros)
numeros_minimo: int = min(numeros)
validacao: bool = False
while not validacao:
    try:
        numero_digitado: int = int(input('Digite um número entre 0 e 20: '))
        if numero_digitado >= numeros_minimo and numero_digitado <= numeros_maximo:
            print(f'Você digitou o número {numero_digitado}')
            validacao: bool = True
        else:
            print(f'Você digitou o número {numero_digitado}. Tente novamente. Digite um número entre 0 e 20: ')
    except ValueError:
        print('Você digitou uma letra. Poderia digitar um numero entre 0 e 20: ')

# Inicializa as variáveis para o controle do loop
nome_valido = False
salario_valido = False
bonus_valido = False

# Loop para verificar o nome
while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)