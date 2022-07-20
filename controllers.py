""" Controllers : Main Program """

import datetime
import os
import sys
from typing import List

from archive import list_archive
from models import Match, Player, Round, Tournament
from views import (display_all_match, display_all_rounds,
                   display_all_tournament, display_main_menu,
                   display_order_name_all_actor, display_order_name_player,
                   display_order_rank_all_actor, display_order_rank_player,
                   display_player_created_message, display_ranking_tournament,
                   display_rapport_menu, display_round_results_message,
                   display_sub_menu, display_tournament_created_message,
                   enter_results, fill_information_player,
                   fill_information_tournament)

NUMBER_PLAYER = 4

new_tournament = None
players = []


def sort_date(tournaments: list) -> list:
    """
    Sort by descending the tournament by the date.

    :param tournaments: list
    :return: list_tournaments_date_sorted: list
    """
    list_tournaments_date_sorted = sorted(
        tournaments,
        key=lambda tournament: datetime.datetime.strptime(tournament.date, "%d/%m/%Y"),
        reverse=True,
    )
    return list_tournaments_date_sorted


def sort_name(players: list) -> list:
    """
    Get a list of player sorted by their last name

    :param players: list
    :return: players_name_sorted: list
    """
    players_name_sorted = sorted(players, key=lambda player: player.last_name)
    return players_name_sorted


def sort_descending_rank(players: list) -> list:
    """
    Get a list of players sorted by their rank in a descending order

    :param players: list
    :return: players_rank_sorted: list
    """
    players_rank_sorted = sorted(players, key=lambda player: player.rank, reverse=True)
    return players_rank_sorted


def split_list_player_round_1(players: list) -> tuple[list, list]:
    """
    Split in half a list of player into two list.
    This is for the first round of the tournament.

    :param players: list
    :return: first_half_players, second_half_players: tuple[list, list]
    """
    length = len(players)
    middle_index = length // 2
    first_half_players = players[:middle_index]
    second_half_players = players[middle_index:]
    return (
        first_half_players,
        second_half_players,
    )


