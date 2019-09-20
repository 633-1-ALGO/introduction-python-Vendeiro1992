# Problème : Réaliser une table de multiplication de taile 10x10 en utilisant la liste fournie.
# Résultat attendu : un affichage comme ceci :   1  2  3  4  5  6  7  8  9  10
#                                             1  1  2  3  4  5  6  7  8  9  10
#                                             2  2  4  6  8  10 12 14 16 18 20
#                                             . .  .  .  .  .  .  .  .  .  .
# Indication :   L'alignement rectiligne n'est pas une contrainte, tant que la table est visible ligne par ligne c'est ok.
#               Si vous êtes perfectionnistes faites vous plaisir.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 1
while i <= 1:
   nb = 1
   while nb <= 10:
      print(i*nb, end = "  ")
      nb = nb + 1
   print("")
   i = i + 1
j = 1
while j <= 10:
   nb = 1
   while nb <= 10:
      print(j*nb, end = "  ")
      nb = nb + 1
   print("")
   j = j + 1
