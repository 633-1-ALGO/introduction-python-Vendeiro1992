# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

nb_occu = texte.count("exemple")
print(nb_occu)


mot_replace = texte.replace("est", 'représente')
print(mot_replace)

texte_inverse = texte[::-1]
print(texte_inverse)



