class DisplayReportView:
    def display_order_rank_player(self, list_ranking: list, tournament):
        """
        Display all players_1 of the tournament ordored by their rank.

        :param list_ranking: list
        :param tournament: models.Tournament
        """
        print("\n============== Joueur par Classement =============\n")

        print(f"{tournament.date},\n{tournament.name}\n")
        print("-" * 50)
        print(f"{'N°' : <3} {'Joueurs' : ^30} {'Rank' : >5}")
        print("-" * 50)

        for i, player in enumerate(list_ranking):
            print(f"{i + 1 : <3} {player.full_name : ^30} {player.rank : >5}")
        print("-" * 50)

    def display_order_rank_all_actor(self, list_ranking: list):
        """
        Display all actor of all tournament ordered by their rank.

        :param list_ranking: list
        """
        print("\n============== Joueur par Classement =============\n")

        print("-" * 50)
        print(f"{'N°' : <3} {'Joueurs' : ^30} {'Rank' : >5}")
        print("-" * 50)

        for i, player in enumerate(list_ranking):
            print(f"{i + 1 : <3} {player.full_name : ^30} {player.rank : >5}")
        print("-" * 50)

    def display_order_name_player(self, players_sorted_name: list, tournament):
        """
        Display all players_1 of all tournament ordered by their name.

        :param players_sorted_name: list
        :param tournament: models.Tournament
        """
        print("\n================= Joueur par Nom =================\n")

        print(f"{tournament.date},\n{tournament.name}\n")
        print("-" * 50)
        print(f"{'N°' : <3} {'Joueurs' : ^30} {'Rank' : >5}")
        print("-" * 50)

        for i, player in enumerate(players_sorted_name):
            print(f"{i + 1 : <3} {player.full_name : ^30} {player.rank : >5}")
        print("-" * 50)

    def display_order_name_all_actor(self, players_sorted_name: list):
        """
        Display all actor of all tournament ordered by their name.

        :param players_sorted_name: list
        """
        print("\n================= Joueur par Nom =================\n")

        print("-" * 50)
        print(f"{'N°' : <3} {'Joueurs' : ^30} {'Rank' : >5}")
        print("-" * 50)

        for i, player in enumerate(players_sorted_name):
            print(f"{i + 1 : <3} {player.full_name : ^30} {player.rank : >5}")
        print("-" * 50)

    def display_all_tournament(self, list_tournaments_sorted_date: list):
        """
        Display all tournament

        :param list_tournaments_sorted_date: list
        """
        print(
            "\n============================ Les Tournois ============================\n"
        )

        print(f"{'Nom' : <40} {'Lieu' : ^15} {'Année' : ^15}")
        print("-" * 70)

        for i, tournament in enumerate(list_tournaments_sorted_date):
            print(
                f"{i + 1} {tournament.name: <40} {tournament.location : ^15} {tournament.date : ^15}"
            )
        print("-" * 70)

    def display_all_rounds(self, tournament):
        """
        Display the result of all rounds of a tournament.

        :param tournament: models.Tournament
        """
        print("\n=================== Les Tours ====================\n")

        print(f"{tournament.date},\n{tournament.name}")

        for i, list_rounds in enumerate(tournament.rounds):
            print(f"\n---- Tour n°{i + 1} ------------------------------------")
            print("-" * 50)

            for match in list_rounds.matches_round:
                print(
                    f"match {match.name[0]}: {match.players[0][0][0]}({match.players[0][0][1]}) vs"
                    f" {match.players[1][0][0]}({match.players[1][0][1]})"
                )
        print("-" * 50)

    def display_all_match(self, tournament, list_all_matches: list):
        """
        Display all matches of a tournament.

        :param tournament: models.Tournament
        :param list_all_matches: list
        """
        print("\n=================== Les Matchs ===================\n")

        print(f"{tournament.date},\n{tournament.name}\n")
        print("-" * 50)
        print(f"{'N°' : <3} {'Joueurs' : <20}")
        print("-" * 50)

        for i, match in enumerate(list_all_matches):
            print(
                f"{i + 1 : <3} {match.players[0][0][0]}({match.players[0][0][1]}) vs"
                f" {match.players[1][0][0]}({match.players[1][0][1]})"
            )
        print("-" * 50)
