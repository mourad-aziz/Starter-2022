# Job 17 : Listes
# Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
# paramètres un nombre de paramètres indéfini (uniquement des nombres).
# La fonction devra :

# Remplir une liste myList contenant tous ces paramètres.

# Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.

def evennumbers(list, n=0):
    #base case
    if n==len(list):
        exit()
    if list[n]%2==0:
        print(list[n], end=" ")
    #calling function recursively
    evennumbers(list, n+1)
#list1 = [10, 21, 4, 45, 66, 93, 100]

print("Nombre paire dans la liste:", end=" ")
list2 = [2, 99, 34, 45, 66, 93, 100990]
evennumbers(list2)
#evennumbers(list1)