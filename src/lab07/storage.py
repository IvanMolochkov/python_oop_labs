import json
from exceptions import StorageError


def save(players: list, filepath: str) -> None:
    try:
        data = []
        for p in players:
            entry = {
                "type": type(p).__name__,
                "name": p._name,
                "age": p._age,
                "team": p._team,
                "batting_avg": p._batting_avg,
                "home_runs": p._home_runs,
                "position": p._position,
                "is_playing": p._is_playing,
            }
            if type(p).__name__ == "Pitcher":
                entry["ERA"] = p._ERA
                entry["WHIP"] = p._WHIP
                entry["K_9"] = p._K_9
            elif type(p).__name__ == "Defensive":
                entry["PO"] = p._PO
                entry["A"] = p._A
                entry["DP"] = p._DP
            data.append(entry)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    except Exception as e:
        raise StorageError(f"Ошибка сохранения: {e}")


def load(filepath: str) -> list:
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

    from src.lab03.models import Pitcher, Defensive

    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        players = []
        for entry in data:
            t = entry["type"]
            if t == "Pitcher":
                p = Pitcher(
                    name=entry["name"],
                    age=entry["age"],
                    team=entry["team"],
                    batting_avg=entry["batting_avg"],
                    home_runs=entry["home_runs"],
                    ERA=entry["ERA"],
                    WHIP=entry["WHIP"],
                    K_9=entry["K_9"],
                    position=entry["position"],
                    is_playing=entry["is_playing"],
                )
            elif t == "Defensive":
                p = Defensive(
                    name=entry["name"],
                    age=entry["age"],
                    team=entry["team"],
                    batting_avg=entry["batting_avg"],
                    home_runs=entry["home_runs"],
                    PO=entry["PO"],
                    A=entry["A"],
                    DP=entry["DP"],
                    position=entry["position"],
                    is_playing=entry["is_playing"],
                )
            else:
                continue
            players.append(p)

        return players

    except Exception as e:
        raise StorageError(f"Ошибка загрузки: {e}")