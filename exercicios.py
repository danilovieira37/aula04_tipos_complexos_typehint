# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# numeros: list = list(range(1,11))
# for numero in numeros:
#     print(numero**2)
#correcao ex. 1:
# numeros = list(range(1, 11))
# for numero in numeros:
#     print(quadrados**2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# lista: list = ["Python", "Java", "C++", "JavaScript"]
# lista.remove("C++")
# lista.append("Ruby")
# print(lista)
# correcao ex. 2:
# linguagens = ["Python", "Java", "C++", "JavaScript"]
# linguagens.remove("C++")
# linguagens.append("Ruby")
# print(linguagens)

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
# correcao ex. 3:
# livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}")

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem
# print(contar_caracteres("engenharia de dados"))
# correcao ex. 4:
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem
# print(contar_caracteres("engenharia de dados"))

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
# dicionario_produtos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# lista_precos: list = []
# for p in dicionario_produtos.values():
#     lista_precos.append(p)
# preco_total_lista: int = sum(lista_precos)
# print(preco_total_lista)
# correcao ex. 5:
# lista_compras = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# total = sum(precos[item] for item in lista_compras)
# print(f"Preço total: {total}")

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.
# emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos: list = list(set(emails))
# print(emails_unicos)
# correcao ex. 6
# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))
# print(emails_unicos)

# 7.Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# def maior_ou_igual_a_18(x):
#     return x >= 18
# idades: list = [22, 15, 30, 17, 18]
# idades_maiores_ou_iguais_a_18: list = list(filter(maior_ou_igual_a_18, idades))
# print(idades_maiores_ou_iguais_a_18)
# correcao ex. 7
# idades = [22, 15, 30, 17, 18]
# idades_validas = [idade for idade in idades if idade >= 18]
# print(idades_validas)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas: list = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Carol", "idade": 20},
#     {"nome": "Bob", "idade": 25}
# ]
# ordenado_por_nome: list = sorted(pessoas, key=lambda pessoa: pessoa["nome"])
# print(ordenado_por_nome)
# correcao ex. 8
# pessoas: list = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Carol", "idade": 20},
#     {"nome": "Bob", "idade": 25}
# ]
# pessoas.sort(key=lambda pessoa: pessoa["nome"])
# print(pessoas)

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
# numeros: list = [10, 20, 30, 40, 50]
# media: float = sum(numeros) / len(numeros)
# print(media)
# correcao ex. 9
# numeros = [10, 20, 30, 40, 50]
# media = sum(numeros) / len(numeros)
# print("Média:", media)

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista_impar: list = []
# lista_par: list = []
# for n in valores:
#     if n % 2 == 0:
#         lista_par.append(n)
#     else:
#         lista_impar.append(n)
# print(f'Lista impar: {lista_impar} e Lista par: {lista_par}')
# correcao ex. 10
# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = [valor for valor in valores if valor % 2 == 0]
# impares = [valor for valor in valores if valor % 2 != 0]
# print("Pares:", pares)
# print("Ímpares:", impares)

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# produtos: lista = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]
# def alterar_preco (lista, nome_antigo, preco_novo):
#     for item in lista:
#         if item["nome"] == nome_antigo:
#             item["preço"] = preco_novo
# alterar_preco(produtos, "Teclado", 150)
# print(produtos)
# # Correcao ex. 11
# produtos: lista = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]
# # Atualizar o preço do produto com id 2 para 90
# for produto in produtos:
#     if produto["id"] == 2:
#         produto["preço"] = 90
# print(produtos)

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.
# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}
# dicionario_unico = dicionario1 | dicionario2
# print(dicionario_unico)
# correcao ex. 12
# dicionario1 = {"a": 1, "b": 2}
# dicionario2 = {"c": 3, "d": 4}
# dicionario_fundido = {**dicionario1, **dicionario2}
# print(dicionario_fundido)