# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# numeros: int = list(range(1,11))
# for numero in numeros:
#     print(numero**2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# lista: list = ["Python", "Java", "C++", "JavaScript"]
# lista.remove("C++")
# lista.append("Ruby")
# print(lista)

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# titulo: str = input("Por favor digite o nome do título: ") 
# autor: str = input("Por favor digite o nome do autor: ")
# ano_publicacao: int = int(input("Por favor digite o ano de publicação do livro: "))

# dicionario: list = {
#     'titulo': titulo,
#     'autor': autor,
#     'ano_publicacao': ano_publicacao
# }

# for chave, valor in dicionario.items():
#     print(f"{chave}: {valor}")

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))