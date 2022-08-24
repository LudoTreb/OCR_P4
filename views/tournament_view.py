from views.validate_input import ValidateInputView


class DisplayTournamentView:
    def fill_information_tournament(self) -> dict:
        """
        Get input data for a tournament in the form of dictonary

        :return: dict
        """
        print("-" * 50)
        message = "Veuillez saisir les informations du tournoi \n"
        print(f"{message : ^50}")

        name_tournament = input("Nom du tournoi : ")
        localisation_tournament = input("Lieu du tournoi : ")
        date_tournament = ValidateInputView.is_valid_date(
            "Date du tournoi (jj/mm/aaaa)"
        )
        time_control = ValidateInputView.is_time_control_right("Cadence (coup rapide)")
        number_round_tournament = ValidateInputView.is_input_digit(
            "Nombre de round du tournoi [4]"
        )

        return {
            "name": name_tournament,
            "location": localisation_tournament,
            "date": date_tournament,
            "time_control": time_control,
            "number_round": number_round_tournament,
        }

    def display_tournament_created_message(self, new_tournament):
        """
        Display the data of a tournament
        :param new_tournament: models.Tournament

        """
        print("-" * 50)
        message = "Tournoi a bien été crée\n"
        print(f"{message : ^50}")
        print(f"{new_tournament.date},\n{new_tournament.name} à {new_tournament.location},\n"
              f"en {new_tournament.number_round} rondes, {new_tournament.time_control}")
        print("-" * 50 + "\n" + "-" * 50)

    def display_round_results_message(self, round_matches: list, rounds):
        """
        Display the result of all the matches of a round.

        :param round_matches: list
        :param rounds: models.Round
        """
        print("-" * 50 + "\n" + "-" * 50)

        message = f"<< Résumé du Round {rounds.name} >>\n"
        print(f"{message : ^50}")
        for number_match, rounds in enumerate(round_matches):
            print(
                f"Match {number_match + 1}: {rounds.players[0][0].last_name} contre {rounds.players[1][0].last_name} "
            )
            if rounds.players[0][1] == "0.5" or rounds.players[0][1] == "0,5":
                print("Résultat : Match nul")
            elif rounds.players[0][1] == "1":
                print(f"Résultat : Victoire de {rounds.players[0][0].last_name}")
            else:
                print(f"Résultat : Victoire de {rounds.players[1][0].last_name}")

            print("-" * 50)

    def enter_results(self, pair_player: list, rounds) -> list:
        """
        Get input data for a score result of a match
        and display it.

        :param pair_player: list
        :param rounds: models.Round
        :return: pair_player: list
        """
        print("-" * 50)
        message = f">> Round {rounds.name} en cours <<\n"
        print(f"{message : ^50}")
        print(
            " ⎮ Pour rappel des notations des scores :      ⎮\n ⎮ victoire = 1  défaite = 0  match nul =  0.5 ⎮\n"
        )

        print("Veuillez rentrer le score du match : ")
        print(f"{pair_player[0][0].last_name} contre {pair_player[1][0].last_name}\n")
        for player in pair_player:
            result_possibility = ["1", "0", "0.5", "0,5"]
            player[1] = input(f"> {player[0].last_name} : ")
            while player[1] not in result_possibility:
                player[1] = input(f"> {player[0].last_name} : ")

        return pair_player

    def display_ranking_tournament(self, list_ranking: list, tournament):
        """
        Display the result of the tournament.

        :param list_ranking: list
        :param tournament: models.Tournament
        """
        print("\n==================== RESULTATS ===================\n")
        print(f"{tournament.date},\n{tournament.name}\n")
        print(f"{'N°' : <3} {'Joueur' : ^15} {'Score' : >3}")

        for i, player in enumerate(list_ranking):
            print(f"{i + 1 : <3} {player.last_name : ^15} {player.score : >3}")
