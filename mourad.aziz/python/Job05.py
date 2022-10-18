# Job 05 : Les boucles For
# Créez un script job05.py
# L’utilisateur devra entrer deux valeurs en input.
# A l’aide d’une boucle for et d’une fonction system, affichez uniquement les nombres se
# trouvant entre l’input 1 et l’input 2. Le programme doit toujours partir de l’input 1 et
# aller jusqu’à l’input 2.
# Si les deux sont égaux, le programme devra écrire “Valeurs égales”.

input1 = int(input('Valeur 1: '))
input2 = int(input('Valeur 2: '))

if input1 == input2 :
    print("Valeurs égales")
elif input1 < input2 :
    for i in range(input1, input2 +1):
        print(i)
else :
    for i in range(input2 , input1 -1):
        
        print( input1 -i )
        
 

# numbers = [input1 .. input2]
# for i in range(input1, input2 +1):
    # numbers[i]
    # print(numbers)
# # returns the first item 
# numbers[1] # returns the second item
# numbers[-1] # returns the first item from the end
# numbers[-2] # returns the second item from the end 
    