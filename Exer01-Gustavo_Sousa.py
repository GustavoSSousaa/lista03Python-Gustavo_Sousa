#-Escreva um programa que forneça o tipo de aplicação financeira a um investidor a partir de dois dados obtidos:  
#O grau de aceitação de risco e o valor a ser investido.
risco=input("Qual o nível de rísco aceitavel : ")
n1=float(input("Qual o valor que deseja investir : "))
if risco=='Bx'and n1<1000:
        print("Recomendação de investivento é poupança")
elif  risco == 'Bx' and n1 >=1000:
   print("Recomendação de investivento é renda fixa")
elif risco =='Al'and n1 <1000:
  print("Recomendação de investivento é Bit coin")
elif  risco == 'Al' and n1 >=1000:
    print("Recomendação de investivento é ações")
else:
    print("Os dados fornecidos estão incorretos")