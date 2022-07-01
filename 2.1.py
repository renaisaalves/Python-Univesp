# Escreva expressões algébricas Python correspondentes aos seguintes comandos:

print('=' * 50)
print('(a) A soma dos 5 primeiros inteiros positivos.')
print()
soma = 0 
for c in range(1, 6):
    num = int(input(f'Nº {c}: '))
    soma = soma + num
print(f'A soma dos 5 primeiros números foi: {soma}')

print('=' * 50)
print('(b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).')
print()
Sara = 23
Mark = 19
Fatima = 31
media = (Sara + Mark + Fatima) / 3
print(f'A média de idade entre Sara, Mark e Fátima é {media}')

print('=' * 50)
print('(c) O número de vezes que 73 cabe em 403.')
print()
num = int(input('Número: '))
numax = int(input('Número máximo: '))
espaço = numax // num
print(f'O número {num} cabe {espaço} vezes em {numax}')

print('=' * 50)
print('(d) O resto de quanto 403 é dividido por 73.')
print()
dividendo = int(input('Dividendo: '))
divisor = int(input('Divisor: '))
resto = dividendo % divisor 
print(f'O resto da divisão {dividendo} por {divisor} é {resto}')

print('=' * 50)
print('(e) 2 à 10ª potência.')
print()
num = int(input('Número: '))
potencia = int(input('Potência: '))
produto = num ** potencia
print(f'O produto de {num} à {potencia}ª potência é {produto}')

print('=' * 50)
print('(f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).')
print()
Sara = 54
Mark = 57
absoluto = Sara + Mark / 2
print(f'O valor absoluto de Sara e Mark é {absoluto}')

print('=' * 50)
print('O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.')
print()
lista = [34.99, 29.95, 31.50]
print(f'O menor produto é R$ {min(lista)}')