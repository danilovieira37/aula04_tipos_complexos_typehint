# lanche = ('hamburger', 'suco', 'pizza', 'pudim', 'batata frita')

# for comida in lanche:
#     print(f'Eu vou comer {comida} ')

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont} ')

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posicao {pos}')

# print ('Comi pra caramba')

# 72
# numeros: tuple = tuple(range(0, 21))
# numeros_extensos: str = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
#     'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 
#     'dezoito', 'dezenove', 'vinte')
# numeros_maximo: int = max(numeros)
# numeros_minimo: int = min(numeros)
# validacao: bool = False
# while not validacao:
#     try:
#         numero_digitado: int = int(input('Digite um número entre 0 e 20: '))
#         if numero_digitado >= numeros_minimo and numero_digitado <= numeros_maximo:
#             extenso: int = numeros.index(numero_digitado)
#             numero_extenso: str = numeros_extensos[extenso]
#             print(f'Você digitou o número {numero_extenso}')
#             validacao: bool = True
#         else:
#             print(f'Você digitou o número {numero_digitado}. Tente novamente. Digite um número entre 0 e 20: ')
#     except ValueError:
#         print('Você digitou uma letra ou não digitou nada. Poderia digitar um numero entre 0 e 20: ')

# 73
classificacao = (
    "Botafogo",
    "Palmeiras",
    "Flamengo",
    "Fortaleza",
    "Internacional",
    "São Paulo",
    "Atlético Mineiro",
    "Fluminense",
    "Grêmio",
    "Corinthians",
    "Santos",
    "Bragantino",
    "Cruzeiro",
    "Bahia",
    "Vasco",
    "Goiás",
    "Athletico Paranaense",
    "Criciúma",
    "Atlético Goianiense",
    "Cuiabá"
)

# a) 5 primeiro colocados
# cinco_primeiros_colocados: str = classificacao[0:5]
# print(f'Os cinco primeiros colocados no Brasileirão forão: {cinco_primeiros_colocados}.')

# b) 4 últimos colocados
# quatro_ultimos_colocados: str = classificacao[-4:]
# print(f'Os quatro ultimos colocados no Brasileirão forão: {cinco_primeiros_colocados}.')

# c) uma lista com os times em ordem alfabetica
ordem_alfabetica: str = sorted(classificacao)
print(ordem_alfabetica)

# d) posicao do goias
posicao_criciuma: int = classificacao.index("Goiás")+1
print(posicao_criciuma)
