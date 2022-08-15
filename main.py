import os

from constances import NUMBER_PLAYER
from controllers.tournament_tools import TournamentToolsController
from controllers.action_report import action_report_menu
from controllers.navigation import NavigationController
from controllers.report_tools import ReportTools
from controllers.pairingtools import PairingTools
from controllers.pairing_player import PairingPlayerController

from models import Tournament
from views import DisplayTournamentView, DisplayMenuView, DisplayPlayerView

new_tournament = None
players = []


def run():
    """
    navigation in the main menu.
    Create a tournament.
    Go to the report.
    Quit the program.
    """
    report_tools = ReportTools()
    tournament_tools = TournamentToolsController()
    tournament_view = DisplayTournamentView()
    pairing_tools = PairingTools()
    navigation = NavigationController()

    while True:
        user_action = DisplayMenuView.display_main_menu()

        if user_action == "1":
            os.system("clear")

            tournament_details = tournament_view.fill_information_tournament()
            new_tournament = Tournament(
                tournament_details["name"],
                tournament_details["location"],
                tournament_details["date"],
                tournament_details["time_control"],
                tournament_details["number_round"],
            )
            tournament_view.display_tournament_created_message(new_tournament)
            players = tournament_tools.add_players(NUMBER_PLAYER)

            tournament_tools.update_players_tournament(players, new_tournament)
            DisplayPlayerView.display_player_created_message(players)

            for round_number in range(1, int(new_tournament.number_round) + 1):
                if round_number == 1:
                    list_pairs = PairingPlayerController.pairing_player_round_1(players)

                else:

                    list_pairs = PairingPlayerController.pairing_player(players)

                matches_round = []
                for match_number, pair in enumerate(list_pairs):
                    match = tournament_tools.add_match(match_number, pair)

                    matches_round.append(match)

                round = tournament_tools.create_round(round_number, matches_round)

                new_tournament.rounds.append(round)

                if round.name == new_tournament.number_round:

                    for match in matches_round:
                        tournament_view.enter_results(match.players, round)
                        tournament_tools.update_player_score(match.players)

                    report_tools.archive_tournament(new_tournament)
                    tournament_view.display_round_results_message(matches_round, round)
                    list_ranking = pairing_tools.sort_descending_score(players)
                    tournament_view.display_ranking_tournament(list_ranking, new_tournament)

                    navigation.back_main_menu()

                else:
                    for match in matches_round:
                        tournament_view.enter_results(match.players, round)
                        tournament_tools.update_player_score(match.players)

                    tournament_view.display_round_results_message(matches_round, round)

        elif user_action == "2":
            os.system("clear")
            action_report_menu()

        elif user_action == "3":
            navigation.quit_program()


if __name__ == "__main__":
    run()