def pairing_player_round_1(players: List[Player]) -> list:
    """
    Sort the list of players in descending order by their rank
    split this list into two list in half
    associate the player one of the first list with
    the player one of the second list...
    Get a list, with a pair of player in tuple.

    :param players: list
    :return:list_pairs: list
    """
    players_sorted = sort_descending_rank(players)
    list_1, list_2 = split_list_player_round_1(players_sorted)
    list_pairs = []
    for i in range(len(players) // 2):
        player_1 = list_1[i]
        player_2 = list_2[i]
        pair_player = (player_1, player_2)

        # remove the player just added from his potential_opponent list
        player_1.potential_opponent.remove(player_2)
        player_2.potential_opponent.remove(player_1)

        list_pairs.append(pair_player)

    return list_pairs


def create_round(name: int, matches_round: list):
    """
    Create a new instance from a class objet Round.

    :param name: int
    :param matches_round: list
    :return: new_round: models.Round
    """
    created_date = datetime.datetime.now()
    new_round = Round(name, created_date, matches_round)

    return new_round


def sort_descending_score(players: list) -> list:
    """
    Get a list of players sorted by their score in a descending order

    :param players: list
    :return: players_score_sorted: list
    """
    players_score_sorted = sorted(
        players, key=lambda player: player.score, reverse=True
    )

    return players_score_sorted


def split_list_player_other_round(players: list) -> tuple[list, list]:
    """
    Split in half a list of player into two list.
    This is for other rounds of the tournament.

    :param players: list
    :return: list_first_player, list_second_player: tuple[list, list]
    """
    list_first_player = []
    list_second_player = []
    for i in range(0, len(players), 2):
        list_first_player.append(players[i])

    for i in range(1, len(players), 2):
        list_second_player.append(players[i])

    return list_first_player, list_second_player


def pairing_player(players: list) -> list:
    """
    Sort the list of players in descending order by their rank
    Sort the list of players in descending order by their score

    associate the first player of the list with the second player.
    If this pair already exists, the first player is associate to the third player...
    until a new pair is created.
    Get a list, with a pair of player in tuple.

    :param players: list
    :return: list_pairs: list
    """
    list_pairs = []

    list_sorted_rank = sort_descending_rank(players)
    list_sorted = sort_descending_score(list_sorted_rank)

    for i, current_player in enumerate(list_sorted):
        list_next_player = list_sorted[i + 1:len(list_sorted)]

        for next_player in list_next_player:
            if next_player in current_player.potential_opponent:
                pair_player = (current_player, next_player)
                list_sorted.remove(next_player)
                list_pairs.append(pair_player)

                # remove the player just added from his potential_opponent list
                current_player.potential_opponent.remove(next_player)
                next_player.potential_opponent.remove(current_player)

                break

            else:
                continue

    return list_pairs


def add_players(number_player: int):
    """
    Create a new instance from the class objet Player.
    Fill the list players with this new instance.

    :param number_player: int

    """
    for i in range(1, int(number_player) + 1):
        player_details = fill_information_player(i)
        player = Player(
            player_details["last_name"],
            player_details["first_name"],
            player_details["birth_date"],
            player_details["gender"],
            player_details["rank"],
        )
        players.append(player)

    # fill the list potential_opponent for all player
    for player in players:
        player.add_potential_opponents(players)


def add_match(match_number: int, players: list):
    """
    Create a new instance from the class objet Match.
    :param match_number: int
    :param players: list
    :return: new_match models.Match
    """
    new_match = Match(match_number, players)
    return new_match


def update_player_score(pair_player: list):
    """
    Update the score attribute of a player.
    :param pair_player:
    """
    for player in pair_player:
        if player[1] == "0,5":
            score_in_dot = player[1].replace(",", ".")
            player[0].score += float(score_in_dot)
        else:
            player[0].score += float(player[1])


def create_list_all_matches(tournament_round: list) -> list:
    """
    Create a list of all matches of a tournament

    :param tournament_round: list
    :return: list_all_matches : list
    """
    list_all_matches = []

    for round in tournament_round:
        for match in round.matches_round:
            list_all_matches.append(match)
    return list_all_matches


def create_list_all_actor(list_archive: list) -> list:
    """
    Create a list of all player of a tounament
    :param list_archive: list
    :return: list_all_actor: list
    """
    list_all_actor = []
    for tournament in list_archive:
        for player in tournament.players:
            list_all_actor.append(player)

    return list_all_actor


def archive_tournament(new_tournament: Tournament):
    """
    Append a new tournament to the list_archive
    :param new_tournament: models.Tournament
    """
    list_archive.append(new_tournament)


def update_players_tournament(players: list, tournament: Tournament):
    """
    Assign the value players to the variable tournament.players
    :param players: list
    :param tournament: models.Tournament

    """
    tournament.players = players


def list_name_tournaments(list_archive: list):
    """
    Create a list of name of all tournament
    :param list_archive: list
    :return: list_name_tournaments: list
    """
    list_name_tournaments = []
    for tournament in list_archive:
        list_name_tournaments.append(tournament.name)
    return list_name_tournaments


def select_tournament():
    """
    Ask to user to choose a name of a tournament
    :return: user_choice: str
    """
    choice_possibility = list_name_tournaments(list_archive)
    user_choice = input("--> Veuillez choisir un nom de tournoi (copier/coller) : ")
    while user_choice not in choice_possibility:
        user_choice = input(
            "Choix non valide.\nSelectionner le nom d'un tournoi (copier/coller) : "
        )

    return user_choice


def quit_program():
    """
    quit the program
    """
    os.system("clear")
    print("-" * 50)
    print("================== A bientôt ! ===================")
    print("-" * 50)
    sys.exit()


def back_main_menu():
    """
    Ask to user to choose between quit the program
    or back to the main menu
    """
    user_action = display_sub_menu()

    if user_action == "2":
        quit_program()

    elif user_action == "1":
        os.system("clear")


def tournament_selected() -> str:
    """
    return wich tournament the user have selected
    :return: tournament_selected: str
    """

    name_tournament = select_tournament()
    for tournament in list_archive:
        if tournament.name == name_tournament:
            tournament_choice = tournament

    return tournament_choice


def action_rapport_menu():
    """
    nagigation/display the rapport menu
    """
    user_action = display_rapport_menu()
    if user_action == "1":
        os.system("clear")
        list_all_actor = create_list_all_actor(list_archive)
        list_ranking = sort_descending_rank(list_all_actor)
        players_sorted_name = sort_name(list_all_actor)
        display_order_name_all_actor(players_sorted_name)
        display_order_rank_all_actor(list_ranking)

        back_main_menu()

    elif user_action == "2":
        os.system("clear")
        display_all_tournament(sort_date(list_archive))

        tournament = tournament_selected()
        list_ranking = sort_descending_rank(tournament.players)
        players_sorted_name = sort_name(tournament.players)
        display_order_name_player(players_sorted_name, tournament)
        display_order_rank_player(list_ranking, tournament)

        back_main_menu()

    elif user_action == "3":
        os.system("clear")
        display_all_tournament(sort_date(list_archive))

        back_main_menu()

    elif user_action == "4":
        os.system("clear")
        display_all_tournament(sort_date(list_archive))

        tournament = tournament_selected()
        display_all_rounds(tournament, tournament.rounds)
        list_ranking = sort_descending_score(tournament.players)
        display_ranking_tournament(list_ranking, tournament)

        back_main_menu()

    elif user_action == "5":
        os.system("clear")
        display_all_tournament(sort_date(list_archive))

        tournament = tournament_selected()
        list_all_matches = create_list_all_matches(tournament.rounds)
        display_all_match(tournament, list_all_matches)
        list_ranking = sort_descending_score(tournament.players)
        display_ranking_tournament(list_ranking, tournament)

        back_main_menu()

    elif user_action == "6":
        os.system("clear")

    elif user_action == "7":
        quit_program()


def run():
    """
    navigation in the main menu.
    Create un tournament.
    Go to the rapport.
    Quit the program.
    """
    while True:
        user_action = display_main_menu()

        if user_action == "1":
            os.system("clear")
            tournament_details = fill_information_tournament()
            new_tournament = Tournament(
                tournament_details["name"],
                tournament_details["location"],
                tournament_details["date"],
                tournament_details["time_control"],
                tournament_details["number_round"],
            )
            display_tournament_created_message(new_tournament)
            add_players(NUMBER_PLAYER)

            update_players_tournament(players, new_tournament)
            display_player_created_message(players)

            for round_number in range(1, int(new_tournament.number_round) + 1):
                if round_number == 1:
                    list_pairs = pairing_player_round_1(players)

                else:

                    list_pairs = pairing_player(players)

                matches_round = []
                for match_number, pair in enumerate(list_pairs):
                    match = add_match(match_number, pair)

                    matches_round.append(match)

                round = create_round(round_number, matches_round)

                new_tournament.rounds.append(round)

                if round.name == new_tournament.number_round:

                    for match in matches_round:
                        enter_results(match.players, round)
                        update_player_score(match.players)

                    archive_tournament(new_tournament)
                    display_round_results_message(matches_round, round)
                    list_ranking = sort_descending_score(players)
                    display_ranking_tournament(list_ranking, new_tournament)

                    back_main_menu()

                else:
                    for match in matches_round:
                        enter_results(match.players, round)
                        update_player_score(match.players)

                    display_round_results_message(matches_round, round)

        elif user_action == "2":
            os.system("clear")
            action_rapport_menu()

        elif user_action == "3":
            quit_program()


if __name__ == "__main__":
    run()
