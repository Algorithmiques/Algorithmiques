# TP6
# Exercice 4 (série 1)
# 1. Ecrire un algorithme permettant de fusionner deux tableaux T1 et T2 dans un tableau T3


def fusionner(T1, n, T2, m):
	T3 = []
	for i in range(n+m):
		T3.append(None)
	for i in range(n):
		T3[i] = T1[i]
	for i in range(n,n+m):
		T3[i] = T2[i-n]
	return T3

# Test
print(fusionner([1,2,3], 3, [4,5,6], 3))
# Doit afficher [1, 2, 3, 4, 5, 6]