""" Interface utilisateur terminal """

import datetime

import os


MESSAGE_INVALID = "Donnée invalide, veuillez saisir une donnée numérique"


def display_main_menu():
    """
    Display the main menu.
    The user choose an action.
    :return:
    """
    menu_action = ["1", "2", "3"]
    menu = """
====================== MENU ======================

Choissisez parmi les actions suivante :
   
1: Créer un nouveau tournoi.
2: Afficher le rapport.
3: Quitter.
    
--> Que souhaitez-vous faire : """

    user_action = input(menu)
    if user_action not in menu_action:
        os.system("clear")
        print("Choix non valide")
        display_main_menu()
    else:
        return user_action


def display_sub_menu():
    sub_menu_action = ["1", "2"]
    sub_menu = """
==================== SUBMENU =====================

Choissisez parmi les actions suivante :

1: Revenir au menu principal.
2: Quitter

Que souhaitez-vous faire : """

    user_action = input(sub_menu)
    if user_action not in sub_menu_action:
        os.system("clear")
        print("Choix non valide")
        display_sub_menu()
    else:
        return user_action


def display_rapport_menu():
    menu_action = ["1", "2", "3", "4", "5", "6", "7"]

    menu_rapport = """
==================== RAPPORT =====================

Choissisez parmi les actions suivante :

1 : Liste de tous les acteurs
2 : Liste de tous les joueurs d'un tournoi
3 : Liste de tous les tournois
4 : Liste de tous les tours d'un tournoi
5 : Liste de tous les matchs d'un tournoi
6 : Revenir au menu principal
7 : Quitter

--> Que souhaitez-vous faire : """

    user_action = input(menu_rapport)

    if user_action not in menu_action:
        os.system("clear")
        print("Choix non valide")
        display_rapport_menu()

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
            datetime.datetime.strptime(date, "%d/%m/%Y")
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

    return int(number_to_check)


def is_time_control_right(message):
    input_to_check = input(message + ": ")
    possibility = ["bullet", "blitz", "coup rapide"]
    while input_to_check not in possibility:
        print("Seuls les cadences rapides sont possible (bullet, blizt, coup rapide)")
        input_to_check = input(message + ": ")

    return input_to_check


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
    gender_player = is_valid_gender("Sexe du joueur (f/h)")
    rank_player = is_input_digit("Classement du joueur")

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
    time_control = is_time_control_right("Cadence (coup rapide)")
    number_round_tournament = is_input_digit("Nombre de round du tournoi [4]")

    return {
        "name": name_tournament,
        "location": localisation_tournament,
        "date": date_tournament,
        "time_control": time_control,
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


def display_round_results_message(round_matches, rounds):
    """
    Display the result of all the matches of a round.

    :param round_matches: a list of matches of a round
    :param rounds: instance of a round

    """

    print("-" * 50 + "\n" + "-" * 50)

    message = f"<< Résumé du Round {rounds.name} >>\n"
    print(f"{message : ^50}")
    for number_match, rounds in enumerate(round_matches):
        print(
            f"Match {number_match + 1}: {rounds.players[0][0].last_name} contre {rounds.players[1][0].last_name} "
        )
        if rounds.players[0][1] == "0.5" or rounds.players[0][1] == "0,5":
            print(f"Résultat : Match nul")
        elif rounds.players[0][1] == "1":
            print(f"Résultat : Victoire de {rounds.players[0][0].last_name}")
        else:
            print(f"Résultat : Victoire de {rounds.players[1][0].last_name}")

        print("-" * 50)


def enter_results(pair_player, rounds):
    """
    Get input data for a score result of a match.
    :param pair_player: a list of pair of player
    :param rounds: instance of a round
    :return: pair_player
    """
    print("-" * 50)
    message = f">> Round {rounds.name} en cours <<\n"
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


def display_order_rank_player(list_ranking, tournament):
    """
    Display the result of the tournament.
    :param list_ranking:
    :param tournament:
    :return:
    """
    print("\n============== Joueur par Classement =============\n")

    print(f"{tournament.date},\n{tournament.name}\n")
    print("-" * 50)
    print(f"{'N°' : <3} {'Joueurs' : ^30} {'Rank' : >5}")
    print("-" * 50)

    for i, player in enumerate(list_ranking):
        print(f"{i + 1 : <3} {player.full_name : ^30} {player.rank : >5}")
    print("-" * 50)


def display_order_rank_all_actor(list_ranking):
    """
    Display the result of the tournament.
    :param list_ranking:
    :return:
    """
    print("\n============== Joueur par Classement =============\n")

    print("-" * 50)
    print(f"{'N°' : <3} {'Joueurs' : ^30} {'Rank' : >5}")
    print("-" * 50)

    for i, player in enumerate(list_ranking):
        print(f"{i + 1 : <3} {player.full_name : ^30} {player.rank : >5}")
    print("-" * 50)


def display_order_name_player(list_players_sorted_name, tournament):
    """
    Display the result of the tournament.
    :param list_players_sorted_name:
    :param tournament:
    :return:
    """
    print("\n================= Joueur par Nom =================\n")

    print(f"{tournament.date},\n{tournament.name}\n")
    print("-" * 50)
    print(f"{'N°' : <3} {'Joueurs' : ^30} {'Rank' : >5}")
    print("-" * 50)

    for i, player in enumerate(list_players_sorted_name):
        print(f"{i + 1 : <3} {player.full_name : ^30} {player.rank : >5}")
    print("-" * 50)


def display_order_name_all_actor(list_players_sorted_name):
    """
    Display the result of the tournament.
    :param list_players_sorted_name:
    :return:
    """
    print("\n================= Joueur par Nom =================\n")

    print("-" * 50)
    print(f"{'N°' : <3} {'Joueurs' : ^30} {'Rank' : >5}")
    print("-" * 50)

    for i, player in enumerate(list_players_sorted_name):
        print(f"{i + 1 : <3} {player.full_name : ^30} {player.rank : >5}")
    print("-" * 50)


def display_all_tournament(list_tournaments_sorted_date):
    """
    Display the result of the tournament.
    :param list_tournaments_sorted_date:
    :return:
    """
    print("\n============================ Les Tournois ============================\n")

    print(f"{'Nom' : <40} {'Lieu' : ^15} {'Année' : ^15}")
    print("-" * 70)

    for i, tournament in enumerate(list_tournaments_sorted_date):
        print(
            f"{tournament.name: <40} {tournament.location : ^15} {tournament.date : ^15}"
        )
    print("-" * 70)


def display_all_rounds(tournament, tournament_round):
    """
    Display the result of the tournament.
    :param tournament:
    :param tournament_round:
    :return:
    """
    print("\n=================== Les Tours ====================\n")

    print(f"{tournament.date},\n{tournament.name}")

    for i, list_rounds in enumerate(tournament_round):
        print(f"\n---- Tour n°{i + 1} ------------------------------------")
        print("-" * 50)

        for match in list_rounds.matches_round:
            print(f"match {match.name + 1}: {match.players[0]} vs {match.players[1]}")
    print("-" * 50)


def display_all_match(tournament, list_all_matches):
    """
    Display the result of the tournament.
    :param tournament:
    :param list_all_matches:
    :return:
    """
    print("\n=================== Les Matchs ===================\n")

    print(f"{tournament.date},\n{tournament.name}\n")
    print("-" * 50)
    print(f"{'N°' : <3} {'Joueurs' : <20}")
    print("-" * 50)

    for i, match in enumerate(list_all_matches):
        print(f"{i + 1 : <3} {match.players[0]} vs {match.players[1]}")
    print("-" * 50)
