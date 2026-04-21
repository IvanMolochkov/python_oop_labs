import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from models import Pitcher, Defensive
from interfaces import Calculate, Printable
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

print()
print("Вызов интерфейсных методов")
print()
print("У класса Pitcher()")
print("to_string():")
print(player1.to_string())
print("calculate():")
print(player1.calculate())
print()
print("У класса Defensive()")
print("to_string():")
print(player2.to_string())
print("calculate():")
print(player2.calculate())



training = PlayerList()

training.add(player1)
training.add(player2)

def print_all(items: list[Printable]):
    for item in items:
        print(item.to_string())

def calculate_all(items: list[Calculate]):
    for item in items:
        print(item.calculate())

print()
print()
print()
print("Работа функции, работающей с разными объектами через интерфейс")
print()
print("print_all():")
print_all(training)
print()
print("calculate_all():")
calculate_all(training)

print()
print()
print()
print("Использование isinstance")
print()
print("интерфейс Printable:")
print(isinstance(player1, Printable))
print()
print("интерфейс Calculate:")
print(isinstance(player1, Calculate))
print()
print("Таким образом, объекты реализуют несколько интерфейсов")

print()
print()
print()
print("Фильтрация коллекции по интерфейсу")
print()
print("get_printable():")
print(training.get_printable())
print()
print("get_calculable():")
print(training.get_calculable())
print()
print("Сортировка через Calculate():")
print(training.sort_by_calculate())
print()