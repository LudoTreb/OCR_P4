""" Interface utilisateur terminal """

import sys, os

menu_action = ["1", "2", "3", "4"]


# sub_menu = """Choissisez parmi les actions suivante :
# 1: Ajouter les joueurs.
# 3: Trier des joueurs par classement.
# 4: Sauvegarder/Charder des données.
# 5: Quitter.
# Que souhaitez-vous faire : """


def display_main_menu():
    menu_action = ["1", "2", "3", "4"]
    menu = """Choissisez parmi les actions suivante :
1: Créer un nouveau tournoi.
2: Afficher le rapport.
3: Sauvegarder/Charder des données.
4: Quitter.
Que souhaitez-vous faire : """

    user_action = input(menu)
    if user_action not in menu_action:
        os.system("clear")
        print("choix non valide")
        display_main_menu()
    else:
        return user_action


def add_player():
    print("Information  tournoi")
    last_name_player = input(f"nom du joueur :")
    gender_player = input(f"sexe du joueur :")
    rank_player = input(f"classemnt du joueur :")

    return {
        "last_name": last_name_player,
        "gender": gender_player,
        "rank": rank_player
    }


def fill_information_tournament():
    name_tournament = input("nom du tournoi:")
    localisation_tournament = input("lieu du tournoi:")
    date_tournament = input("date du tournoi:")
    number_round_tournament = input("nombre de round du tournoi [4]: ")

    return {
        "name": name_tournament,
        "location": localisation_tournament,
        "date": date_tournament,
        "number_round": number_round_tournament
    }

# while True:
#     user_action = ""
#     while user_action not in menu_action:
#         user_action = input(menu)
#         if user_action not in menu_action:
#             print("Veuillez choisir une action valide")
#     if user_action == "1":
#         os.system("clear")
#         fill_information_tournament()
#         user_action = input(sub_menu)
#         if user_action not in menu_action:
#             print("Veuillez choisir une action valide")
#         elif user_action == "1":
#             print("under construction")
#
#     elif user_action == "2":
#         print("script en cours de construction")
#     elif user_action == "3":
#         print("script en cours de construction")
#     elif user_action == "4":
#         print(" A bientôt !")
#         sys.exit()
