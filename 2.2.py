#Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:
print('=' * 50)
print('(a) A soma de 2 e 2 é menor que 4.')
resposta = 2 + 2 < 4
print(resposta)

print('=' * 50)
print('(b) O valor de 7 // 3 é igual a 1 + 1.')
resposta = 7 // 3 == 1 + 1
print(resposta)

print('=' * 50)
print('(c) A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.')
resposta = 3**2 + 4**2 == 25
print(resposta)

print('=' * 50)
print('(d) A soma de 2, 4 e 6 é maior que 12.')
resposta = 2 + 4 + 6 > 12
print(resposta)

print('=' * 50)
print('(e) 1387 é divisível por 19.')
resposta = 1387 / 19
print(resposta)

print('=' * 50)
print('(f) 31 é par')
resposta = 31 % 2 == 0
print(resposta)

print('=' * 50)
print('(g) O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.')
preco = [34.99, 29.95, 31.50]
resposta = min(preco) < 30.00
print(resposta, min(preco))