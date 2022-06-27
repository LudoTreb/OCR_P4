""" Interface utilisateur terminal """

import sys, os


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


def add_player(player_number):
    print(f"Information joueur_{player_number} : ")
    last_name_player = input(f"Nom du joueur : ")
    first_name_player = input(f"Prénom du joueur : ")
    birth_date_player = input(f"Date de naissance du joueur : ")
    gender_player = input(f"sexe du joueur : ")
    rank_player = input(f"classemnt du joueur : ")
    score_player = input(f"Score du joueur [0] : ")
    print("-" * 50)

    return {
        "last_name": last_name_player,
        "first_name": first_name_player,
        "birth_date": birth_date_player,
        "gender": gender_player,
        "rank": rank_player,
        "score": score_player
    }


def fill_information_tournament():
    name_tournament = input("nom du tournoi : ")
    localisation_tournament = input("lieu du tournoi : ")
    date_tournament = input("date du tournoi : ")
    number_round_tournament = input("nombre de round du tournoi [4] : ")

    return {
        "name": name_tournament,
        "location": localisation_tournament,
        "date": date_tournament,
        "number_round": number_round_tournament
    }


def display_tournament_created_message(new_tournament):
    print("-" * 50)
    print("Tournoi a bien été crée : ")
    print(new_tournament.__dict__)
    print("-" * 50 + "\n" + "-" * 50)


def display_player_created_message(list_player):
    print("-" * 50)
    print("Les joueurs ont bien été saisis : ")
    for player in list_player:
        print(f"{player.first_name}, rank: {player.rank}, score: {player.score}")
    print("-" * 50 + "\n" + "-" * 50)


def display_round_created_message():
    """ Affiche les informations du round
    - numero de round
    - quel joueur affronte quel joueur
    - le score des joueurs
    """
    pass


def display_round_results_message(round_matches, list_scores):
    """ Affiche les resultats du round
    - numero de tournoi
    - quel joueur à gagner contre quel joueur
    - le score des joureurs mise à jour
    """
    print("-" * 50 + "\n" + "-" * 50)

    print(f"Résumé du Round {int(round_matches[0].name) + 1}:")
    for number_match, score in enumerate(list_scores):
        print(f"Match {number_match + 1}: {score[0][0]} contre {score[1][0]} ")
        if score[0][1] and score[1][1] == "0,5":
            print(f"Résultat : Match nul {score[0]}, {score[1]}")
        elif score[0][1] == "1":
            print(f"Résultat : {score[0]} victoire")
        else:
            print(f"Résultat : {score[1]} victoire")

        print("-" * 50)


def enter_results(pair_player):  # tuple d'instance de joueur
    print("Pour rappel:  victoire = 1, défaite = 0, match nul =  0,5")
    scores = []
    for player in pair_player:
        player_score = (player, input("score du joueur : "))
        scores.append(player_score)

    return scores
