#Faça um programa que leia 4 notas de um aluno, salve as em uma lista e calcule a média das notas. 


primeironome=input("Digite seu primeiro nome: ")
primeiraletra=primeironome [0 : 1].upper()
restantenome=primeironome [ 1: ]. lower()
nomeformatado=primeiraletra + restantenome

ainput=(" Digite sua nota na primeira atividade: ")
binput=(" Digite sua na segunda atividade: ")
cinput=(" Digite sua nota na terceira atividade: ")
dinput=(" Digite sua nota na quarta atividade: ")

a=float(ainput)
b=float(binput)
c=float(cinput)
d=float(dinput)
média= (a + b + c + d) / 4

minhalista= []
minhalista.append(ainput)
minhalista.append(binput)
minhalista.append(cinput)
minhalista.append(dinput)

print(minhalista)

print(" A média das notas de " + nomeformatado + "é de" + str (média) + ".")