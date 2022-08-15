import datetime
from typing import List

from models import Player, Tournament, Round, Match
from views import DisplayPlayerView

new_tournament = None


class TournamentToolsController:

    def create_round(self, name: int, matches_round: list):
        """
        Create a new instance from a class objet Round.

        :param name: int
        :param matches_round: list
        :return: new_round: models.Round
        """
        created_date = datetime.datetime.now()
        new_round = Round(name, created_date, matches_round)

        return new_round

    def add_players(self, number_player: int) -> list:
        """
        Create a new instance from the class objet Player.
        Fill the list players with this new instance.

        :param number_player: int

        """
        players = []
        for i in range(1, int(number_player) + 1):
            player_details = DisplayPlayerView.fill_information_player(i)
            player = Player(
                player_details["last_name"],
                player_details["first_name"],
                player_details["birth_date"],
                player_details["gender"],
                player_details["rank"],
            )
            players.append(player)

        # fill the list potential_opponent for all player
        for player in players:
            player.add_potential_opponents(players)

        return players


    def add_match(self, match_number: int, players: List[Player]):
        """
        Create a new instance from the class objet Match.
        :param match_number: int
        :param players: list
        :return: new_match models.Match
        """
        new_match = Match(match_number, players)
        return new_match

    def update_player_score(self, pair_player: list):
        """
        Update the score attribute of a player.
        :param pair_player:
        """
        for player in pair_player:
            if player[1] == "0,5":
                score_in_dot = player[1].replace(",", ".")
                player[0].score += float(score_in_dot)
            else:
                player[0].score += float(player[1])

    def update_players_tournament(self, players: List[Player], tournament: Tournament):
        """
        Assign the value players to the variable tournament.players
        :param players: list
        :param tournament: models.Tournament

        """
        tournament.players = players
