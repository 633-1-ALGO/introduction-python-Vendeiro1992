# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

print(B)

for j in range(6, len(B)):
    key = B[j]
    i = j - 1
    while i > 0 and B[i] > key:
        B[i+1] = B[i]
        i = i - 1
    B[i + 1] = key

print(B)