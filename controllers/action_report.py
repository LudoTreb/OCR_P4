import os

from controllers.navigation import NavigationController

from archive import list_archive
from controllers.report_tools import ReportTools

from controllers.pairingtools import PairingTools
from views import DisplayMenuView, DisplayReportView, DisplayTournamentView

display_report = DisplayReportView()
report_tools = ReportTools()
navigation = NavigationController()
pairing_tools = PairingTools()
tournament_view = DisplayTournamentView()


def action_report_menu():
    """
    navigation/display the report menu
    """
    user_action = DisplayMenuView.display_report_menu()
    if user_action == "1":
        os.system("clear")
        list_all_actor = report_tools.create_list_all_actor(list_archive)
        list_ranking = pairing_tools.sort_descending_rank(list_all_actor)
        players_sorted_name = report_tools.sort_name(list_all_actor)
        display_report.display_order_name_all_actor(players_sorted_name)
        display_report.display_order_rank_all_actor(list_ranking)

        navigation.back_main_menu()

    elif user_action == "2":
        os.system("clear")
        display_report.display_all_tournament(report_tools.sort_date(list_archive))

        tournament = navigation.tournament_selected()
        list_ranking = pairing_tools.sort_descending_rank(tournament.players)
        players_sorted_name = report_tools.sort_name(tournament.players)
        display_report.display_order_name_player(players_sorted_name, tournament)
        display_report.display_order_rank_player(list_ranking, tournament)

        navigation.back_main_menu()

    elif user_action == "3":
        os.system("clear")
        display_report.display_all_tournament(report_tools.sort_date(list_archive))

        navigation.back_main_menu()

    elif user_action == "4":
        os.system("clear")
        display_report.display_all_tournament(report_tools.sort_date(list_archive))

        tournament = navigation.tournament_selected()
        display_report.display_all_rounds(tournament, tournament.rounds)
        list_ranking = pairing_tools.sort_descending_score(tournament.players)
        tournament_view.display_ranking_tournament(list_ranking, tournament)

        navigation.back_main_menu()

    elif user_action == "5":
        os.system("clear")
        display_report.display_all_tournament(report_tools.sort_date(list_archive))

        tournament = navigation.tournament_selected()
        list_all_matches = report_tools.create_list_all_matches(tournament.rounds)
        display_report.display_all_match(tournament, list_all_matches)
        list_ranking = pairing_tools.sort_descending_score(tournament.players)
        tournament_view.display_ranking_tournament(list_ranking, tournament)

        navigation.back_main_menu()

    elif user_action == "6":
        os.system("clear")

    elif user_action == "7":
        navigation.quit_program()
