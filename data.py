import models
import datetime

# Tournament 1 archive

tournament_1 = models.Tournament(
    "Tournoi d'échec de St Brieux", "St Brieux", "22/06/2022", 4
)

player_1 = models.Player("Blot", "Denis", "24 juin 1998", "h", 3560, 1)
player_2 = models.Player("Vallet", "Virginie", "02 janvier 2003", "f", 4300, 4)
player_3 = models.Player("Coulon", "Maurice", "16 avril 2001", "h", 2030, 0)
player_4 = models.Player("Caron", "Pauline", "03 juin 2000", "f", 3700, 3)
player_5 = models.Player("Carpentier", "Yves", "21 octobre 2000", "h", 3560, 3)
player_6 = models.Player("Dubois", "Madeleine", "12 septembre 1999", "f", 3230, 0)
player_7 = models.Player("Bertin", "Astrid", "24 décembre 1998", "f", 3750, 3)
player_8 = models.Player("Martel", "Patricia", "29 mai 2001", "f", 3560, 2)

list_players = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
]
tournament_1.list_players = list_players

# Round 1
match_1 = models.Match(0, [player_2, player_5])
match_2 = models.Match(1, [player_7, player_8])
match_3 = models.Match(2, [player_4, player_6])
match_4 = models.Match(3, [player_1, player_3])

matches_round_1 = [match_1, match_2, match_3, match_4]
round_1 = models.Round(1, "22/06/2022", matches_round_1)

# Round 2
match_5 = models.Match(0, [player_2, player_7])
match_6 = models.Match(1, [player_4, player_1])
match_7 = models.Match(2, [player_8, player_6])
match_8 = models.Match(3, [player_5, player_3])

matches_round_2 = [match_5, match_6, match_7, match_8]
round_2 = models.Round(2, "22/06/2022", matches_round_2)

# Round 3
match_9 = models.Match(0, [player_2, player_4])
match_10 = models.Match(1, [player_8, player_1])
match_11 = models.Match(2, [player_5, player_6])
match_12 = models.Match(3, [player_7, player_3])

matches_round_3 = [match_9, match_10, match_11, match_12]
round_3 = models.Round(3, "22/06/2022", matches_round_3)

# Round 4
match_13 = models.Match(0, [player_2, player_8])
match_14 = models.Match(1, [player_5, player_1])
match_15 = models.Match(2, [player_7, player_6])
match_16 = models.Match(3, [player_4, player_3])

matches_round_4 = [match_13, match_14, match_15, match_16]
round_4 = models.Round(4, "22/06/2022", matches_round_4)

list_round = [round_1, round_2, round_3, round_4]
tournament_1.rounds = list_round

# Autre tounoi mais juste l'instance de tounoi, pas de joueur ou autre

# Tournoi 2
tournament_2 = models.Tournament(
    "20th Rochefort Chess Festival - Masters", "Rochefort", "12/08/2022", 4
)

player_1 = models.Player("Huet", "Adèle", "24 juin 1998", "f", 3560, 1)
player_2 = models.Player("Morin", "Gilles", "02 janvier 2003", "h", 4300, 4)
player_3 = models.Player("Bazin", "Alfred", "16 avril 2001", "h", 2030, 0)
player_4 = models.Player("Vasseur", "Aurore", "03 juin 2000", "f", 3700, 3)
player_5 = models.Player("Letellier", "Gérard", "21 octobre 2000", "h", 3555, 3)
player_6 = models.Player("Chretien", "Élise", "12 septembre 1999", "f", 3230, 0)
player_7 = models.Player("Diaz", "Juliette", "24 décembre 1998", "f", 3780, 3)
player_8 = models.Player("Bouvet", "Alex", "29 mai 2001", "h", 3550, 2)

list_players_2 = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
]
tournament_2.list_players = list_players_2

# Round 1
match_1 = models.Match(0, [player_2, player_5])
match_2 = models.Match(1, [player_7, player_8])
match_3 = models.Match(2, [player_4, player_6])
match_4 = models.Match(3, [player_1, player_3])

matches_round_1 = [match_1, match_2, match_3, match_4]
round_1 = models.Round(1, "212/08/2022", matches_round_1)

