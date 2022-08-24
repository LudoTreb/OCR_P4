from datetime import datetime

from constances import MESSAGE_INVALID


class ValidateInputView:
    @staticmethod
    def is_valid_gender(message: str) -> str:
        """
        Check if the input is the right string
        :param message: str
        :return: choice: str
        """
        gender = ["h", "f"]
        choice = input(message + " : ")
        while choice not in gender:
            print("Veuillez faire un choix parmi les deux options")
            choice = input(message + " : ")
        return choice

    @staticmethod
    def is_valid_date(message: str) -> str:
        """
        Check if the input is the right date format

        :param message: str
        :return: date: str
        """
        while True:
            try:
                date = input(message + ": ")
                datetime.strptime(date, "%d/%m/%Y")
                return date

            except ValueError:

                print("Veuillez saisir la date au bon format")

    @staticmethod
    def is_input_digit(message: str) -> int:
        """
        Check if the input is digital or not.

        :param message: str
        :return: number_to_check: int
        """
        number_to_check = input(message + ": ")
        while not number_to_check.isdigit():
            print(f"{MESSAGE_INVALID}")
            number_to_check = input()

        return int(number_to_check)

    @staticmethod
    def is_time_control_right(message: str) -> str:
        """
        Check if the input of the time control is right.
        User have choice between bullet, blitz or coup rapide.
        :param message: str
        :return: input_to_check: str
        """
        input_to_check = input(message + ": ")
        possibility = ["bullet", "blitz", "coup rapide"]
        while input_to_check not in possibility:
            print(
                "Seuls les cadences rapides sont possible (bullet, blizt, coup rapide)"
            )
            input_to_check = input(message + ": ")

        return input_to_check
