#Escreva um programa para exibir na tela o nome e a categoria de um lutador o programa deve ler em ”string” para o nome e um número real para o peso.
nome = str(input("Digite seu nome : "))
peso = float(input("Digite seu peso : "))
if (peso < 52):
    print ("Categoria invalida ")
elif peso>=52 <65:
    print ("Categoria pena ")
elif peso>=65 <72:
    print ("Categoria leve")
elif peso>=72 <79:
    print ("Categirua ligeiro")
elif peso>=79 <86:
    print ("Categoria medio")
elif peso>=86 <100:
    print ("Categoria pesado")
else:
    print ("Peso muito alto")