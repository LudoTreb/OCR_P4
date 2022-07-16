import models
from itertools import repeat
from view import enter_results
from datetime import datetime
import re

# Tournament 1 archive

tournament_1 = models.Tournament("Tournoi d'échec de St Brieux", "St Brieux", "22/06/2022", 4)

player_1 = models.Player("Blot", "Denis", "24 juin 1998", "h", 3560, 1)
player_2 = models.Player("Vallet", "Virginie", "02 janvier 2003", "f", 4300, 4)
player_3 = models.Player("Coulon", "Maurice", "16 avril 2001", "h", 2030, 0)
player_4 = models.Player("Caron", "Pauline", "03 juin 2000", "f", 3700, 3)
player_5 = models.Player("Carpentier", "Yves", "21 octobre 2000", "h", 3560, 3)
player_6 = models.Player("Dubois", "Madeleine", "12 septembre 1999", "f", 3230, 0)
player_7 = models.Player("Bertin", "Astrid", "24 décembre 1998", "f", 3750, 3)
player_8 = models.Player("Martel", "Patricia", "29 mai 2001", "f", 3560, 2)

list_players = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]
tournament_1.list_players = list_players

# Round 1
match_1 = models.Match("match 1", [player_2, player_5])
match_2 = models.Match("match 2", [player_7, player_8])
match_3 = models.Match("match 3", [player_4, player_6])
match_4 = models.Match("match 4", [player_1, player_3])

matches_round_1 = [match_1, match_2, match_3, match_4]
round_1 = models.Round(1, "22/06/2022", matches_round_1)

# Round 2
match_5 = models.Match("match 1", [player_2, player_7])
match_6 = models.Match("match 2", [player_4, player_1])
match_7 = models.Match("match 3", [player_8, player_6])
match_8 = models.Match("match 4", [player_5, player_3])

matches_round_2 = [match_5, match_6, match_7, match_8]
round_2 = models.Round(2, "22/06/2022", matches_round_2)

# Round 3
match_9 = models.Match("match 1", [player_2, player_4])
match_10 = models.Match("match 2", [player_8, player_1])
match_11 = models.Match("match 3", [player_5, player_6])
match_12 = models.Match("match 4", [player_7, player_3])

matches_round_3 = [match_9, match_10, match_11, match_12]
round_3 = models.Round(3, "22/06/2022", matches_round_3)

# Round 4
match_13 = models.Match("match 1", [player_2, player_8])
match_14 = models.Match("match 2", [player_5, player_1])
match_15 = models.Match("match 3", [player_7, player_6])
match_16 = models.Match("match 4", [player_4, player_3])

matches_round_4 = [match_13, match_14, match_15, match_16]
round_4 = models.Round(4, "22/06/2022", matches_round_4)

list_round = [round_1, round_2, round_3, round_4]
tournament_1.rounds = list_round

# Autre tounoi mais juste l'instance de tounoi, pas de joueur ou autre

# Tournoi 2
tournament_2 = models.Tournament("20th Rochefort Chess Festival - Masters", "Rochefort", "12/08/2022", 4)

player_1 = models.Player("Huet", "Adèle", "24 juin 1998", "f", 3560, 1)
player_2 = models.Player("Morin", "Gilles", "02 janvier 2003", "h", 4300, 4)
player_3 = models.Player("Bazin", "Alfred", "16 avril 2001", "h", 2030, 0)
player_4 = models.Player("Vasseur", "Aurore", "03 juin 2000", "f", 3700, 3)
player_5 = models.Player("Letellier", "Gérard", "21 octobre 2000", "h", 3555, 3)
player_6 = models.Player("Chretien", "Élise", "12 septembre 1999", "f", 3230, 0)
player_7 = models.Player("Diaz", "Juliette", "24 décembre 1998", "f", 3780, 3)
player_8 = models.Player("Bouvet", "Alex", "29 mai 2001", "h", 3550, 2)

list_players_2 = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]
tournament_2.list_players = list_players_2

# Tournoi 3
tournament_3 = models.Tournament("5ème Open Fide de Lavérune", "Lavérune", "24/03/2022", 4)

player_1 = models.Player("Laine", "Joséphine", "24 juin 1998", "f", 3570, 1)
player_2 = models.Player("Martel", "Éric", "02 janvier 2003", "h", 4310, 4)
player_3 = models.Player("Morvan", "Nicolas", "16 avril 2001", "h", 2030, 0)
player_4 = models.Player("Lambert", "Jeanne", "03 juin 2000", "f", 3700, 3)
player_5 = models.Player("Joly", "André", "21 octobre 2000", "h", 3560, 3)
player_6 = models.Player("Grenier", "Suzanne", "12 septembre 1999", "f", 3230, 0)
player_7 = models.Player("Diaz", "Juliette", "24 décembre 1998", "f", 3790, 3)
player_8 = models.Player("Colin", "Auguste", "29 mai 2001", "h", 3530, 2)

