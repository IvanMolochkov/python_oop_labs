import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.lab03.base import Player as Player
from src.lab03.models import Pitcher, Defensive
from collection import PlayerList


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

player3 = Defensive(
    name = "Jeremy Pena",
    age = 29,
    team = "Houston Astros",
    batting_avg = 0.195,
    home_runs = 87,
    PO = 927,
    A = 41,
    DP = 9,
    position = "SS"
)

playoff_player_list = PlayerList()
playoff_player_list.add(player1)
playoff_player_list.add(player2)
playoff_player_list.add(player3)

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
print()

print("Собственная сортировка по тем свойствам, по которым выберет пользователь, с возможностью выбрать обратную сортировку")
print("Например, обратная сортировка по командам:")
playoff_player_list.sort("team", True)
print(playoff_player_list.get_all())
print()

print("Фильтр по")
print("играющим игрокам(в этом сезоне все играют):")
print(playoff_player_list.get_active())
print("игрокам, по высокой оценке отбиваний:")
print(playoff_player_list.get_top())
print()

print("Мапинг:")
print("по имени:")
print(playoff_player_list.get_only_name())
print("по полному названию position:")
print(playoff_player_list.get_full_position())
print("преобразует в string:")
print(playoff_player_list.map_to_strings())
print()


print("sort_by() с функцией-стратегией")
by_name = lambda p: p.name
by_age = lambda p: p.age
by_home_runs = lambda p: p.home_runs
print("По имени:")
for p in playoff_player_list.sort_by(by_name):
    print(f"{p.name}")
print("По возрасту:")
for p in playoff_player_list.sort_by(by_age):
    print(f"{p.name}: {p.age}")
print("По хоум-ранам (reverse):")
for p in playoff_player_list.sort_by(by_home_runs, reverse=True):
    print(f"{p.name}: {p.home_runs}")
print()


print("filter_by() и фабрики функций")
print("Только питчеры:")
for p in playoff_player_list.filter_by(lambda e: isinstance(e, Pitcher)):
    print(f"{p.name}")
print()
print("Только активные игроки:")
for p in playoff_player_list.filter_by(lambda e: e.status == "yes"):
    print(f"{p.name}: {p.status}")
print()
print("Фабрика make_batting_filter(0.280) - batting avg >= 0.280:")
high_avg = PlayerList.make_batting_filter(0.280)
for p in playoff_player_list.filter_by(high_avg):
    print(f"  {p.name}: {p.batting_avg:.3f}")
print()
print("Фабрика make_home_run_filter(100) — HR >= 100:")
hr_filter = PlayerList.make_home_run_filter(100)
for p in playoff_player_list.filter_by(hr_filter):
    print(f"{p.name}: {p.home_runs} HR")
print()
print("Сравнение: lambda vs фабрика (одинаковый результат):")
via_lambda = playoff_player_list.filter_by(lambda p: p.batting_avg >= 0.280)
via_factory = playoff_player_list.filter_by(PlayerList.make_batting_filter(0.280))
print(f"lambda: {[p.name for p in via_lambda]}")
print(f"фабрика: {[p.name for p in via_factory]}")
print()


print("Цепочка filter_by, sort_by, apply")
def add_home_run(player):
    try:
        player.hit_home_run()
    except RuntimeError as e:
        return f"{e.__name__}: {e}"
    return player
print("filter_by (только активные):")
step1 = playoff_player_list.filter_by(lambda e: e.status == "yes")
print([p.name for p in step1])
print()
print("sort_by batting_avg (reverse):")
step2 = step1.sort_by(lambda p: p.batting_avg, reverse=True)
for p in step2:
    print(f"  {p.name}: {p.batting_avg:.3f}")
print()
print("apply (добавить хоум-ран каждому):")
print("HR до:", [p.home_runs for p in step2])
step3 = step2.apply(add_home_run)
print("HR после:", [p.home_runs for p in step3])
print()
print("Вся цепочка в одну строку:")
result = (playoff_player_list
    .filter_by(lambda e: e.status == "yes")
    .sort_by(lambda p: p.home_runs, reverse=True)
    .apply(add_home_run))
for p in result:
    print(f"{p.name}: {p.batting_avg:.3f}, {p.home_runs} HR")