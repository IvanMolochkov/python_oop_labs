import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
 
from model import Player

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

print("-" * 90)
print("getters:")
print(player1)
print(player2)
print(player3)

print("-" * 90)
print("reprs:")
print(repr(player1))
print(repr(player2))
print(repr(player3))
 
bad_cases = [
    dict(name="", age=25, team="Yankees", batting_avg=0.280, home_runs=10, position="1B"),
    dict(name="John", age=10, team="Yankees", batting_avg=0.280, home_runs=10, position="1B"),
    dict(name="John", age=25, team="Yankees", batting_avg=1.50, home_runs=10, position="1B"),
    dict(name="John", age=25, team="Yankees", batting_avg=0.280, home_runs=-5, position="1B"),
    dict(name="John", age=25, team="Yankees", batting_avg=0.280, home_runs=10, position="GOAT"),
    dict(name="John", age=25, team="", batting_avg=0.280, home_runs=10, position="1B"),
]
print("-" * 90)
print("bad cases:")
for e in bad_cases:
    try:
        p = Player(**e)
    except (TypeError, ValueError) as el:
        print(f"{type(el).__name__}: {el}")
 
 
print("-" * 90)
print("изменение параметров игрока:")
print(f"до: BA={player2.batting_avg:.3f}  HR={player2.home_runs}  age={player2.age}")
player2.batting_avg = 0.310
player2.home_runs = 180
player2.age = 31
print(f"после: BA={player2.batting_avg:.3f}  HR={player2.home_runs}  age={player2.age}")
 
print("-" * 90)
print("подмена игрока Mike Trout:")
print(f"до: {player2._team}")
player2.team_change("New York Yankees")
print(f"после: {player2._team}")

print("-" * 90)
print("попытка поменять на эту же команду:")
try:
    player2.team_change("New York Yankees")
except RuntimeError as e:
    print(f"RuntimeError: {e}")
 
print("-" * 90)
print("травмируем игрока Rafael Devers):")
print(f"до: {player3._is_playing}")
player3.injure()
print(f"после: {player3._is_playing}")
 
print("-" * 90)
print("попытка травмировать травмированного:")
try:
    player3.injure()
except RuntimeError as e:
    print(f"RuntimeError: {e}")

print("-" * 90)
print("восстанавливаем игрока:")
player3.recover()
print(f"{player3._is_playing}")
 
print("-" * 90)
print("выход на пенсию")
player3.retire()
print(f"{player3._is_playing}")
 
print("-" * 90)
print("попытка выйти на пенсию дважды")
try:
    player3.retire()
except RuntimeError as e:
    print(f"RuntimeError: {e}")
 
print("-" * 90)
print("механика хоумранов:")
print(f"Aaron Judge is playing: {player1._is_playing}, HR before: {player1.home_runs}")
player1.hit_home_run()
print(f"hit a home run, HR after : {player1.home_runs}")
print("-" * 90)
print("может ли неиграющий и игрок забить хоумран:")
player1.injure()
print(f"Aaron Judge is playing: {player1._is_playing}")
try:
    player1.hit_home_run()
except RuntimeError as e:
    print(f"RuntimeError: {e}")
player1.recover()

print("-" * 90)
print("оценка статистики:")
print(f"{player1.name} BA={player1.batting_avg:.3f} оценка: {player1.performance_grade()}")

print("-" * 90)
print(f"всего игроков: {Player.total_players()}")
print("-" * 90)
