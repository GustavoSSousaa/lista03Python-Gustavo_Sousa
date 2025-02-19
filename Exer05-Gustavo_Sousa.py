#no comércio o conceito de margem bruta é uma porcentagem que é aplicada ao preço de custo para ser obter o preço de venda.
#Uma loja tem como política comercial aplicar uma margem bruta de 45% (porcento) quando o preço de custo é menor ou igual a 100 reais 
#quando o preço for maior que isso a margem bruta é de 35%.
#Escreva um programa que leia o preço de custo do produto e mostre na tela qual o seu preço de venda com duas casas decimais.

n1 = float(input("Digite o valor :"))
if n1<100:
    conta = n1*0.45
    print ("O preço de venda foi ",conta+n1)
    print ("Com",conta,"de impostos")
else:
    conta = n1*0.35
    print ("O preço de venda foi ",conta+n1)
    print ("Com",conta,"de impostos")
    