# Escreva expressões algébricas Python correspondentes aos seguintes comandos:

# (a) A soma dos 5 primeiros inteiros positivos.

soma = 0 
for c in range(1, 6):
    num = int(input(f'Nº {c}: '))
    soma = soma + num
print(f'A soma dos 5 primeiros números foi: {soma}')

# (b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
# (c) O número de vezes que 73 cabe em 403.
# (d) O resto de quando 403 é dividido por 73.
# (e) 2 à 10ª potência.
# (f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
# (g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.