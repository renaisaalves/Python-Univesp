var_animal = ['cachorro', 'gato', 'pássaro']
var_numero = [2, 4, 6, 8, 10]
var_misto = ['pássaro', 6, '1.8', [2, 4]]
var_flor = []

print(var_animal[1])
print(var_numero[3])
print(var_misto[-1])

if 'pássaro' in var_animal:
    print('True')
else:
    print('Not')
    
resposta = 10 in var_numero
print(resposta)

resposta = 18 in var_misto
print(resposta)

resposta = 'gato' not in var_animal
print(resposta)

for c in range(1, 4):
    var_flor.append(str(input(f'{c}ª Flor: ')))
print(var_flor)