import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from model import Player

class PlayerList():
    _items = []
    
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
        return next((e for e in self._items if e.name == name), "Игрок с таким именем не найден")
    
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
            print(f"{type(e).__name__}: Такого аттрибута не существует")
            
    def get_active(self):
        return list(e for e in self._items if e.status == "yes")
    
    def get_top(self):
        return list(e for e in self._items if e.performance_grade() == "very good")