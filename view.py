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


def display_round_results_message(round_matches, round):  # j'ai enlever le parametre "list_scores"
    """ Affiche les resultats du round
    - numero de tournoi
    - quel joueur à gagner contre quel joueur
    - le score des joureurs mise à jour
    """
    print("-" * 50 + "\n" + "-" * 50)

    print(f"Résumé du Round {round.name}:") # <-- à checker c'est pas normal le result de ce print
    for number_match, round in enumerate(round_matches):
        print(
            f"Match {number_match + 1}: {round.players[0][0].last_name} contre {round.players[1][0].last_name} ")
        if round.players[0][1] == "0.5" or round.players[0][1] == "0,5":
            print(f"Résultat : Match nul")
        elif round.players[0][1] == "1":
            print(
                f"Résultat : Victoire de {round.players[0][0].last_name}")
        else:
            print(f"Résultat : Victoire de {round.players[1][0].last_name}")

        print("-" * 50)


def enter_results(pair_player):  # tuple d'instance de joueur
    print("Pour rappel:  victoire = 1, défaite = 0, match nul =  0.5")
    # print(f"pair_player: {pair_player}")  # test --> [[<models.Player object at 0x10449c2b0>, 0],
    # [<models.Player object at 0x10449c280>, 0]]
    for player in pair_player:
        player[1] = input(f"score du joueur, {player[0].last_name} : ")

    return pair_player
