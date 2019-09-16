# Problème : Calculer le prix TTC d'une nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75
tva = 0.077

prix_total = nb_articles * prix_ht
ttc = prix_total * tva
prix_ttc = prix_total + ttc


print("Le prix TTC est de ",prix_ttc," chf.")
