import data
import sys, os

from models import Tournament
from view import fill_information_tournament, display_main_menu, add_player

numbers_player = 2
new_tournament = None
list_player = []


def sort_descending_rank(list_players) -> list:
    list_players_rank = []
    for player in data.list_players:
        list_players_rank.append(player.rank)
    list_players_rank_sorted = sorted(list_players_rank, reverse=True)
    return list_players_rank_sorted



def run():
    user_action = display_main_menu()

    if user_action == "1":
        os.system("clear")
        tournament_details = fill_information_tournament()
        new_tournament = Tournament(tournament_details["name"],
                                    tournament_details["location"],
                                    tournament_details["date"],
                                    tournament_details["number_round"])
        print("-" * 50)
        print("Tournoi est bien créer :")
        print(new_tournament.__dict__)
        print("-" * 50 + "\n" + "-" * 50)

        for i in range(1, numbers_player + 1):
            print(f"information joueur_{i}")
            player = add_player()
            list_player.append(player)
            print("-" * 50)

        print("-" * 50)
        print("Les joueurs ont bien été saisis :")
        print(list_player)
        print("-" * 50 + "\n" + "-" * 50)





    elif user_action == "2":
        print("script en cours de construction")
    elif user_action == "3":
        print("script en cours de construction")
    elif user_action == "4":
        print(" A bientôt !")
        sys.exit()


if __name__ == "__main__":
    run()
