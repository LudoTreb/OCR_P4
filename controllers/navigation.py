import os
import sys

from typing import List
from models import Tournament

from views.main_menu_view import DisplayMenuView


class NavigationController:
    def quit_program(self):
        """
        quit the program
        """
        os.system("clear")
        print("-" * 50)
        print("================== A bientôt ! ===================")
        print("-" * 50)
        sys.exit()

    def back_main_menu(self):
        """
        Ask to user to choose between quit the program
        or back to the main menu
        """
        user_action = DisplayMenuView.display_sub_menu()

        if user_action == "2":
            self.quit_program()

        elif user_action == "1":
            os.system("clear")

    def select_tournament(self, tournaments: list) -> int:
        """
        Ask the user to choose a name of a tournament
        :param tournaments:
        :return: choice_tournament: int
        """
        choice_possibility_tournament = []
        for i in range(len(tournaments)):
            choice_possibility_tournament.append(i + 1)

        choice_tournament = int(input("choisir un tournoi (n°): "))
        while choice_tournament not in choice_possibility_tournament:
            choice_tournament = int(input("non valide. Choix un numéro de tournoi"))

        return choice_tournament

    def tournament_selected(
        self, choice_tournament: int, tournaments_archive: List[Tournament]
    ) -> list:
        """
        by the index a tournament is choose in a list of tournament
        :param choice_tournament: int
        :param tournaments_archive: list
        :return: tournament_selected: list (one tournament)
        """
        tournament_selected = tournaments_archive[choice_tournament - 1]
        return tournament_selected
