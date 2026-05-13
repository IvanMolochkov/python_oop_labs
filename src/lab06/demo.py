import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.lab03.models import Pitcher, Defensive
from container import TypedCollection, Displayable, Scorable

def pitcher_display(self) -> str:
    return f"Питчер {self._name} | Команда: {self._team} | ERA: {self._ERA} | WHIP: {self._WHIP} | K/9: {self._K_9}"

def pitcher_score(self) -> float:
    return round((self._ERA + self._WHIP + self._K_9) / 3, 2)

def defensive_display(self) -> str:
    return f"{self._position} {self._name} | Команда: {self._team} | PO: {self._PO} | A: {self._A} | DP: {self._DP}"

def defensive_score(self) -> float:
    return float(self._PO + self._A)

Pitcher.display = pitcher_display
Pitcher.score = pitcher_score
Defensive.display = defensive_display
Defensive.score = defensive_score

player1 = Pitcher(
    name="Gerrit Cole", age=33, team="New York Yankees",
    batting_avg=0.280, home_runs=11,
    ERA=2.17, WHIP=1.28, K_9=22, position="P"
)
player2 = Pitcher(
    name="Shohei Ohtani", age=30, team="Los Angeles Dodgers",
    batting_avg=0.304, home_runs=44,
    ERA=3.14, WHIP=1.06, K_9=11, position="P"
)
player3 = Defensive(
    name="Aaron Judge", age=33, team="New York Yankees",
    batting_avg=0.331, home_runs=62,
    PO=1346, A=39, DP=8, position="RF"
)
player4 = Defensive(
    name="Mookie Betts", age=31, team="Los Angeles Dodgers",
    batting_avg=0.307, home_runs=39,
    PO=280, A=10, DP=2, position="RF"
)

print()
print("Базовая демонстрация TypedCollection")
print()

collection: TypedCollection[Pitcher] = TypedCollection()
collection.add(player1)
collection.add(player2)

print("Все элементы:")
for p in collection.get_all():
    print(f"{p}")
print()

print(f"Длина коллекции: {len(collection)}")
print(f"Элемент по индексу [0]: {collection[0]._name}")
print()

print("Попытка добавить дубликат:")
try:
    collection.add(player1)
except TypeError as e:
    print(f"TypeError: {e}")

print()
print("find(), filter(), map()")
print()

mixed: TypedCollection = TypedCollection()
for p in [player1, player2, player3, player4]:
    mixed.add(p)

print("find() — найден:")
found = mixed.find(lambda p: p._name == "Aaron Judge")
print(f"{found._name if found else None}")
print()

print("find() — не найден:")
not_found = mixed.find(lambda p: p._name == "Mike Trout")
print(f"{not_found}")
print()

print("filter() — только ERA < 3.0 (питчеры):")
result = mixed.filter(lambda p: isinstance(p, Pitcher) and p._ERA < 3.0)
for p in result:
    print(f"{p._name}: ERA {p._ERA}")
print()

print("map() — извлечение имён (list[str]):")
names: list[str] = mixed.map(lambda p: p._name)
print(f"{names}")
print()

print("map() — извлечение batting avg (list[float]):")
avgs: list[float] = mixed.map(lambda p: p._batting_avg)
print(f"{avgs}")
print()

print("map() — строковое представление (list[str]):")
strings: list[str] = mixed.map(lambda p: str(p))
for s in strings:
    print(f"{s}")

print()
print("TypedCollection[D] через Protocol Displayable")
print()

displayable: TypedCollection[Displayable] = TypedCollection()
displayable.add(player1)
displayable.add(player2)
displayable.add(player3)
displayable.add(player4)

print("Вызов display() для каждого объекта:")
for p in displayable:
    print(f"{p.display()}")
print()

print("map() через display() — list[str]:")
displays: list[str] = displayable.map(lambda p: p.display())
for d in displays:
    print(f"{d}")
print()

print("find() — первый у кого 'Yankees' в display():")
found = displayable.find(lambda p: "New York Yankees" in p.display())
print(f"{found._name}")
print()

print("filter() — только те у кого 'Dodgers' в display():")
dodgers = displayable.filter(lambda p: "Dodgers" in p.display())
for p in dodgers:
    print(f"{p._name}")

print()
print("TypedCollection[S] через Protocol Scorable")
print()

scorable: TypedCollection[Scorable] = TypedCollection()
scorable.add(player1)
scorable.add(player2)
scorable.add(player3)
scorable.add(player4)

print("Вызов score() для каждого объекта:")
for p in scorable:
    print(f"{p._name}: {p.score()}")
print()

print("map() через score() — list[float]:")
scores: list[float] = scorable.map(lambda p: p.score())
print(f"{scores}")
print()

print("find() — игрок с наивысшим score():")
best = scorable.find(lambda p: p.score() == max(q.score() for q in scorable))
print(f"{best._name}: {best.score()}")
print()

print("sort_by() через score():")
sorted_col = scorable.sort_by(lambda p: p.score(), reverse=True)
for p in sorted_col:
    print(f"{p._name}: {p.score()}")
print()