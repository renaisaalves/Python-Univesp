print('Você tem que digitar a sua nacionalidade')  
nacionalid=input("Coloque b (brasileiro) ou q (caso não seja)") 
if (nacionalid== 'q'): 
    print('Você não pode votar') 
else: 
    idade = eval(input("Entre com sua idade ")) 
    if idade < 16: 
        print("Você não é eleitor ") 
    elif idade >= 18 and idade<= 65: 
        print("Você é eleitor obrigatório") 
    elif (idade >=16 and idade <18) or idade > 65: 
        print("Você é eleitor facultativo") 
    else: 
        print("Erro") 
print("Obrigada por usar nossos serviços")