# TP6
# Exercice 4 (série 1)
# 1. Ecrire un algorithme permettant de fusionner deux tableaux T1 et T2 dans un tableau T3


T1 = []
T2 = []
n = int(input("Donner la taille de T1"))
m = int(input("Donner la taille de T2"))

for l in range(n):
	el = int(input("Donner une valeur pour stocker dans T1: "))
	T1.append(el)
for l in range(m):
	el = int(input("Donner une valeur pour stocker dans T2: "))
	T2.append(el)


T3 = []
for i in range(n+m):
	T3.append(None)
for i in range(n):
	T3[i] = T1[i]
for i in range(n,n+m):
	T3[i] = T2[i-n]
	print(T3)