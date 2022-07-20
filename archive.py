""" Data base of tournament """

from models import Player, Tournament, Round, Match


# Tournament 1 archive

tournament_1 = Tournament("Master des Alpes de Haute Provence", "Digne les bains", "05/03/2022", 4)

player_1 = Player("Blot", "Denis", "24 juin 1998", "h", 3560, 1)
player_2 = Player("Vallet", "Virginie", "02 janvier 2003", "f", 4300, 4)
player_3 = Player("Coulon", "Maurice", "16 avril 2001", "h", 2030, 0)
player_4 = Player("Caron", "Pauline", "03 juin 2000", "f", 3700, 3)
player_5 = Player("Carpentier", "Yves", "21 octobre 2000", "h", 3560, 2.5)
player_6 = Player("Dubois", "Madeleine", "12 septembre 1999", "f", 3230, 0.5)
player_7 = Player("Bertin", "Astrid", "24 décembre 1998", "f", 3750, 3)
player_8 = Player("Martel", "Patricia", "29 mai 2001", "f", 3560, 2)

players = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
]
tournament_1.players = players

# Round 1
match_1 = Match(0, [player_2, player_5])
match_1.players = [[player_2, 1], [player_5, 0]]
match_2 = Match(1, [player_7, player_8])
match_2.players = [[player_7, 1], [player_8, 0]]
match_3 = Match(2, [player_4, player_6])
match_3.players = [[player_4, 1], [player_6, 0]]
match_4 = Match(3, [player_1, player_3])
match_4.players = [[player_1, 1], [player_3, 0]]

matches_round_1 = [match_1, match_2, match_3, match_4]
round_1 = Round(1, "22/06/2022", matches_round_1)

# Round 2
match_5 = Match(0, [player_2, player_7])
match_5.players = [[player_2, 1], [player_7, 0]]
match_6 = Match(1, [player_4, player_1])
match_6.players = [[player_4, 1], [player_1, 0]]
match_7 = Match(2, [player_8, player_6])
match_7.players = [[player_8, 1], [player_6, 0]]
match_8 = Match(3, [player_5, player_3])
match_8.players = [[player_5, 1], [player_3, 0]]

matches_round_2 = [match_5, match_6, match_7, match_8]
round_2 = Round(2, "22/06/2022", matches_round_2)

# Round 3
match_9 = Match(0, [player_2, player_4])
match_9.players = [[player_2, 1], [player_4, 0]]
match_10 = Match(1, [player_8, player_1])
match_10.players = [[player_8, 1], [player_1, 0]]
match_11 = Match(2, [player_5, player_6])
match_11.players = [[player_5, 0.5], [player_6, 0.5]]
match_12 = Match(3, [player_7, player_3])
match_12.players = [[player_7, 1], [player_3, 0]]

matches_round_3 = [match_9, match_10, match_11, match_12]
round_3 = Round(3, "22/06/2022", matches_round_3)

# Round 4
match_13 = Match(0, [player_2, player_8])
match_13.players = [[player_2, 1], [player_8, 0]]
match_14 = Match(1, [player_5, player_1])
match_14.players = [[player_5, 1], [player_1, 0]]
match_15 = Match(2, [player_7, player_6])
match_15.players = [[player_7, 1], [player_6, 0]]
match_16 = Match(3, [player_4, player_3])
match_16.players = [[player_4, 1], [player_3, 0]]

matches_round_4 = [match_13, match_14, match_15, match_16]
round_4 = Round(4, "22/06/2022", matches_round_4)

list_round = [round_1, round_2, round_3, round_4]
tournament_1.rounds = list_round



# Tournament 2 archive
tournament_2 = Tournament(
    "20th Rochefort Chess Festival - Masters", "Rochefort", "12/08/2022", 4
)

player_1 = Player("Huet", "Adèle", "24 juin 1998", "f", 3560, 1)
player_2 = Player("Morin", "Gilles", "02 janvier 2003", "h", 4300, 4)
player_3 = Player("Bazin", "Alfred", "16 avril 2001", "h", 2030, 0.5)
player_4 = Player("Vasseur", "Aurore", "03 juin 2000", "f", 3700, 3)
player_5 = Player("Letellier", "Gérard", "21 octobre 2000", "h", 3555, 3)
player_6 = Player("Chretien", "Élise", "12 septembre 1999", "f", 3230, 0)
player_7 = Player("Diaz", "Juliette", "24 décembre 1998", "f", 3780, 2.5)
player_8 = Player("Bouvet", "Alex", "29 mai 2001", "h", 3550, 2)

players_2 = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
]
tournament_2.players = players_2

# Round 1
match_1 = Match(0, [player_2, player_5])
match_1.players = [[player_2, 1], [player_5, 0]]
match_2 = Match(1, [player_7, player_8])
match_2.players = [[player_7, 1], [player_8, 0]]
match_3 = Match(2, [player_4, player_6])
match_3.players = [[player_4, 1], [player_6, 0]]
match_4 = Match(3, [player_1, player_3])
match_4.players = [[player_1, 1], [player_3, 0]]

matches_round_1 = [match_1, match_2, match_3, match_4]
round_1 = Round(1, "212/08/2022", matches_round_1)

