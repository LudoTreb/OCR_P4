from typing import List
from models import Player, Tournament, Round, Match


class SerializerController:

    def serialized_players(self, players: List[Player]) -> list:
        """
        serialize players
        :param players: players: list
        :return: serialized_players: list
        """
        serialized_players = []
        for player in players:
            serialized_player = {
                "last_name": player.last_name,
                "first_name": player.first_name,
                "birth_date": player.birth_date,
                "gender": player.gender,
                "rank": player.rank,
                "score": player.score,
            }
            serialized_players.append(serialized_player)

        return serialized_players

    def serialized_match_players(self, matches_player: list) -> list:
        """
        serialize match of player
        :param matches_player: list
        :return: serialized_matches_players: list
        """
        serialized_matches_players = []
        for match in matches_player:
            serialized_match_player = {
                "name_player": match[0].last_name,
                "score_player": match[1],
            }
            serialized_matches_players.append(serialized_match_player)
        return serialized_matches_players

    def serialized_match(self, matches: List[Match]) -> list:
        """
        serialize a list of matches
        :param matches: list
        :return: serialized_matches: list
        """
        serialized_matches = []
        for match in matches:
            serialized_match = {
                "match_number": match.name + 1,
                "players": self.serialized_match_players(match.players),
            }
            serialized_matches.append(serialized_match)
        return serialized_matches

    def serialized_round(self, rounds: List[Round]) -> list:
        """
        serialize a list of rounds
        :param rounds: list
        :return: serialized_rounds: list
        """
        serialized_rounds = []
        for round in rounds:
            serialized_round = {
                "round_number": round.name,

                "matches_round": self.serialized_match(round.matches_round),
            }
            serialized_rounds.append(serialized_round)
        return serialized_rounds

    def serialized_tournament(self, new_tournament: List[Tournament]) -> list:
        """
        serialize a list of tournaments
        :param new_tournament: list
        :return: serialized_tournament: list
        """
        serialized_tournament = {
            "name": new_tournament.name,
            "location": new_tournament.location,
            "date": new_tournament.date,
            "time_control": new_tournament.time_control,
            "number_round": new_tournament.number_round,
            "rounds": self.serialized_round(new_tournament.rounds),
            "players": self.serialized_players(new_tournament.players),
        }
        serialized_tournaments = [serialized_tournament]

        return serialized_tournaments


class DeserializerController:
    def instancing_serialized_player(self, serialized_players: List[dict]) -> list:
        """
        Instancing a list of serialized players
        :param serialized_players: list
        :return: instantiate_serialized_players: list
        """
        instantiate_serialized_players = []

        for player in serialized_players:
            last_name = player["last_name"]
            first_name = player["first_name"]
            birth_date = player["birth_date"]
            gender = player["gender"]
            rank = player["rank"]
            score = player["score"]

            player_convert = Player(
                last_name=last_name,
                first_name=first_name,
                birth_date=birth_date,
                gender=gender,
                rank=rank,
                score=score,
            )
            instantiate_serialized_players.append(player_convert)

        return instantiate_serialized_players

    def instancing_serialized_match_players(
            self, serialized_matches_player: List[dict]
    ) -> list:
        """
        Instancing a list of serialized match player

        :param serialized_matches_player: list
        :return: instantiate_serialized_matches_players: list
        """
        instantiate_serialized_matches_players = []

        for match in serialized_matches_player:
            name_player = match["name_player"]
            score_player = match["score_player"]

            match_player_convert = [name_player, score_player]

            instantiate_serialized_matches_players.append(match_player_convert)

        return instantiate_serialized_matches_players

    def instancing_serialized_match(self, serialized_matches: List[dict]) -> list:
        """
        Instancing a list of serialized matches
        :param serialized_matches: list
        :return: instantiate_serialized_matches: list
        """
        instantiate_serialized_matches = []

        for match in serialized_matches:
            match_number = (match["match_number"],)
            players = self.instancing_serialized_match_players(match["players"])

            match_convert = Match(name=match_number, players=players)

            instantiate_serialized_matches.append(match_convert)
        return instantiate_serialized_matches

    def instancing_serialized_round(self, serialized_rounds: List[dict]) -> list:
        """
        Instancing a list of serialized rounds
        :param serialized_rounds: list
        :return: instantiate_serialized_rounds: list
        """
        instantiate_serialized_rounds = []

        for round in serialized_rounds:
            round_number = (round["round_number"],)
            # date = round["date"],
            matches_round = self.instancing_serialized_match(round["matches_round"])

            round_convert = Round(
                name=round_number,
                date=None,
                matches_round=matches_round,
            )
            instantiate_serialized_rounds.append(round_convert)

        return instantiate_serialized_rounds

    def instancing_serialized_tournament(
            self, serialized_tournaments: List[dict]
    ) -> list:
        """
        Instancing a list of serialized tournaments
        :param serialized_tournaments: list
        :return: list
        """
        instantiate_serialized_tournaments = []

        for tournament in serialized_tournaments:
            name = tournament["name"]
            location = tournament["location"]
            date = tournament["date"]
            time_control = tournament["time_control"]
            number_round = tournament["number_round"]
            rounds = self.instancing_serialized_round(tournament["rounds"])
            players = self.instancing_serialized_player(tournament["players"])

            tournament_convert = Tournament(
                name=name,
                location=location,
                date=date,
                time_control=time_control,
                number_round=number_round,
            )
            tournament_convert.rounds = rounds
            tournament_convert.players = players

            instantiate_serialized_tournaments.append(tournament_convert)

        return instantiate_serialized_tournaments
