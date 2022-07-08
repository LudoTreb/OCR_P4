import datetime

import data
import sys, os

from models import Tournament, Player, Match, Round
from view import fill_information_tournament, display_main_menu, fill_information_player, \
    display_tournament_created_message, \
    display_player_created_message, enter_results, display_round_results_message

numbers_player = 4
numbers_round = numbers_player - 1
new_tournament = None
list_players = []


# players_with_temporary_scores = [] # liste temporaire cntenant l'instance de joueur et son score lors round


def sort_descending_rank(list_players) -> list:
    list_players_rank_sorted = sorted(list_players, key=lambda player: player.rank, reverse=True)
    return list_players_rank_sorted  # exemple: [
    # <models.Player object at 0x109763dc0>,
    # <models.Player object at 0x1097638b0>,
    # <models.Player object at 0x109763df0>,
    # <models.Player object at 0x109763d90>]


def split_list_player_round_1(list_players):
    length = len(list_players)
    middle_index = length // 2
    first_half_list_players = list_players[:middle_index]
    second_half_list_players = list_players[middle_index:]
    return first_half_list_players, second_half_list_players  # exemple: ([<models.Player object at 0x10b05bdc0>,
    # <models.Player object at 0x10b05b8b0>],
    # [<models.Player object at 0x10b05bdf0>,
    # <models.Player object at 0x10b05bd90>])


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
    list_1, list_2 = split_list_player_round_1(list_players_sorted)
    list_pairs = []
    for i in range(len(list_players) // 2):
        player_1 = list_1[i]
        player_2 = list_2[i]
        pair_player = (player_1, player_2)
        # enlève joueur d'un potential opposant
        player_1.potential_opponent.remove(player_2)
        player_2.potential_opponent.remove(player_1)

        list_pairs.append(pair_player)

    # print(f"list_pairs pour round 1 : {list_pairs}")
    return list_pairs  # exemple : [(<models.Player object at 0x108bd7dc0>, <models.Player object at 0x108bd7df0>),
    # (<models.Player object at 0x108bd78b0>, <models.Player object at 0x108bd7d90>)]


def sort_descending_score(list_players) -> list:
    list_players_score_sorted = sorted(list_players, key=lambda player: player.score, reverse=True)

    return list_players_score_sorted


def split_list_player_other_round(list_sorted):
    list_first_player = []
    list_second_player = []
    for i in range(0, len(list_sorted), 2):
        list_first_player.append(list_sorted[i])

    for i in range(1, len(list_sorted), 2):
        list_second_player.append(list_sorted[i])

    return list_first_player, list_second_player


def pairing_player(list_players):
    list_pairs = []

    list_sorted_rank = sort_descending_rank(list_players)
    list_sorted = sort_descending_score(list_sorted_rank)

    for i, current_player in enumerate(list_sorted):
        list_next_player = list_sorted[i + 1:len(list_sorted)]

        for next_player in list_next_player:
            if next_player in current_player.potential_opponent:
                pair_player = (current_player, next_player)
                list_sorted.remove(next_player)
                list_pairs.append(pair_player)

                # enlève joueur d'un potential opposant
                current_player.potential_opponent.remove(next_player)
                next_player.potential_opponent.remove(current_player)

                break

            else:
                continue

    return list_pairs


def simulation_matchs():
    """Déterminde de manière aléatoire une gagnat et un perdant
    Pour chaque pair de joueur
    """
    pass


def add_players(numbers_player):

    for i in range(1, int(numbers_player) + 1):
        player_details = fill_information_player(i)
        player = Player(player_details["last_name"],
                        player_details["first_name"],
                        player_details["birth_date"],
                        player_details["gender"],
                        player_details["rank"],
                        )
        list_players.append(player)

    # rempli la liste d'oppsant potentiel
    for player in list_players:
        player.add_potential_opponents(list_players)


def add_match(match_number, list_players):
    new_match = Match(match_number, list_players)
    return new_match


def enter_result_2(round_matches):
    """
    on veut en sortie une liste de tuple
    """
    list_players_with_score = []
    for match in round_matches:
        scores = enter_results(match.players)
        match.players_scores = scores

    list_players_with_score.extend(scores)
    return list_players_with_score

    print(f"scores: {match.players_scores}")


def update_player_score(pair_player):
    for player in pair_player:
        if player[1] == "0,5":
            score_in_dot = player[1].replace(",", ".")
            player[0].score += float(score_in_dot)
        else:
            player[0].score += float(player[1])


def run():
    user_action = display_main_menu()

    if user_action == "1":
        os.system("clear")
        tournament_details = fill_information_tournament()
        new_tournament = Tournament(tournament_details["name"],
                                    tournament_details["location"],
                                    tournament_details["date"],
                                    tournament_details["number_player"])
        display_tournament_created_message(new_tournament)
        add_players(new_tournament.number_player)
        # print(list_players) # test --> [<models.Player object at 0x10100d900>,
        # <models.Player object at 0x10100cdc0>,
        # <models.Player object at 0x10100dab0>,
        # <models.Player object at 0x10100f1f0>]

        display_player_created_message(list_players)

        for round_number in range(1, int(new_tournament.number_round) + 1):
            if round_number == 1:
                list_pairs = pairing_player_round_1(list_players)
                # print(list_pairs) # test --> [(<models.Player object at 0x10100dab0>, <models.Player object at 0x10100cdc0>),
                # (<models.Player object at 0x10100f1f0>, <models.Player object at 0x10100d900>)]

            else:
                # algo des autres rounds
                list_pairs = pairing_player(list_players)

            # print(f"list_pairs:{len({list_pairs})} {list_pairs}, pour le round: {round_number}") # test -->
            round_matches = []
            for match_number, pair in enumerate(list_pairs):
                # print(f"match_number: {match_number}, pair: {pair}") # test --> match_number: 0, pair: (<models.Player object at 0x10100dab0>,
                # <models.Player object at 0x10100cdc0>)
                match = add_match(match_number, pair)
                # print(f"match: {match}")  # test --> ex: <models.Match object at 0x10100ceb0>
                round_matches.append(match)
                # print(f"round_matches: {round_matches}")  # test --> ex: [<models.Match object at 0x10100ceb0>,
                # <models.Match object at 0x10100f1c0>]
            round = create_round(round_number, round_matches)
            # print(f"round: {round}")  # test --> <models.Round object at 0x10100da50>
            new_tournament.rounds.append(round)
            # print(f"new_tournament: {new_tournament}") # test --> <models.Tournament object at 0x101093010>


            if round.name == numbers_round:
                for match in round_matches:
                    scores = enter_results(match.players, round)
                    update_player_score(match.players)

                display_round_results_message(round_matches, round)
                
                # retourner au menu ? Afficher Rapport ?

            else:
                for match in round_matches:
                    scores = enter_results(match.players, round)
                    update_player_score(match.players)

                display_round_results_message(round_matches, round)

            # print(f"round_matches :{round_matches}") # test --> ex: [<models.Match object at 0x100f7fee0>,
            # <models.Match object at 0x100f7fe80>]
        # print(f"test_round_matches_players: {round_matches[0].players}") # test --> ex: [[<models.Player object at 0x102771000>],
        # [<models.Player object at 0x102771030>]]



    elif user_action == "2":
        os.system("clear")
        print("Script en cours de construction \n")
        display_main_menu()

    elif user_action == "3":
        os.system("clear")
        print("Script en cours de construction \n")
        display_main_menu()

    elif user_action == "4":
        os.system("clear")
        print("A bientôt !")
        sys.exit()


if __name__ == "__main__":
    run()
