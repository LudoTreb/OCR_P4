import os

from controllers.navigation import NavigationController
from controllers.serialized import InstancingSerializedController
from controllers.report_tools import ReportTools
from controllers.pairingtools import PairingTools
from models import tournaments_table, players_table
from views.tournament_view import DisplayTournamentView
from views.report_view import DisplayReportView
from views.main_menu_view import DisplayMenuView

display_report = DisplayReportView()
report_tools = ReportTools()
navigation = NavigationController()
pairing_tools = PairingTools()
tournament_view = DisplayTournamentView()
instancing_serialized = InstancingSerializedController()


def action_report_menu():
    """
    navigation/display the report menu
    """
    tournaments_serialized = tournaments_table.all()
    players_serialized = players_table.all()
    tournaments_archive = instancing_serialized.instancing_serialized_tournament(
        tournaments_serialized
    )
    players_archive = instancing_serialized.instancing_serialized_player(
        players_serialized
    )

    user_action = DisplayMenuView.display_report_menu()

    if user_action == "1":
        os.system("clear")
        list_ranking = report_tools.sort_descending_rank(players_archive)
        players_sorted_name = report_tools.sort_name(players_archive)
        display_report.display_order_name_all_actor(players_sorted_name)
        display_report.display_order_rank_all_actor(list_ranking)

        navigation.back_main_menu()

    elif user_action == "2":
        os.system("clear")
        display_report.display_all_tournament(
            report_tools.sort_date(tournaments_archive)
        )

        choice_tournament = navigation.select_tournament(tournaments_archive)
        tournament_selected = navigation.tournament_selected(
            choice_tournament, tournaments_archive
        )

        list_ranking = report_tools.sort_descending_rank(tournament_selected.players)
        players_sorted_name = report_tools.sort_name(tournament_selected.players)
        display_report.display_order_name_player(
            players_sorted_name, tournament_selected
        )
        display_report.display_order_rank_player(list_ranking, tournament_selected)

        navigation.back_main_menu()

    elif user_action == "3":
        os.system("clear")
        display_report.display_all_tournament(
            report_tools.sort_date(tournaments_archive)
        )

        navigation.back_main_menu()

    elif user_action == "4":
        os.system("clear")
        display_report.display_all_tournament(
            report_tools.sort_date(tournaments_archive)
        )

        choice_tournament = navigation.select_tournament(tournaments_archive)
        tournament_selected = navigation.tournament_selected(
            choice_tournament, tournaments_archive
        )

        display_report.display_all_rounds(tournament_selected)
        list_ranking = report_tools.sort_descending_score(tournament_selected.players)
        tournament_view.display_ranking_tournament(list_ranking, tournament_selected)

        navigation.back_main_menu()

    elif user_action == "5":
        os.system("clear")
        display_report.display_all_tournament(
            report_tools.sort_date(tournaments_archive)
        )

        choice_tournament = navigation.select_tournament(tournaments_archive)
        tournament_selected = navigation.tournament_selected(
            choice_tournament, tournaments_archive
        )

        list_all_matches = report_tools.create_list_all_matches(
            tournament_selected.rounds
        )
        display_report.display_all_match(tournament_selected, list_all_matches)
        list_ranking = pairing_tools.sort_descending_score(tournament_selected.players)
        tournament_view.display_ranking_tournament(list_ranking, tournament_selected)

        navigation.back_main_menu()

    elif user_action == "6":
        os.system("clear")

    elif user_action == "7":
        navigation.quit_program()
