#No Senailândia mulheres e homens podem servir o exército do país.
#O serviço é opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da vida.
#Existe uma única restrição para o ingresso que é a idade da pessoa:
#A-	Para mulheres a idade aceita é entre 21 e 34 anos.
#B-	Pra homens a idade aceita é entre 18 e 39 anos.
#Escreva um programa que leia três dados de entrada: O nome da pessoa, idade e sexo, e informe se a pessoa vai poder servir ou não. 
#Obs: Para o sexo deve ser lido apenas um caractere que pode “f” ou “F” ou “n” “N”. Qualquer coisa diferente deve ser informado “Dado inválido”.

nome = str(input("Digite seu nome : "))
print ("")
idade = int(input("Digite sua idade : "))
print ("")
gen = str(input("Digite seu genero : "))
print ("")
if gen == "f" or "F" and idade == 21 <34:
        print ("Voce foi aceita")
elif gen == "m" or "M" and idade == 18 <39:
        print ("Voce foi aceito")
else:
    print ("Não vai poder servir")