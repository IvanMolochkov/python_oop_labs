import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.lab03.base import Player as Player
from src.lab03.models import Pitcher, Defensive
from src.lab04.interfaces import Printable, Calculate


full_position = {
    "P": "pitcher",
    "C": "catcher",
    "1B": "the first basemen",
    "2B": "the second basemen",
    "3B": "the third basemen",
    "SS": "short stop",
    "LF": "left field",
    "CF": "center field",
    "RF": "right field",
    "DH": "на банке",
}

class PlayerList():
    def __init__(self, items=None):
        self._items = list(items) if items else list()
    
    def add(self, item):
        if not isinstance(item, Player):
            raise TypeError("Дружище, добавлять можно только Бейсболистов")
        if list(e for e in self._items if e == item) != list():
            raise TypeError("Нельзя добавлять дубликат")
        if list(e for e in self._items if e.name == item.name) != list():
            raise TypeError("Игрок с таким именем уже существует")
        self._items.append(item)
    
    def remove(self, item):
        try:
            self._items.remove(item)
        except ValueError as e:
            print(f"{type(e).__name__}: Нельзя удалять несуществующего игрока")
        
    def get_all(self):
        return self._items
    
    def find_by_name(self, name):
        player = list(e for e in self._items if e.name == name)
        if player == []:
            return "Игрок с таким именем не найден"
        return player

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, id):
        try:
            return self._items[id]
        except IndexError as e:
            return f"{type(e).__name__}: Игрок с таким индексом не найден"

    def remove_at(self, index):
        try:
            self._items = list(e for e in self._items if e != self._items[index])
        except IndexError as e:
            print(f"{type(e).__name__}: Игрок с таким индексом не найден")

    # 99999 сортировок
    def sort_by_name(self):
        self._items = sorted(self._items, key=lambda e: e.name)

    def sort_by_team(self):
        self._items = sorted(self._items, key=lambda e: e.team)

    def sort_by_batting_avg(self):
        self._items = sorted(self._items, key=lambda e: e.batting_avg, reverse=True)

    def sort(self, key, reverse: bool = False):
        try:
            self._items = sorted(self._items, key=lambda e: getattr(e, key), reverse=reverse)
        except AttributeError as e:
            print(f"{type(e).__name__}: Такого атрибута не существует")

    def sort_by(self, key_func, reverse: bool = False):
        sorted_items = sorted(self._items, key=key_func, reverse=reverse)
        return PlayerList(sorted_items)

    def calculate_all(self):
        return list(f"{e._name}: {e.calculate()}" for e in self._items)

    def get_only_pitchers(self):
        return list(e for e in self._items if isinstance(e, Pitcher))

    def get_only_defensive(self): 
        return list(e for e in self._items if isinstance(e, Defensive))

    def get_printable(self):
        return [e for e in self._items if isinstance(e, Printable)]

    def get_calculable(self):
        return [e for e in self._items if isinstance(e, Calculate)]

    def sort_by_calculate(self):
        calculable = self.get_calculable()
        return sorted(calculable, key=lambda x: x.calculate())
    
    # воздушный фильтр
    def get_active(self):
        array = list(filter(lambda e: e.status == "yes", self._items)) 
        if array == []:
            return "В этом сезоне никто не играет("
        return array
    
    def get_top(self):
        array = list(filter(lambda e: e.performance_grade() == "very good", self._items)) 
        if array == []:
            return "Топов нет("
        return array

    def filter_by(self, predicate):
        filtered_items = list(filter(predicate, self._items))
        return PlayerList(filtered_items)
    
    # map
    def get_only_name(self):
        return list(map(lambda e: e.name, self._items))

    def get_full_position(self):
        return list(map(lambda e: full_position[e.position], self._items))

    def map_to_strings(self):
        return list(map(lambda e: str(e), self._items))

    # заводы
    @staticmethod
    def make_batting_filter(min_avg: float):
        def filter_fn(player):
            return player.batting_avg >= min_avg
        return filter_fn

    @staticmethod
    def make_home_run_filter(min_hr: int):
        def filter_fn(player):
            return player.home_runs >= min_hr
        return filter_fn
    
    # aппли
    def apply(self, func):
        result = list(map(func, self._items))
        return PlayerList(result)