list_players_3 = [player_1, player_2, player_3, player_4, player_5, player_6, player_7, player_8]

list_archive = [tournament_1, tournament_2, tournament_3]


def display_order_rank_player(list_players, tournament):
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
    list_ranking = sort_descending_rank(list_players)
    for i, player in enumerate(list_ranking):
        print(f"{i + 1 : <3} {player.full_name : ^30} {player.rank : >5}")
    print("-" * 50)


def display_order_name_player(list_players, tournament):
    """
    Display the result of the tournament.
    :param list_players:
    :param tournament:
    :return:
    """
    print("\n================= Joueur par Nom =================\n")

    print(f"{tournament.date},\n{tournament.name}\n")
    print("-" * 50)
    print(f"{'N°' : <3} {'Joueurs' : ^30}")
    print("-" * 50)
    list_players_sorted_name = sort_name(list_players)
    for i, player in enumerate(list_players_sorted_name):
        print(f"{i + 1 : <3} {player.full_name : ^30}")
    print("-" * 50)


def display_all_tournament(list_tournaments):
    """
    Display the result of the tournament.
    :param list_players:
    :param tournament:
    :return:
    """
    print("\n============================ Les Tournois ============================\n")

    print(f"{'Nom' : <40} {'Lieu' : ^15} {'Année' : ^15}")
    print("-" * 70)

    for i, tournament in enumerate(sort_date(list_tournaments)):
        print(f"{tournament.name: <40} {tournament.location : ^15} {tournament.date : ^15}")
    print("-" * 70)


def display_all_rounds(tournament, tournament_round):
    """
    Display the result of the tournament.
    :param list_players:
    :param tournament:
    :return:
    """
    print("\n=================== Les Tours ====================\n")

    print(f"{tournament.date},\n{tournament.name}")

    for i, round in enumerate(tournament_round):
        print(f"\n---- Tour n°{i + 1} ------------------------------------")
        print("-" * 50)

        for match in round.matches_round:
            print(f"{match.name}: {match.players[0]} vs {match.players[1]}")
    print("-" * 50)


def create_list_all_matches(tournament_round):
    list_all_matches = []

    for round in tournament_round:
        for match in round.matches_round:
            list_all_matches.append(match)
    return list_all_matches


def display_all_match(tournament, tournament_round):
    """
    Display the result of the tournament.
    :param list_players:
    :param tournament:
    :return:
    """
    print("\n=================== Les Matchs ===================\n")

    print(f"{tournament.date},\n{tournament.name}\n")
    print("-" * 50)
    print(f"{'N°' : <3} {'Joueurs' : <20}")
    print("-" * 50)
    list_all_matches = create_list_all_matches(tournament_round)
    for i, match in enumerate(list_all_matches):
        print(f"{i + 1 : <3} {match.players[0]} vs {match.players[1]}")
    print("-" * 50)


def sort_date(list_tournaments):
    list_tournaments_date_sorted = sorted(
        list_tournaments, key=lambda tournament: datetime.strptime(tournament.date, '%d/%m/%Y'), reverse=True
    )
    return list_tournaments_date_sorted


def sort_descending_rank(list_players) -> list:
    """
    Get a list of players sorted by their rank in a descending order

    :param list_players: a list of player unordered
    :return: list_players_rank_sorted
    """
    list_players_rank_sorted = sorted(
        list_players, key=lambda player: player.rank, reverse=True
    )
    return list_players_rank_sorted


def sort_name(list_players) -> list:
    """
    Get a list of player sorted by their last name

    :param list_players: a list of player unordered
    :return: list_players_name_sorted
    """
    list_players_name_sorted = sorted(list_players, key=lambda player: player.last_name)
    return list_players_name_sorted


def create_list_all_actor(list_archive):
    list_all_actor = []
    for tournament in list_archive:
        for player in tournament.list_players:
            list_all_actor.append(player)

    return list_all_actor


def archive_tournament(new_tournament):
    list_archive.append(new_tournament)


def update_list_players_tournament(list_players, tournament):
    tournament.list_players = list_players


display_order_name_player(tournament_1.list_players, tournament_1)
display_order_rank_player(tournament_1.list_players, tournament_1)
display_all_tournament(list_archive)
display_all_rounds(tournament_1, tournament_1.rounds)
display_all_match(tournament_1, tournament_1.rounds)
