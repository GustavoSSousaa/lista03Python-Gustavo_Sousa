#Uma empresa financeira concede empréstimos a pessoas físicas quando o valor da parcela é menor que 8% que o salário da pessoa.
#Escreva um programa que leia dois números reais: O valor do salário e o valor da parcela e informe se o empréstimo será concedido ou não.
n1=float(input("Digite quanto você ganha : "))
n2=float(input("Qual o valor da parcela : "))
aa = n2/n1
if aa <0.08:
  print("empréstimo sera concedido ")
else:
  print("empréstimo sera negado ")