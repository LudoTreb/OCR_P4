import datetime

import data
import sys, os

from models import Tournament, Player, Match, Round
from view import fill_information_tournament, display_main_menu, fill_information_player, display_tournament_created_message, \
    display_player_created_message, enter_results, display_round_results_message

numbers_player = 4
numbers_round = 3
new_tournament = None
list_players = []
#players_with_temporary_scores = [] # liste temporaire cntenant l'instance de joueur et son score lors round

def sort_descending_rank(list_players) -> list:
    list_players_rank_sorted = sorted(list_players, key=lambda player: player.rank, reverse=True)
    return list_players_rank_sorted # exemple: [
                                                # <models.Player object at 0x109763dc0>,
                                                # <models.Player object at 0x1097638b0>,
                                                # <models.Player object at 0x109763df0>,
                                                # <models.Player object at 0x109763d90>]


def split_list_player(list_players):
    length = len(list_players)
    middle_index = length // 2
    first_half_list_players = list_players[:middle_index]
    second_half_list_players = list_players[middle_index:]
    return first_half_list_players, second_half_list_players # exemple: ([<models.Player object at 0x10b05bdc0>,
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
    list_1, list_2 = split_list_player(list_players_sorted)
    list_pairs = []
    for i in range(len(list_players) // 2):
        player_1 = list_1[i]
        player_2 = list_2[i]
        pair_player = (player_1, player_2)
        list_pairs.append(pair_player)
    #print(f"list_pairs pour round 1 : {list_pairs}")
    return list_pairs # exemple : [(<models.Player object at 0x108bd7dc0>, <models.Player object at 0x108bd7df0>),
                                # (<models.Player object at 0x108bd78b0>, <models.Player object at 0x108bd7d90>)]


def pairing_player(players_with_temporary_scores):
    """
    Pair_1 = Le gagnant d'un match rencontre le gagnant de l'autre match
    Pair_2 = les deux autres joureurs
    Tant que Pair_1 a déjà eu lieu alors pour joueur dans Pair_2 faire une nouvelle Pair_1.

    :return:
    """
    list_pairs = []
    list_winner = []
    list_looser = []
    for i in range(len(players_with_temporary_scores)):

        if players_with_temporary_scores[i][1] == "1":
            list_winner.append(players_with_temporary_scores[i][0])

        else:
            list_looser.append(players_with_temporary_scores[i][0])

        list_pairs = [tuple(list_winner), tuple(list_looser)]
    #print(f"list_pairs pour les autres round : {list_pairs}")
    # exemple et c'est pas ce que l'on veut:  [(<models.Player object at 0x104bcbcd0>,),
                                            # (<models.Player object at 0x104bcbd30>,)]

    return list_pairs



def update_score():
    pass


def simulation_matchs():
    """Déterminde de manière aléatoire une gagnat et un perdant
    Pour chaque pair de joueur
    """
    pass


def add_players(numbers_player):
    for i in range(1, numbers_player + 1):
        player_details = fill_information_player(i)
        player = Player(player_details["last_name"],
                        player_details["first_name"],
                        player_details["birth_date"],
                        player_details["gender"],
                        player_details["rank"],
                        )
        list_players.append(player)


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
            score_in_dot = player[1].replace(",",".")
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
                                    tournament_details["number_round"])
        display_tournament_created_message(new_tournament)
        add_players(numbers_player)
        #print(list_players) # test --> [<models.Player object at 0x10100d900>,
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
                list_pairs = pairing_player(players_with_temporary_scores)

            #print(f"list_pairs:{len({list_pairs})} {list_pairs}, pour le round: {round_number}") # test -->
            round_matches = []
            for match_number, pair in enumerate(list_pairs):
                # print(f"match_number: {match_number}, pair: {pair}") # test --> match_number: 0, pair: (<models.Player object at 0x10100dab0>,
                                                                                                    # <models.Player object at 0x10100cdc0>)
                match = add_match(match_number, pair)
                # print(f"match: {match}")  # test --> ex: <models.Match object at 0x10100ceb0>
                round_matches.append(match)
                #print(f"round_matches: {round_matches}")  # test --> ex: [<models.Match object at 0x10100ceb0>,
                                                                    # <models.Match object at 0x10100f1c0>]
            round = create_round(round_number, round_matches)
            # print(f"round: {round}")  # test --> <models.Round object at 0x10100da50>
            new_tournament.rounds.append(round)
            #print(f"new_tournament: {new_tournament}") # test --> <models.Tournament object at 0x101093010>

            players_with_temporary_scores = []
            if round.name == 4:
                print(f"Round {round.name} , c'est le dernier !")
                for match in round_matches:
                    scores = enter_results(match.players)
                    update_player_score(match.players)

                display_round_results_message(round_matches, round)

                print("C'est fini -- fonction retour au menu à faire ? pour acceder au rapport")

            else:
                print(f"Round {round.name} en cours")
                players_with_temporary_scores.clear()
                for match in round_matches:
                    scores = enter_results(match.players)
                    update_player_score(match.players)
                    for i in range(len(scores)):
                        players_with_temporary_scores.append(scores[i])
                    #print(f"players_with_temporary_scores : {players_with_temporary_scores}") # test --> ex :
                                                                        # [[<models.Player object at 0x108e03be0>, '1'],
                                                                        # [<models.Player object at 0x108e03b20>, '0'],
                                                                        # [<models.Player object at 0x108e03b50>, '0'],
                                                                        # [<models.Player object at 0x108e03b80>, '1']]
                display_round_results_message(round_matches, round)

            #print(f"round_matches :{round_matches}") # test --> ex: [<models.Match object at 0x100f7fee0>,
                                                            # <models.Match object at 0x100f7fe80>]
        #print(f"test_round_matches_players: {round_matches[0].players}") # test --> ex: [[<models.Player object at 0x102771000>],
                                                                                    # [<models.Player object at 0x102771030>]]




    elif user_action == "2":
        print("script en cours de construction")
    elif user_action == "3":
        print("script en cours de construction")
    elif user_action == "4":
        print(" A bientôt !")
        sys.exit()


if __name__ == "__main__":
    run()
