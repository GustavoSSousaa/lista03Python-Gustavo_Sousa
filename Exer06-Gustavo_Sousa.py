#Nas eleições municipais com 200 mil eleitores ou mais tem segundo turno caso o primeiro colocado não tenha mais que 50% dos votos.
#Escreva um programa que leia o nome do município a quantidade de eleitores e a quantidade de votos do candidato mais votado e informe se avéra segundo turno ou não.
cidade=input("Qual o nome da cidade : ")
qtde_votos=int(input("Quantas pessoas votaram : "))
votos_candidato=int(input("Quantos votos teve o candidato mais votado : "))
porcentagem=votos_candidato/qtde_votos
if porcentagem <=0.50:
    print("Vai ter segundo turno em: ",cidade)
else:
     print("Não vai ter segundo turno em: ",cidade)