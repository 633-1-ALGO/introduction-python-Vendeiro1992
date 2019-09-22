# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A

A = [1, 5, 15, 25, 10, 55, 50, 35]

nb = len(A)
moyenne = 0

for i in range(1, nb + 1):
    moyenne += A[i - 1]  #moyenne = moyenne + A[i - 1]
moyenne /= nb  #moyenne = moyenne + nb

print(moyenne)

