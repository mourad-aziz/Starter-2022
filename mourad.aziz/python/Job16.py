# Job 16 : Fonctions et paramètres 2.0
# Créer un programme job16.py. Le programme devra contenir une fonction qui prend en
# paramètres un nombre de paramètres indéfini.
# La fonction écrira tous les paramètres dans le terminal.

# 
def show_user_info(**data):
    # data is a dict
    for key, value in data.items():
        print(f"{key}: {value}")
show_user_info(prenom="Mourad")
show_user_info(name="Aziz", job="contact me")
show_user_info(school="Laplateforme.io", Mail="contact@me.oz", city="here" )

