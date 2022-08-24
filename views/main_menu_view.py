import os

from constances import (
    MAIN_MENU,
    MAIN_MENU_ACTION,
    SUB_MENU,
    SUB_MENU_ACTION,
    MENU_REPORT,
    MENU_REPORT_ACTION,
)


class DisplayMenuView:
    @staticmethod
    def display_main_menu() -> str:
        """
        Display the main menu.
        The user choose an action.
        :return: user_action: str
        """

        user_action = input(MAIN_MENU)
        if user_action not in MAIN_MENU_ACTION:
            os.system("clear")
            print("Choix non valide")
            DisplayMenuView.display_main_menu()
        else:
            return user_action

    @staticmethod
    def display_sub_menu() -> str:
        """
        Display the sub menu.
        The user choose an action
        :return: user_action: str
        """

        user_action = input(SUB_MENU)
        if user_action not in SUB_MENU_ACTION:
            os.system("clear")
            print("Choix non valide")
            DisplayMenuView.display_sub_menu()
        else:
            return user_action

    @staticmethod
    def display_report_menu() -> str:
        """
        Display the rapport menu.
        The user choose an action
        :return: user_action: str
        """

        user_action = input(MENU_REPORT)

        if user_action not in MENU_REPORT_ACTION:
            os.system("clear")
            print("Choix non valide")
            DisplayMenuView.display_report_menu()

        else:
            return user_action
