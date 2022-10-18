# Job 04 : Les boucles while
# Créez un script job04.py
# L’utilisateur devra entrer une valeur en input.
# A l’aide d’une boucle while et d’une fonction system, affichez nombres se trouvant de 0
# (inclus) à l’input (inlus).

input1 = int(input('Valeur 1: '))
i = 0
while i < input1 + 1:
    print(i)
    i += 1