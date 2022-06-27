import datetime

import data
import sys, os

from models import Tournament, Player, Match, Round
from view import fill_information_tournament, display_main_menu, add_player, display_tournament_created_message, \
    display_player_created_message, enter_results, display_round_results_message

numbers_player = 4
new_tournament = None
list_players = []


def sort_descending_rank(list_players) -> list:
    list_players_rank = []
    for player in list_players:
        list_players_rank.append(player.rank)
    list_players_rank_sorted = sorted(list_players_rank, reverse=True)
    return list_players_rank_sorted


def split_list_player(list_players):
    length = len(list_players)
    middle_index = length // 2
    first_half_list_players = list_players[:middle_index]
    second_half_list_players = list_players[middle_index:]
    return first_half_list_players, second_half_list_players


def create_round(name, matches_round):
    created_date = datetime.datetime.now()
    new_round = Round(name, created_date, matches_round)
    return new_round


def pairing_player_round_1(list_players):
    """
    classer la liste des joueurs par ordre décroissant
    diviser en deux 2 listes
    associer les joueurs entre eux
    :return:
    """
    list_players_sorted = sort_descending_rank(list_players)
    list_1, list_2 = split_list_player(list_players_sorted)
    list_pairs = []
    for i in range(len(list_players) // 2):
        player_1 = list_1[i]
        player_2 = list_2[i]
        pair_player = (player_1, player_2)
        list_pairs.append(pair_player)

    return list_pairs


def pairing_player():
    """
    Pair_1 = Le gagnant d'un match rencontre le gagnant de l'autre match
    Pair_2 = les deux autres joureurs
    Tant que Pair_1 a déjà eu lieu alors pour joueur dans Pair_2 faire une nouvelle Pair_1.

    :return:
    """
    pass


def update_score():
    pass


def simulation_matchs():
    """Déterminde de manière aléatoire une gagnat et un perdant
    Pour chaque pair de joueur
    """
    pass


def add_players(numbers_player):
    for i in range(1, numbers_player + 1):
        player_details = add_player(i)
        player = Player(player_details["last_name"],
                        player_details["first_name"],
                        player_details["birth_date"],
                        player_details["gender"],
                        player_details["rank"],
                        )
        list_players.append(player)
    return list_players


def add_match(match_number, list_players):
    new_match = Match(match_number, list_players)
    return new_match


def run():
    user_action = display_main_menu()

    if user_action == "1":
        os.system("clear")
        tournament_details = fill_information_tournament()
        new_tournament = Tournament(tournament_details["name"],
                                    tournament_details["location"],
                                    tournament_details["date"],
                                    tournament_details["number_round"])
        display_tournament_created_message(new_tournament)
        add_players(numbers_player)
        display_player_created_message(list_players)

        for round_number in range(1, int(new_tournament.number_round) + 1):
            if round_number == 1:
                list_pairs = pairing_player_round_1(list_players)

            else:
                # algo des autres rounds
                print("algo next round à faire\n")
                # list_pairs = pairing_player(list_players) 

                break

            round_matches = []
            for match_number, pair in enumerate(list_pairs):
                match = add_match(match_number, pair)
                round_matches.append(match)
            round = create_round(round_number, round_matches)
            new_tournament.rounds.append(round)

            # rentre resultat
            list_scores = []
            for match in round_matches:
                scores = enter_results(match.players)
                match.players_scores = scores
                list_scores.append(match.players_scores)
                print(f"scores: {match.players_scores}")

        display_round_results_message(round_matches, list_scores)






    elif user_action == "2":
        print("script en cours de construction")
    elif user_action == "3":
        print("script en cours de construction")
    elif user_action == "4":
        print(" A bientôt !")
        sys.exit()


if __name__ == "__main__":
    run()
