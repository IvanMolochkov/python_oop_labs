# кр 2

# теория
# вопрос №1

# Функции высшего порядка - это функции которые принимают другие функции как аргументы или возвращают функции как результат.

# Чтобы функцию можно было передавать как аргумент, она должна быть объектом первого класса - в питоне все функции являются объектами, их можно присваивать переменным, передавать и возвращать.

# Псевдокод:

# def reverse(e):
#     res = []
#     for el in e:
#         res.append(el)
#     res = res[::-1]
#     return "".join(res)

# workouts = ["пресс качат", "бегит", "турник", "анжуманя"]

# def apply_to_all(workouts, transform_func):
#     result = []
#     for workout in workouts:
#         result.append(transform_func(workout))
#     return result

# print("Пример вызова с lambda:")
# print(apply_to_all(workouts, lambda e: f"Он любит {e}"))
# print()

# print("Пример ошибки:")
# print(apply_to_all(workouts, reverse()))
# print("Как должно быть:")
# print(apply_to_all(workouts, reverse))
# print()

# Впоследствии transform() вызывается сразу и возвращает ошибку TypeError


# практика
# вопрос №2

from datetime import date
from abc import ABC, abstractmethod

class Workout:
    def __init__(self, athlete_name: str, exercise_type: str, duration_min: int, calories_burned: float, date: date) -> None:
        athlete_name = athlete_name.strip()
        if not athlete_name:
            raise ValueError("Имя спортсмена не может быть пустым")
        if not exercise_type.strip():
            raise ValueError("Тип упражнения не может быть пустым")
        if not isinstance(duration_min, int) or not (1 <= duration_min <= 600):
            raise ValueError("Длительность должна быть целым числом от 1 до 600")
        if calories_burned <= 0:
            raise ValueError("Калории должны быть больше 0")
        if date > date.today():
            raise ValueError("Дата не может быть в будущем")

        self._athlete_name: str = athlete_name
        self._exercise_type: str = exercise_type.strip()
        self._duration_min: int = duration_min
        self._calories_burned: float = calories_burned
        self._date: date = date

    @property
    def athlete_name(self) -> str:
        return self._athlete_name

    @property
    def exercise_type(self) -> str:
        return self._exercise_type

    @property
    def duration_min(self) -> int:
        return self._duration_min

    @property
    def calories_burned(self) -> float:
        return self._calories_burned

    @property
    def date(self):
        return self._date

    def intensity(self) -> float:
        return self._calories_burned / self._duration_min

    def is_intense(self) -> bool:
        return self.intensity() > 10

    def __str__(self) -> str:
        return f"{self._athlete_name} — {self._exercise_type}, {self._duration_min} мин, {self._calories_burned} ккал ({self._date})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Workout):
            return NotImplemented
        return (self._athlete_name == other._athlete_name and
                self._date == other._date and
                self._exercise_type == other._exercise_type)

    def __lt__(self, other: "Workout") -> bool:
        return self._date < other._date



# вопрос №3 

class AnalyticsStrategy(ABC):
    @abstractmethod
    def analyze(self, workouts: list) -> dict:
        pass


class TotalStats(AnalyticsStrategy):
    def analyze(self, workouts: list) -> dict:
        return {
            "total_workouts": len(workouts),
            "total_minutes": sum(w.duration_min for w in workouts),
            "total_calories": sum(w.calories_burned for w in workouts),
        }

class AverageStats(AnalyticsStrategy):
    def analyze(self, workouts: list) -> dict:
        if not workouts:
            return {"avg_duration": 0, "avg_calories": 0, "avg_intensity": 0}
        n = len(workouts)
        return {
            "avg_duration": round(sum(w.duration_min for w in workouts) / n, 2),
            "avg_calories": round(sum(w.calories_burned for w in workouts) / n, 2),
            "avg_intensity": round(sum(w.intensity() for w in workouts) / n, 2),
        }

class ByExerciseStats(AnalyticsStrategy):
    def analyze(self, workouts: list) -> dict:
        result = {}
        for w in workouts:
            if w.exercise_type not in result:
                result[w.exercise_type] = {"count": 0, "total_calories": 0}
            result[w.exercise_type]["count"] += 1
            result[w.exercise_type]["total_calories"] += w.calories_burned
        return result


class WorkoutJournal:
    def __init__(self) -> None:
        self._workouts: list[Workout] = []
        self._analytics: AnalyticsStrategy | None = None

    def add(self, workout: Workout) -> None:
        if not isinstance(workout, Workout):
            raise TypeError("Можно добавлять только объекты Workout")
        self._workouts.append(workout)

    def __iter__(self):
        return iter(self._workouts)

    def __len__(self) -> int:
        return len(self._workouts)

    def filter_by(self, predicate) -> "WorkoutJournal":
        result = WorkoutJournal()
        result._workouts = list(filter(predicate, self._workouts))
        return result

    def map_to(self, transform_func) -> list:
        return list(map(transform_func, self._workouts))

    def apply(self, func) -> "WorkoutJournal":
        result = WorkoutJournal()
        result._workouts = list(map(func, self._workouts))
        return result

    def set_analytics(self, strategy: AnalyticsStrategy) -> None:
        self._analytics = strategy

    def get_report(self) -> dict:
        if self._analytics is None:
            raise ValueError("Стратегия анализа не установлена")
        return self._analytics.analyze(self._workouts)


def make_intensity_filter(min_intensity: float):
    def predicate(workout: Workout) -> bool:
        return workout.intensity() >= min_intensity
    return predicate

def make_date_range_filter(start_date, end_date):
    def predicate(workout: Workout) -> bool:
        return start_date <= workout.date <= end_date
    return predicate

def make_exercise_filter(exercise_type: str):
    def predicate(workout: Workout) -> bool:
        return workout.exercise_type == exercise_type
    return predicate


# demo.py

from datetime import date as d

w = Workout('Александр', 'бег', 45, 450, d(2025, 5, 20))
print("Создание экземпляра Workout и вызов методов")
print("__str__():")
print(w)
print("intensity():")
print(w.intensity())
print("is_intense():")
print(w.is_intense())
print()

print("Создание журнала (список упражнений)")
j = WorkoutJournal()
j.add(Workout('Александр', 'бег', 30, 350, d(2025, 5, 15)))
j.add(Workout('Александр', 'присед.', 20, 150, d(2025, 5, 16)))
j.add(Workout('Александр', 'бег', 45, 500, d(2025, 5, 20)))

print("Использование стратегии TotalStats():")
j.set_analytics(TotalStats())
print(j.get_report())
print()

print("Использование стратегии TotalStats():")
j.set_analytics(AverageStats())
print(j.get_report())
print()

print("Использование стратегии TotalStats():")
j.set_analytics(ByExerciseStats())
print(j.get_report())
print()


print("З\u0336а\u0336в\u0336о\u0336д\u0336ы\u0336 фабрика функций")
print("Фильтр по интенсивности не менее 10 (т.е. по соотношению калорий к времени):")
intense = j.filter_by(make_intensity_filter(10))
print(*intense)
print()

print("Фильтр по бегу (по имени):")
may_run = j.filter_by(make_exercise_filter('бег'))
names = may_run.map_to(lambda w: w.athlete_name)
print(names)