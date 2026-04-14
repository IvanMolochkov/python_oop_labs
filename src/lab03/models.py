import sys
import os
 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.lab03.base import Player


# класс питчера
class Pitcher(Player):
    def __init__(self, name: str, age: int, team: str, batting_avg: float, home_runs: int, ERA: float, WHIP: float, K_9: float, position: str, is_playing: str = "yes"):
        super().__init__(name, age, team, batting_avg, home_runs, position, is_playing)
        if position != "P":
            raise ValueError("Игрок не является питчером")
        self._ERA = ERA
        self._WHIP = WHIP
        self._K_9 = K_9
    
    @property
    def ERA(self):
        return self._ERA
    
    @property
    def WHIP(self):
        return self._WHIP
    
    @property
    def K_9(self):
        return self._K_9
    
    @ERA.setter
    def ERA(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("ERA must be a number")
        self._ERA = float(value)
    
    @WHIP.setter
    def WHIP(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("WHIP must be a number")
        self._WHIP = float(value)
    
    @K_9.setter
    def K_9(self, value: int):
        if not isinstance(value, int):
            raise TypeError("K/9 must be a number")
        if value > 27:
            raise ValueError("Страйкаутов за 9 иннингов не может быть больше 27")
        self._K_9 = value
    
    # total chances
    def calculate(self):
        return round((self._ERA + self._WHIP + self._K_9) / 3, 2)
    
    def ERA_grade(self):
        if self._ERA <= 2.0:
            return "elite"
        if 2.0 < self._ERA <= 3.0:
            return "very good"
        if 3.0 < self._ERA >= 4.0:
            return "good"
        if 4.0 < self._ERA >= 5.0:
            return "average"
        if 5.0 < self._ERA >= 6.0:
            return "bad"
        return "he's not a pitcher anymore"
    
    def __str__(self):
        return (
            f"name: {self._name}, age: {self._age}, team: {self._team}, position: {self._position}, BA: {self._batting_avg:.3f}, HR: {self._home_runs}, ERA: {self._ERA}, WHIP: {self._WHIP}, K/9: {self._K_9}, is playing: {self._is_playing}"
        )
 
    def __repr__(self):
        return (
            f"Player(name={self._name!r}, age={self._age}, team={self._team}, batting_avg={self._batting_avg:.3f}, home_runs={self._home_runs}, ERA={self._ERA}, WHIP={self._WHIP}, K_9={self._K_9}, position={self._position!r}, is playing={self._is_playing!r})"
        )
 
    def __eq__(self, other: object):
        if not isinstance(other, Pitcher):
            return NotImplemented
        return (self._name == other._name and self._position == other._position and self._batting_avg == other._batting_avg and self._ERA == other._ERA and self._WHIP == other._WHIP and self._K_9 == other._K_9)


# класс зашиты
class Defensive(Player):
    def __init__(self, name: str, age: int, team: str, batting_avg: float, home_runs: int, PO: int, A: int, DP: int, position: str, is_playing: str = "yes"):
        super().__init__(name, age, team, batting_avg, home_runs, position, is_playing)
        if position == "P":
            raise ValueError("Игрок не является ни защитником базы, ни шортстопом, ни аутфилдером, ни кетчером")
        self._PO = PO
        self._A = A
        self._DP = DP
    
    @property
    def PO(self):
        return self._PO
    
    @property
    def A(self):
        return self._A
    
    @property
    def DP(self):
        return self._DP
    
    @PO.setter
    def PO(self, value: int):
        if not isinstance(value, int):
            raise TypeError("PO must be a number")
        if value > 1458:
            raise ValueError("PO не может быть больше 1458")
        self._PO = value
    
    @A.setter
    def A(self, value: int):
        if not isinstance(value, int):
            raise TypeError("A must be a number")
        if value > 4374:
            raise ValueError("A не может быть больше 4374")
        self._A = value
    
    @DP.setter
    def DP(self, value: int):
        if not isinstance(value, int):
            raise TypeError("DP must be a number")
        if value > 1458:
            raise ValueError("DP не может быть больше 1458")
        self._DP = value
    
    # sum stats
    def calculate(self):
        return self._PO + self._A
    
    def defensive_rating(self):
        score = self._PO + self._A + self._DP * 2
        if score >= 500:
            return "elite"
        if score >= 300:
            return "good"
        if score >= 150:
            return "average"
        return "bad"
    
    def __str__(self):
        return (
            f"name: {self._name}, age: {self._age}, team: {self._team}, position: {self._position}, BA: {self._batting_avg:.3f}, HR: {self._home_runs}, PO: {self._PO}, A: {self._A}, DP: {self._DP}, is playing: {self._is_playing}"
        )
 
    def __repr__(self):
        return (
            f"Player(name={self._name!r}, age={self._age}, team={self._team}, batting_avg={self._batting_avg:.3f}, home_runs={self._home_runs}, PO={self._PO}, A={self._A}, DP={self._DP}, position={self._position!r}, is playing={self._is_playing!r})"
        )
 
    def __eq__(self, other: object):
        if not isinstance(other, Defensive):
            return NotImplemented
        return (self._name == other._name and self._position == other._position and self._batting_avg == other._batting_avg and self._PO == other._PO and self._A == other._A and self._DP == other._DP)