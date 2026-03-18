# 7. Фитнес / Спорт
import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from validate import (validate_name, validate_age, validate_team, validate_batting_average, validate_home_runs, validate_position, validate_status)

class Player:
    position_example = ("P", "C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH")
    status_example  = ("yes", "no, injured", "no, retired")
    _count: int = 0
    
    # описание игрока
    def __init__(self, name: str, age: int, team: str, batting_avg: float, home_runs: int, position: str, is_playing: str = "yes"):
        self._name = validate_name(name)
        self._age  = validate_age(age)
        self._team = validate_team(team)
        self._batting_avg = validate_batting_average(batting_avg)
        self._home_runs = validate_home_runs(home_runs)
        self._position = validate_position(position)
        self._is_playing = validate_status(is_playing)
        Player._count += 1

    # геттеры
    @property
    def name(self):
        return self._name
 
    @property
    def age(self):
        return self._age

    @property
    def batting_avg(self):
        return self._batting_avg
 
    @property
    def home_runs(self):
        return self._home_runs
 
    @property
    def position(self):
        return self._position
 
    @property
    def status(self):
        return self._is_playing
    
    # сеттеры
    @batting_avg.setter
    def batting_avg(self, value: float):
        self._batting_avg = value
 
    @home_runs.setter
    def home_runs(self, value: int):
        self._home_runs = value
 
    @age.setter
    def age(self, value: int):
        self._age = value
    
    # перевод в другую команду
    def team_change(self, new_team: str):
        new_team = validate_team(new_team)
        if self._team == new_team:
            raise RuntimeError(f"this player already playing in {new_team}")
        self._team = new_team
        
    # механика is_playing
    def injure(self):
        if self._is_playing != "yes":
            raise RuntimeError("injured player can not injure again")
        self._is_playing = "no, injured"
 
    def recover(self):
        if self._is_playing != "no, injured":
            raise RuntimeError("healthy player can not recover")
        self._is_playing = "yes"
 
    def retire(self):
        if self._is_playing == "no, retired":
            raise RuntimeError("this player already retired")
        self._is_playing = "no, retired"
    
    # статистика отбиваний мяча (бизнес-методы)
    def hit_home_run(self):
        if self._is_playing != "yes":
            raise RuntimeError("this player cannot hit a home run")
        self._home_runs += 1
 
    def performance_grade(self):
        if self._batting_avg >= 0.300:
            return "very good"
        if self._batting_avg >= 0.260:
            return "good"
        if self._batting_avg >= 0.230:
            return "average"
        return "bad"
    
    # подсчет игроков (класс-метод)
    @classmethod
    def total_players(cls) -> int:
        return cls._count
    
    # магические методы
    def __str__(self):
        return (
            f"name: {self._name}, age: {self._age}, position: {self._position}, BA: {self._batting_avg:.3f}, HR: {self._home_runs}, is playing: {self._is_playing}"
        )
 
    def __repr__(self):
        return (
            f"Player(name={self._name!r}, age={self._age}, batting_avg={self._batting_avg:.3f}, home_runs={self._home_runs}, position={self._position!r}, is playing={self._is_playing!r})"
        )
 
    def __eq__(self, other: object):
        if not isinstance(other, Player):
            return NotImplemented
        return (self._name == other._name and self._position == other._position and self._batting_avg == other._batting_avg)