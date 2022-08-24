from views.validate_input import ValidateInputView


class DisplayPlayerView:
    @staticmethod
    def fill_information_player(player_number: int) -> dict:
        """
        Get input data for players_1 in the form of dictonary

        :param player_number: int
        :return: dict
        """
        message = f"Veuillez saisir les informations du joueur {player_number}\n"
        print(f"{message : ^50}")

        last_name_player = input("Nom du joueur : ")
        first_name_player = input("Prénom du joueur : ")
        birth_date_player = ValidateInputView.is_valid_date(
            "Date de naissance du joueur (jj/mm/aaaa)"
        )
        gender_player = ValidateInputView.is_valid_gender("Sexe du joueur (f/h)")
        rank_player = ValidateInputView.is_input_digit("Classement du joueur")

        print("-" * 50)

        return {
            "last_name": last_name_player,
            "first_name": first_name_player,
            "birth_date": birth_date_player,
            "gender": gender_player,
            "rank": rank_player,
        }

    @staticmethod
    def display_player_created_message(players: list):
        """
        Display the data of all player of a list
        :param players:

        """
        print("-" * 50)
        message = "Les joueurs ont bien été saisis \n"
        print(f"{message : ^50}")

        for player in players:
            print(
                f"{player.last_name} {player.first_name}, rank: {player.rank}, score: {player.score}"
            )

        print("-" * 50)
