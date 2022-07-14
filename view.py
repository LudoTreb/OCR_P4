""" Interface utilisateur terminal """

import datetime

import sys, os


# sub_menu = """Choissisez parmi les actions suivante :
# 1: Ajouter les joueurs.
# 3: Trier des joueurs par classement.
# 4: Sauvegarder/Charder des données.
# 5: Quitter.
# Que souhaitez-vous faire : """
MESSAGE_INVALID = "Donnée invalide, veuillez saisir une donnée numérique"


def display_main_menu():
    """
    Display the main menu.
    The user choose an action.
    :return:
    """
    menu_action = ["1", "2", "3", "4"]
    menu = """
====================== MENU ======================

Choissisez parmi les actions suivante :
   
1: Créer un nouveau tournoi.
2: Afficher le rapport.
3: Sauvegarder/Charder des données.
4: Quitter.
    
➡️  Que souhaitez-vous faire : """

    user_action = input(menu)
    if user_action not in menu_action:
        os.system("clear")
        print("Choix non valide")
        display_main_menu()
    else:
        return user_action


def is_valid_gender(message):
    """
    Check if the input is the right string
    :param message: message of what the program wants
    :return: choice
    """
    gender = ["h", "f"]
    choice = input(message + " : ")
    while choice not in gender:
        print("Veuillez faire un choix parmi les deux options")
        choice = input(message + " : ")
    return choice


def is_valid_date(message):
    """
    Check if the input is the right date format

    :param message: message of what the program wants
    :return: formated date
    """
    while True:
        try:
            date = input(message + ": ")
            valid_date = datetime.datetime.strptime(date, "%d/%m/%Y")
            return date

        except ValueError:

            print("Veuillez saisir la date au bon format")


def is_input_digit(message):
    """
    Check if the input is digital or not.

    :param message: the message if is not digital (str)
    :return: number_to_check
    """
    number_to_check = input(message + ": ")
    while not number_to_check.isdigit():
        print(f"{MESSAGE_INVALID}")
        number_to_check = input()

    return number_to_check


def fill_information_player(player_number):
    """
    Get input data for players in the form of dictonary

    :param player_number: a int
    :return: a dictionary
    """
    message = f"Veuillez saisir les informations du joueur {player_number}\n"
    print(f"{message : ^50}")

    last_name_player = input("Nom du joueur : ")
    first_name_player = input("Prénom du joueur : ")
    birth_date_player = is_valid_date("Date de naissance du joueur (jj/mm/aaaa)")
    gender_player = is_valid_gender("sexe du joueur (f/h)")
    rank_player = is_input_digit("classemnt du joueur")

    print("-" * 50)

    return {
        "last_name": last_name_player,
        "first_name": first_name_player,
        "birth_date": birth_date_player,
        "gender": gender_player,
        "rank": rank_player,
    }


def fill_information_tournament():
    """
    Get input data for a tournament in the form of dictonary

    :return: a dictionary
    """
    print("-" * 50)
    message = "Veuillez saisir les informations du tournoi \n"
    print(f"{message : ^50}")

    name_tournament = input("Nom du tournoi : ")
    localisation_tournament = input("Lieu du tournoi : ")
    date_tournament = is_valid_date("Date du tournoi (jj/mm/aaaa)")
    number_round_tournament = is_input_digit("Nombre de round du tournoi [4]")

    return {
        "name": name_tournament,
        "location": localisation_tournament,
        "date": date_tournament,
        "number_round": number_round_tournament,
    }


def display_tournament_created_message(new_tournament):
    """
    Display the data of a tournament
    :param new_tournament: a instance of tournament

    """
    print("-" * 50)
    message = "Tournoi a bien été crée\n"
    print(f"{message : ^50}")
    print(new_tournament.__dict__)
    print("-" * 50 + "\n" + "-" * 50)


def display_player_created_message(list_player):
    """
    Display the data of all player of a list
    :param list_player:

    """
    print("-" * 50)
    message = "Les joueurs ont bien été saisis \n"
    print(f"{message : ^50}")

    for player in list_player:
        print(f"{player.first_name}, rank: {player.rank}, score: {player.score}")
    # print("-" * 50 + "\n" + "-" * 50)
    print("-" * 50)


def display_round_created_message():
    """Affiche les informations du round
    - numero de round
    - quel joueur affronte quel joueur
    - le score des joueurs
    """
    pass


def display_round_results_message(round_matches, round):
    """
    Display the result of all the matches of a round.

    :param round_matches: a list of matches of a round
    :param round: instance of a round

    """

    print("-" * 50 + "\n" + "-" * 50)

    message = f"<< Résumé du Round {round.name} >>\n"
    print(f"{message : ^50}")
    for number_match, round in enumerate(round_matches):
        print(
            f"Match {number_match + 1}: {round.players[0][0].last_name} contre {round.players[1][0].last_name} "
        )
        if round.players[0][1] == "0.5" or round.players[0][1] == "0,5":
            print(f"Résultat : Match nul")
        elif round.players[0][1] == "1":
            print(f"Résultat : Victoire de {round.players[0][0].last_name}")
        else:
            print(f"Résultat : Victoire de {round.players[1][0].last_name}")

        print("-" * 50)


def enter_results(pair_player, round):
    """
    Get input data for a score result of a match.
    :param pair_player: a list of pair of player
    :param round: instance of a round
    :return: pair_player
    """
    print("-" * 50)
    message = f">> Round {round.name} en cours <<\n"
    print(f"{message : ^50}")
    print(
        "⎮ Pour rappel des notations des scores :      ⎮\n⎮ victoire = 1  défaite = 0  match nul =  0.5 ⎮\n"
    )

    print("Veuillez rentrer le score du match : ")
    # print(f"pair_player: {pair_player}")  # test --> [[<models.Player object at 0x10449c2b0>, 0],
    # [<models.Player object at 0x10449c280>, 0]]
    print(f"{pair_player[0][0].last_name} contre {pair_player[1][0].last_name}\n")
    for player in pair_player:
        result_possibility = ["1", "0", "0.5", "0,5"]
        player[1] = input(f"> {player[0].last_name} : ")
        while player[1] not in result_possibility:
            player[1] = input(f"> {player[0].last_name} : ")

    return pair_player


def display_ranking_tournament(list_ranking, tournament):
    """
    Display the result of the tournament.
    :param list_ranking:
    :param tournament:
    :return:
    """
    print("\n==================== RESULTATS ===================\n")
    print(f"{tournament.date},\n{tournament.name}\n")
    print(f"{'N°' : <3} {'Joueur' : ^15} {'Score' : >5}")

    for i, player in enumerate(list_ranking):
        print(f"{i + 1 : <3} {player.last_name : ^15} {player.score : >5}")
