import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from model import Player
from collection import PlayerList


player1 = Player(
    name = "Aaron Judge",
    age = 33,
    team = "New York Yankees",
    batting_avg = 0.331,
    home_runs = 360,
    position = "RF"
)
player2 = Player(
    name = "Mike Trout",
    age = 32,
    team = "Los Angeles Angels",
    batting_avg = 0.302,
    home_runs = 368,
    position = "CF"
)
player3 = Player(
    name = "Rafael Devers",
    age = 29,
    team = "Boston Red Sox",
    batting_avg = 0.276,
    home_runs = 235,
    position = "3B"
)

fake_player = Player(
    name = "Aaron Judge",
    age = 23,
    team = "New York Yankees",
    batting_avg = 0.31,
    home_runs = 360,
    position = "RF"
)

print("\n")

playoff_player_list = PlayerList()


playoff_player_list.add(player1)
playoff_player_list.add(player2)
playoff_player_list.add(player3)

print("Вывод списка объектов игрока:")
print(playoff_player_list.get_all())
print("\n")

print("Все проверки при добавлении игрока в список:")
try:
    playoff_player_list.add({"name": "Saddam Husein"})
except TypeError as e:
    print(f"{type(e).__name__}: {e}")

try:
    playoff_player_list.add(player1)
except TypeError as e:
    print(f"{type(e).__name__}: {e}")
    
try:
    playoff_player_list.add(fake_player)
except TypeError as e:
    print(f"{type(e).__name__}: {e}")
print("\n")

print("Удаляем игрока Rafael Devers:")
playoff_player_list.remove(player3)
print(playoff_player_list.get_all())
print("\n")

print("Ошибка при удалении несуществующего игрока:")
playoff_player_list.remove(player3)
print("\n")

playoff_player_list.add(player3)

print("Находим игрока по имени:")
print(playoff_player_list.find_by_name("Aaron Judge"))
print("\n")

print("Выводим длину списка:")
print(len(playoff_player_list))
print("\n")

print("Итерация по списку(рядом с каждым объектом указал имя игрока):")
print([(e, e.name) for e in playoff_player_list])
print("\n")

print("Индексация по списку:")
print(playoff_player_list[0])
print(playoff_player_list[1])
print(playoff_player_list[2])
print("\n")

print("Ошибка при указании несуществующего индекса")
print(playoff_player_list[3])
print("\n")

print("Удаление игрока по индексу (1):")
playoff_player_list.remove_at(1)
print(playoff_player_list.get_all())
print("\n")

playoff_player_list.add(player2)

print("Сортировка по")
print("имени:")
playoff_player_list.sort_by_name()
print(playoff_player_list.get_all())
print("команде:")
playoff_player_list.sort_by_team()
print(playoff_player_list.get_all())
print("отбиваниям:")
playoff_player_list.sort_by_batting_avg()
print(playoff_player_list.get_all())
print("\n")

print("Собственная сортировка по тем свойствам, по которым выберет пользователь, с возможностью выбрать обратную сортировку")
print("Например, обратная сортировка по командам:")
playoff_player_list.sort("team", True)
print(playoff_player_list.get_all())
print("\n")

print("Логические операции, которые возвращают новый список по")
print("играющим игрокам(в этом сезоне все играют):")
print(playoff_player_list.get_active())
print("игрокам, по высокой оценке отбиваний:")
print(playoff_player_list.get_top())


# print(playoff_player_list.get_all())
# print(playoff_player_list[0])
# print(playoff_player_list[1])
# print(playoff_player_list[2])
# print(playoff_player_list.remove_at(1))

# print(playoff_player_list.get_active())
# print(playoff_player_list.get_top())