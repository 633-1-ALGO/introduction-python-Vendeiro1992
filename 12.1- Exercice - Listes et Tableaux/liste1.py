# Problème : Réaliser une table de multiplication de taile 10x10 en utilisant la liste fournie.
# Résultat attendu : un affichage comme ceci :   1  2  3  4  5  6  7  8  9  10
#                                             1  1  2  3  4  5  6  7  8  9  10
#                                             2  2  4  6  8  10 12 14 16 18 20
#                                             . .  .  .  .  .  .  .  .  .  .
# Indication :   L'alignement rectiligne n'est pas une contrainte, tant que la table est visible ligne par ligne c'est ok.
#               Si vous êtes perfectionnistes faites vous plaisir.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 1
print("   ", end=" ")
while i <= 1:
   nb = 1
   while nb <= 10:
      print("{:>3d}".format(i*nb), end=" ")
      nb += 1
   print("")
   i += 1

for i in range(1,len(liste)+1):
    print("{:>3d}".format(i), end=" ")
    for j in range (1,len(liste)+1):
        print("{:>3d}".format(j*i), end=" ")
    print("")
