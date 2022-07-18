class Player:
    potential_opponent = []

    def __init__(self, last_name, first_name, birth_date, gender, rank, score=0):
        """
        Initialise un joueur
        :param last_name:
        :param first_name:
        :param birth_date:
        :param gender:
        :param rank:
        """

        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        self.score = score

    def __repr__(self):
        return str(self.last_name)

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def played_with(self, player):  # pas utile mais à voir
        pass

    def add_potential_opponents(self, list_player):
        list_copy = list_player.copy()
        list_copy.remove(self)
        self.potential_opponent = list_copy


class Tournament:
    rounds = []
    list_players = []

    def __init__(self, name, location, date, time_control, number_round=4):
        """
        Initialise le nom, le lieu, la date du tournoi
        l'attribut "number_round" par défaut est 4
        :param name:
        :param location:
        :param date:
        :param number_round:
        """
        self.name = name
        self.location = location
        self.date = date
        self.time_control = time_control
        self.number_round = number_round

    def description_tournament(self):
        """
        Affiche la description du tournoi
        :return:
        """
        pass

    def historic_tournament(self):
        """
        Affiche l'historique du tournoi en cours
        :return:
        """
        pass


class Match:
    def __init__(self, name, list_players):
        """
        Initialise le nom du match
        :param name:
        """
        self.name = name
        self.players = [[i, 0] for i in list_players]

    def __repr__(self):
        return str(self.players)


class Round:
    end_time = None

    def __init__(self, name, date, matches_round, status="ongoing"):
        """
        Initialise le nom, la date, l'heure de fin, l'état
        :param name:
        :param date:
        :param status:
        """
        self.name = name
        self.date = date
        self.matches_round = matches_round
        self.status = status

    def __repr__(self):
        return str(self.matches_round)
