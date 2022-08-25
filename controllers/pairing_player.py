from typing import List

from controllers.pairing_tools import PairingTools
from models import Player

pairing_tools = PairingTools()


class PairingPlayerController:
    @staticmethod
    def pairing_player_round_1(players: List[Player]) -> list:
        """
        Sort the list of players_1 in descending order by their rank
        split this list into two list in half
        associate the player one of the first list with
        the player one of the second list...
        Get a list, with a pair of player in tuple.

        :param players: list
        :return:list_pairs: list
        """
        players_sorted = pairing_tools.sort_descending_rank(players)
        list_1, list_2 = pairing_tools.split_list_player_round_1(players_sorted)
        list_pairs = []
        for i in range(len(players) // 2):
            player_1 = list_1[i]
            player_2 = list_2[i]
            pair_player = (player_1, player_2)

            # remove the player just added from his potential_opponent list
            player_1.potential_opponent.remove(player_2)
            player_2.potential_opponent.remove(player_1)

            list_pairs.append(pair_player)

        return list_pairs

    @staticmethod
    def pairing_player(players: List[Player]) -> list:
        """
        Sort the list of players_1 in descending order by their rank
        Sort the list of players_1 in descending order by their score

        associate the first player of the list with the second player.
        If this pair already exists, the first player is associate to the third player...
        until a new pair is created.
        Get a list, with a pair of player in tuple.

        :param players: list
        :return: list_pairs: list
        """
        list_pairs = []

        list_sorted_rank = pairing_tools.sort_descending_rank(players)
        list_sorted = pairing_tools.sort_descending_score(list_sorted_rank)

        for i, current_player in enumerate(list_sorted):
            list_next_player = list_sorted[i + 1: len(list_sorted)]

            for next_player in list_next_player:
                if next_player in current_player.potential_opponent:
                    pair_player = (current_player, next_player)
                    list_sorted.remove(next_player)
                    list_pairs.append(pair_player)

                    # remove the player just added from his potential_opponent list
                    current_player.potential_opponent.remove(next_player)
                    next_player.potential_opponent.remove(current_player)

                    break

                else:
                    continue

        return list_pairs
