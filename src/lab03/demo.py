import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from models import Pitcher, Defensive
from src.lab02.collection import PlayerList

player1 = Pitcher(
    name = "Gerrit Cole",
    age = 33,
    team = "New York Yankees",
    batting_avg = 0.280,
    home_runs = 11,
    ERA = 2.17,
    WHIP = 1.28,
    K_9 = 22,
    position = "P"
)

player2 = Defensive(
    name = "Aaron Judge",
    age = 33,
    team = "New York Yankees",
    batting_avg = 0.331,
    home_runs = 360,
    PO = 1346,
    A = 39,
    DP = 8,
    position = "RF"
)






playoff_player_list = PlayerList()
playoff_player_list.add(player1)
playoff_player_list.add(player2)

print()
print("единый список объектов разных типов:")
print(playoff_player_list.get_all())
print()

print("вызов одинакового метода для разных типов и получение разных результатов")
print("calculate() для Pitcher:")
print(f"{player1.calculate()}, total chances")
print("calculate() для Defensive:")
print(f"{player2.calculate()}, sum stats")
print()

print("фильтрация по типу")
print("только Pitcher:")
print(playoff_player_list.get_only_pitchers())
print("только Defensive:")
print(playoff_player_list.get_only_defensive())
print()

print("сценарии использования:")
print()

print("использование методов")
print("оценка по ERA для Pitcher:")
print(player1.ERA_grade())
print("оценка по зашите для Defensive:")
print(player2.defensive_rating())
print()

print("геттеры")
print("WHIP для Pitcher:")
print(player1.WHIP)
print("PO для Defensive:")
print(player2.PO)
print()

print("сеттеры")
print("K/9 для Pitcher:")
print("Было:")
print(player1)
player1.K_9 = 27
print("Стало:")
print(player1)
print("DP для Defensive:")
print("Было:")
print(player2)
player2.DP = 12
print("Стало:")
print(player2)
print()