# Round 2
match_5 = models.Match(0, [player_2, player_7])
match_6 = models.Match(1, [player_4, player_1])
match_7 = models.Match(2, [player_8, player_6])
match_8 = models.Match(3, [player_5, player_3])

matches_round_2 = [match_5, match_6, match_7, match_8]
round_2 = models.Round(2, "12/08/2022", matches_round_2)

# Round 3
match_9 = models.Match(0, [player_2, player_4])
match_10 = models.Match(1, [player_8, player_1])
match_11 = models.Match(2, [player_5, player_6])
match_12 = models.Match(3, [player_7, player_3])

matches_round_3 = [match_9, match_10, match_11, match_12]
round_3 = models.Round(3, "12/08/2022", matches_round_3)

# Round 4
match_13 = models.Match(0, [player_2, player_8])
match_14 = models.Match(1, [player_5, player_1])
match_15 = models.Match(2, [player_7, player_6])
match_16 = models.Match(3, [player_4, player_3])

matches_round_4 = [match_13, match_14, match_15, match_16]
round_4 = models.Round(4, "12/08/2022", matches_round_4)

list_round_2 = [round_1, round_2, round_3, round_4]
tournament_2.rounds = list_round_2



# Tournoi 3
tournament_3 = models.Tournament(
    "5ème Open Fide de Lavérune", "Lavérune", "24/03/2022", 4
)

player_1 = models.Player("Laine", "Joséphine", "24 juin 1998", "f", 3570, 1)
player_2 = models.Player("Martel", "Éric", "02 janvier 2003", "h", 4310, 4)
player_3 = models.Player("Morvan", "Nicolas", "16 avril 2001", "h", 2030, 0)
player_4 = models.Player("Lambert", "Jeanne", "03 juin 2000", "f", 3700, 3)
player_5 = models.Player("Joly", "André", "21 octobre 2000", "h", 3560, 3)
player_6 = models.Player("Grenier", "Suzanne", "12 septembre 1999", "f", 3230, 0)
player_7 = models.Player("Diaz", "Juliette", "24 décembre 1998", "f", 3790, 3)
player_8 = models.Player("Colin", "Auguste", "29 mai 2001", "h", 3530, 2)

list_players_3 = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
]
tournament_3.list_players = list_players_3


# Round 1
match_1 = models.Match(0, [player_2, player_5])
match_2 = models.Match(1, [player_7, player_8])
match_3 = models.Match(2, [player_4, player_6])
match_4 = models.Match(3, [player_1, player_3])

matches_round_1 = [match_1, match_2, match_3, match_4]
round_1 = models.Round(1, "24/03/2022", matches_round_1)

# Round 2
match_5 = models.Match(0, [player_2, player_7])
match_6 = models.Match(1, [player_4, player_1])
match_7 = models.Match(2, [player_8, player_6])
match_8 = models.Match(3, [player_5, player_3])

matches_round_2 = [match_5, match_6, match_7, match_8]
round_2 = models.Round(2, "24/03/2022", matches_round_2)

# Round 3
match_9 = models.Match(0, [player_2, player_4])
match_10 = models.Match(1, [player_8, player_1])
match_11 = models.Match(2, [player_5, player_6])
match_12 = models.Match(3, [player_7, player_3])

matches_round_3 = [match_9, match_10, match_11, match_12]
round_3 = models.Round(3, "24/03/2022", matches_round_3)

# Round 4
match_13 = models.Match(0, [player_2, player_8])
match_14 = models.Match(1, [player_5, player_1])
match_15 = models.Match(2, [player_7, player_6])
match_16 = models.Match(3, [player_4, player_3])

matches_round_4 = [match_13, match_14, match_15, match_16]
round_4 = models.Round(4, "24/03/2022", matches_round_4)

list_round_3 = [round_1, round_2, round_3, round_4]
tournament_3.rounds = list_round_3


list_archive = [tournament_1, tournament_2, tournament_3]


def sort_date(list_tournaments : list) -> list:
    list_tournaments_date_sorted = sorted(
        list_tournaments,
        key=lambda tournament: datetime.datetime.strptime(tournament.date, "%d/%m/%Y"),
        reverse=True,
    )
    return list_tournaments_date_sorted


print(sort_date(list_archive))

print(type(tournament_3.rounds))