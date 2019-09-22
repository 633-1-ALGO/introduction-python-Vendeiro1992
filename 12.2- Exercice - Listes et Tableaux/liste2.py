# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

valMax = max(max(x) for x in tab)
indice = [(index, row.index(valMax)) for index, row in enumerate(tab) if valMax in row]

print("La valeur maximum est :",valMax,"et elle se trouve à l'indice",indice)

