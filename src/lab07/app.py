import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.lab03.base import Player
from src.lab03.models import Pitcher, Defensive
from exceptions import PlayerNotFoundError, DuplicatePlayerError, InvalidPlayerTypeError
import storage

STORAGE_PATH = os.path.join(os.path.dirname(__file__), "players.json")


class App:
    def __init__(self) -> None:
        self._players: list[Player] = []
        self._load()

    def _load(self) -> None:
        self._players = storage.load(STORAGE_PATH)

    def save(self) -> None:
        storage.save(self._players, STORAGE_PATH)


    def add_pitcher(self, name: str, age: int, team: str, batting_avg: float, home_runs: int, ERA: float, WHIP: float, K_9: int, position: str = "P", is_playing: str = "yes") -> Pitcher:
        self._check_duplicate(name)
        player = Pitcher(name=name, age=age, team=team, batting_avg=batting_avg, home_runs=home_runs, ERA=ERA, WHIP=WHIP, K_9=K_9, position=position, is_playing=is_playing)
        self._players.append(player)
        return player

    def add_defensive(self, name: str, age: int, team: str, batting_avg: float, home_runs: int, PO: int, A: int, DP: int, position: str = "RF", is_playing: str = "yes") -> Defensive:
        self._check_duplicate(name)
        player = Defensive(name=name, age=age, team=team, batting_avg=batting_avg, home_runs=home_runs, PO=PO, A=A, DP=DP, position=position, is_playing=is_playing)
        self._players.append(player)
        return player

    def remove(self, name: str) -> None:
        player = self._find_or_raise(name)
        self._players.remove(player)

    def get_all(self) -> list[Player]:
        return list(self._players)

    def find_by_name(self, name: str) -> Player:
        return self._find_or_raise(name)


    def get_pitchers(self) -> list[Pitcher]:
        return [p for p in self._players if isinstance(p, Pitcher)]

    def get_defensive(self) -> list[Defensive]:
        return [p for p in self._players if isinstance(p, Defensive)]

    def get_active(self) -> list[Player]:
        return [p for p in self._players if p.status == "yes"]

    def filter_by_team(self, team: str) -> list[Player]:
        return [p for p in self._players if p.team.lower() == team.lower()]

    def filter_by_batting_avg(self, min_avg: float) -> list[Player]:
        return [p for p in self._players if p.batting_avg >= min_avg]


    def sort_by_name(self) -> list[Player]:
        return sorted(self._players, key=lambda p: p.name)

    def sort_by_batting_avg(self) -> list[Player]:
        return sorted(self._players, key=lambda p: p.batting_avg, reverse=True)

    def sort_by_age(self) -> list[Player]:
        return sorted(self._players, key=lambda p: p.age)


    def _find_or_raise(self, name: str) -> Player:
        for p in self._players:
            if p.name.lower() == name.lower():
                return p
        raise PlayerNotFoundError(f"Игрок '{name}' не найден")

    def _check_duplicate(self, name: str) -> None:
        for p in self._players:
            if p.name.lower() == name.lower():
                raise DuplicatePlayerError(f"Игрок '{name}' уже существует")

    def count(self) -> int:
        return len(self._players)