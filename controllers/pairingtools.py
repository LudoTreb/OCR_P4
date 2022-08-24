from typing import List

from models import Player


class PairingTools:
    def sort_descending_rank(self, players: List[Player]) -> list:
        """
        Get a list of players_1 sorted by their rank in a descending order

        :param players: list
        :return: players_rank_sorted: list
        """
        players_rank_sorted = sorted(
            players, key=lambda player: player.rank, reverse=True
        )
        return players_rank_sorted

    def split_list_player_round_1(self, players: List[Player]) -> tuple[list, list]:
        """
        Split in half a list of player into two list.
        This is for the first round of the tournament.

        :param players: list
        :return: first_half_players, second_half_players: tuple[list, list]
        """
        length = len(players)
        middle_index = length // 2
        first_half_players = players[:middle_index]
        second_half_players = players[middle_index:]
        return (
            first_half_players,
            second_half_players,
        )

    def sort_descending_score(self, players: List[Player]) -> list:
        """
        Get a list of players_1 sorted by their score in a descending order

        :param players: list
        :return: players_score_sorted: list
        """
        players_score_sorted = sorted(
            players, key=lambda player: player.score, reverse=True
        )

        return players_score_sorted

    def split_list_player_other_round(self, players: List[Player]) -> tuple[list, list]:
        """
        Split in half a list of player into two list.
        This is for other rounds of the tournament.

        :param players: list
        :return: list_first_player, list_second_player: tuple[list, list]
        """
        list_first_player = []
        list_second_player = []
        for i in range(0, len(players), 2):
            list_first_player.append(players[i])

        for i in range(1, len(players), 2):
            list_second_player.append(players[i])

        return list_first_player, list_second_player