# Round 2
match_5 = Match(0, [player_2, player_7])
match_5.players = [[player_2, 1], [player_7, 0]]
match_6 = Match(1, [player_4, player_1])
match_6.players = [[player_4, 1], [player_1, 0]]
match_7 = Match(2, [player_8, player_6])
match_7.players = [[player_8, 1], [player_6, 0]]
match_8 = Match(3, [player_5, player_3])
match_8.players = [[player_5, 1], [player_3, 0]]

matches_round_2 = [match_5, match_6, match_7, match_8]
round_2 = Round(2, "12/08/2022", matches_round_2)

# Round 3
match_9 = Match(0, [player_2, player_4])
match_9.players = [[player_2, 1], [player_4, 0]]
match_10 = Match(1, [player_8, player_1])
match_10.players = [[player_8, 1], [player_1, 0]]
match_11 = Match(2, [player_5, player_6])
match_11.players = [[player_5, 1], [player_6, 0]]
match_12 = Match(3, [player_7, player_3])
match_12.players = [[player_7, 0.5], [player_3, 0.5]]

matches_round_3 = [match_9, match_10, match_11, match_12]
round_3 = Round(3, "12/08/2022", matches_round_3)

# Round 4
match_13 = Match(0, [player_2, player_8])
match_13.players = [[player_2, 1], [player_8, 0]]
match_14 = Match(1, [player_5, player_1])
match_14.players = [[player_5, 1], [player_1, 0]]
match_15 = Match(2, [player_7, player_6])
match_15.players = [[player_7, 1], [player_6, 0]]
match_16 = Match(3, [player_4, player_3])
match_16.players = [[player_4, 1], [player_3, 0]]

matches_round_4 = [match_13, match_14, match_15, match_16]
round_4 = Round(4, "12/08/2022", matches_round_4)

list_round_2 = [round_1, round_2, round_3, round_4]
tournament_2.rounds = list_round_2

# Tournament 3 archive
tournament_3 = Tournament("5ème Open Fide de Lavérune", "Lavérune", "24/03/2022", 4)

player_1 = Player("Laine", "Joséphine", "24 juin 1998", "f", 3570, 1)
player_2 = Player("Martel", "Éric", "02 janvier 2003", "h", 4310, 4)
player_3 = Player("Morvan", "Nicolas", "16 avril 2001", "h", 2030, 0.5)
player_4 = Player("Lambert", "Jeanne", "03 juin 2000", "f", 3700, 3)
player_5 = Player("Joly", "André", "21 octobre 2000", "h", 3560, 3)
player_6 = Player("Grenier", "Suzanne", "12 septembre 1999", "f", 3230, 0)
player_7 = Player("Diaz", "Juliette", "24 décembre 1998", "f", 3790, 2.5)
player_8 = Player("Colin", "Auguste", "29 mai 2001", "h", 3530, 2)

players_3 = [
    player_1,
    player_2,
    player_3,
    player_4,
    player_5,
    player_6,
    player_7,
    player_8,
]
tournament_3.players = players_3

# Round 1
match_1 = Match(0, [player_2, player_5])
match_1.players = [[player_2, 1], [player_5, 0]]
match_2 = Match(1, [player_7, player_8])
match_2.players = [[player_7, 1], [player_8, 0]]
match_3 = Match(2, [player_4, player_6])
match_3.players = [[player_4, 1], [player_6, 0]]
match_4 = Match(3, [player_1, player_3])
match_4.players = [[player_1, 1], [player_3, 0]]

matches_round_1 = [match_1, match_2, match_3, match_4]
round_1 = Round(1, "24/03/2022", matches_round_1)

# Round 2
match_5 = Match(0, [player_2, player_7])
match_5.players = [[player_2, 1], [player_7, 0]]
match_6 = Match(1, [player_4, player_1])
match_6.players = [[player_4, 1], [player_1, 0]]
match_7 = Match(2, [player_8, player_6])
match_7.players = [[player_8, 1], [player_6, 0]]
match_8 = Match(3, [player_5, player_3])
match_8.players = [[player_5, 1], [player_3, 0]]

matches_round_2 = [match_5, match_6, match_7, match_8]
round_2 = Round(2, "24/03/2022", matches_round_2)

# Round 3
match_9 = Match(0, [player_2, player_4])
match_9.players = [[player_2, 1], [player_8, 0]]
match_10 = Match(1, [player_8, player_1])
match_10.players = [[player_8, 0], [player_1, 1]]
match_11 = Match(2, [player_5, player_6])
match_11.players = [[player_5, 1], [player_6, 0]]
match_12 = Match(3, [player_7, player_3])
match_12.players = [[player_7, 0.5], [player_3, 0.5]]

matches_round_3 = [match_9, match_10, match_11, match_12]
round_3 = Round(3, "24/03/2022", matches_round_3)

# Round 4
match_13 = Match(0, [player_2, player_8])
match_13.players = [[player_2, 1], [player_8, 0]]
match_14 = Match(1, [player_5, player_1])
match_14.players = [[player_5, 1], [player_1, 0]]
match_15 = Match(2, [player_7, player_6])
match_15.players = [[player_7, 1], [player_6, 0]]
match_16 = Match(3, [player_4, player_3])
match_16.players = [[player_4, 1], [player_3, 0]]

matches_round_4 = [match_13, match_14, match_15, match_16]
round_4 = Round(4, "24/03/2022", matches_round_4)

list_round_3 = [round_1, round_2, round_3, round_4]
tournament_3.rounds = list_round_3

# Archive
list_archive = [tournament_1, tournament_2, tournament_3]
