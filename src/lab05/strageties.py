import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
 
from src.lab03.models import Pitcher, Defensive

 
def by_name(player):
    return player.name
 
def by_batting_avg(player):
    return player.batting_avg
 
def by_age(player):
    return player.age
 
def by_home_runs(player):
    return player.home_runs
 
def by_name_and_age(player):
    return (player.name, player.age)
 

def is_active(player):
    return player.status == "yes"
 
def is_pitcher(player):
    return isinstance(player, Pitcher)
 
def is_defensive(player):
    return isinstance(player, Defensive)
 
def is_top_batter(player):
    return player.batting_avg >= 0.300
 
 
def make_batting_filter(min_avg: float):
    def filter_fn(player):
        return player.batting_avg >= min_avg
    return filter_fn
 
def make_home_run_filter(min_hr: int):
    def filter_fn(player):
        return player.home_runs >= min_hr
    return filter_fn
 
 
class InjureStrategy:
    def __call__(self, player):
        try:
            player.injure()
        except RuntimeError:
            pass
        return player
 
class RecoverStrategy:
    def __call__(self, player):
        try:
            player.recover()
        except RuntimeError:
            pass
        return player
 
class HitHomeRunStrategy:
    def __call__(self, player):
        try:
            player.hit_home_run()
        except RuntimeError:
            pass
        return player