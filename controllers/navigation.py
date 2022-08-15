import os
import sys

from archive import list_archive
from controllers.report_tools import ReportTools
from views import DisplayMenuView

report_tools = ReportTools()


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

    def tournament_selected(self) -> str:
        """
        return wich tournament the user have selected
        :return: tournament_selected: str
        """

        name_tournament = self.select_tournament()
        for tournament in list_archive:
            if tournament.name == name_tournament:
                tournament_choice = tournament

        return tournament_choice

    def select_tournament(self):
        """
        Ask to user to choose a name of a tournament
        :return: user_choice: str
        """
        choice_possibility = report_tools.list_name_tournaments(list_archive)
        user_choice = input("--> Veuillez choisir un nom de tournoi (copier/coller) : ")
        while user_choice not in choice_possibility:
            user_choice = input(
                "Choix non valide.\nSelectionner le nom d'un tournoi (copier/coller) : "
            )

        return user_choice
