# 2. Ecrire un algorithme permettant de fusionner deux tableaux T1 et T2 dans un tableau T3,
# sachant que T1 et T2 sont déjà triés par ordre croissant, T3 doit aussi être trié

def fusionner(T1, n, T2, m):
	T3 = []
	i = 0
	j = 0
	k = 0
	for l in range(n+m):
		T3.append(None)
	while (j < n) and (k < m):
		if T1[j] < T2[k]:
			T3[i] = T1[j]
			j = j+1
		else:
			T3[i] = T2[k]
			k = k+1
		i = i+1
	# if j < n:
		for l in range(j, n):
			T3[i] = T1[l]
			i = i+1
	# else:
		for l in range(k, m):
			T3[i] = T2[l]
			i = i+1
		return T3



	

print(fusionner([1,2], 2, [1,2,3], 3))
# Doit afficher [1, 1, 2, 2, 3]