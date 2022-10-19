# Job 24 : Aller plus loin 2
# A l’aide du dictionnaire de la langue française téléchargeable sur ce lien, écrivez un
# programme job24.py qui demandera à l’utilisateur d'entrer des lettres, sans espace ni
# autre caractère que les 26 lettres de l’alphabet (sans accent ni majuscule).
# Votre programme devra donner les différentes combinaisons possibles de mots se
# trouvant dans le dictionnaire à réaliser avec ces lettres, ainsi que les points de chaque
# mots selon la règle de scrabble française :
# 1 point : E, A, I, N, O, R, S, T, U, L
# 2 points : D, G, M
# 3 points : B, C, P
# 4 points : F, H, V
# 8 points : J, Q
# 10 points : K, W, X, Y, Z
# Votre programme affichera les mots par ordre décroissant de points.

my_dict = dict.fromkeys(['E', 'A', 'I', 'N', 'O', 'R', 'S', 'T', 'U', 'L'], 1)
my_dict.update(dict.fromkeys(['D', 'G', 'M'], 2))
my_dict.update(dict.fromkeys(['B', 'C', 'P'], 3))
my_dict.update(dict.fromkeys(['F', 'H', 'V'], 4))
my_dict.update(dict.fromkeys(['J', 'Q'], 8))
my_dict.update(dict.fromkeys(['K', 'W', 'X', 'Y', 'Z'], 10))

# def score
# def anagram

words = open('C:\\Users\\Admin\\Documents\\GitHub\\Starter-2022\\mourad.aziz\\python\\dico_france.txt', 'r').read().split()
print(len(words))