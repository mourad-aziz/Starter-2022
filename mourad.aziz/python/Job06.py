# Job 06 : Les boucles infinies

# Créez un script job06.py
# Lorsque l’utilisateur va lancer le script, un prompteur devra s’afficher “>”, et le
# programme devra attendre un input.
# Si l’input entré est “Bonjour”, le programme devra répondre “Bonjour à toi”
# Si l’input entré est “Au revoir”, le programme devra quitter

hello = "Bonjour à toi"
bye = "Au revoir"
input1 = input('> ')

i = 1
while i == 1 :
    
    
    if input1 == "Bonjour" :
        print ("Bonjour à toi")
      
    if input1 == "Au revoir" :
        i = 0    
        exit
print(">")   