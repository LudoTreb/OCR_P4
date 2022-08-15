import datetime

from typing import List

from archive import list_archive
from models import Tournament, Player


class ReportTools:

    def sort_date(self, tournaments: List[Tournament]) -> list:
        """
        Sort by descending the tournament by the date.

        :param tournaments: list
        :return: list_tournaments_date_sorted: list
        """
        list_tournaments_date_sorted = sorted(
            tournaments,
            key=lambda tournament: datetime.datetime.strptime(tournament.date, "%d/%m/%Y"),
            reverse=True,
        )
        return list_tournaments_date_sorted

    def sort_name(self, players: List[Player]) -> list:
        """
        Get a list of player sorted by their last name

        :param players: list
        :return: players_name_sorted: list
        """
        players_name_sorted = sorted(players, key=lambda player: player.last_name)
        return players_name_sorted

    def create_list_all_matches(self, tournament_round: list) -> list:
        """
        Create a list of all matches of a tournament

        :param tournament_round: list
        :return: list_all_matches : list
        """
        list_all_matches = []

        for round in tournament_round:
            for match in round.matches_round:
                list_all_matches.append(match)
        return list_all_matches

    def create_list_all_actor(self, list_archive: List[Tournament]) -> list:
        """
        Create a list of all player of a tounament
        :param list_archive: list
        :return: list_all_actor: list
        """
        list_all_actor = []
        for tournament in list_archive:
            for player in tournament.players:
                list_all_actor.append(player)

        return list_all_actor

    def archive_tournament(self, new_tournament: Tournament):
        """
        Append a new tournament to the list_archive
        :param new_tournament: models.Tournament
        """
        list_archive.append(new_tournament)

    def list_name_tournaments(self, list_archive: List[Tournament]) -> list:
        """
        Create a list of name of all tournament
        :param list_archive: list
        :return: list_name_tournaments: list
        """
        list_name_tournaments = []
        for tournament in list_archive:
            list_name_tournaments.append(tournament.name)
        return list_name_tournaments