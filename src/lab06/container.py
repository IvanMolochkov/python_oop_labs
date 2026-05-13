from typing import TypeVar, Generic, Callable, Optional, Protocol


# ───────────────────────────────────────────────
# Протоколы
# ───────────────────────────────────────────────

class Displayable(Protocol):
    def display(self) -> str:
        ...

class Scorable(Protocol):
    def score(self) -> float:
        ...


# ───────────────────────────────────────────────
# TypeVar
# ───────────────────────────────────────────────

T = TypeVar('T')
R = TypeVar('R')
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)


# ───────────────────────────────────────────────
# TypedCollection
# ───────────────────────────────────────────────

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        if list(e for e in self._items if e == item) != list():
            raise TypeError("Нельзя добавлять дубликат")
        self._items.append(item)

    def remove(self, item: T) -> None:
        try:
            self._items.remove(item)
        except ValueError as e:
            print(f"{type(e).__name__}: Нельзя удалять несуществующий элемент")

    def get_all(self) -> list[T]:
        return list(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        try:
            return self._items[index]
        except IndexError as e:
            return f"{type(e).__name__}: Элемент с таким индексом не найден"

    def remove_at(self, index: int) -> None:
        try:
            self._items = list(e for e in self._items if e != self._items[index])
        except IndexError as e:
            print(f"{type(e).__name__}: Элемент с таким индексом не найден")

    def sort(self, key: str, reverse: bool = False) -> None:
        try:
            self._items = sorted(self._items, key=lambda e: getattr(e, key), reverse=reverse)
        except AttributeError as e:
            print(f"{type(e).__name__}: Такого атрибута не существует")

    def sort_by(self, key_func: Callable[[T], any], reverse: bool = False) -> "TypedCollection[T]":
        result: TypedCollection[T] = TypedCollection()
        result._items = sorted(self._items, key=key_func, reverse=reverse)
        return result

    def filter_by(self, predicate: Callable[[T], bool]) -> "TypedCollection[T]":
        result: TypedCollection[T] = TypedCollection()
        result._items = list(filter(predicate, self._items))
        return result

    def apply(self, func: Callable[[T], T]) -> "TypedCollection[T]":
        result: TypedCollection[T] = TypedCollection()
        result._items = list(map(func, self._items))
        return result

    # ── методы из задания на 4 ──

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Возвращает первый элемент, удовлетворяющий условию, или None."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """Возвращает список всех элементов, удовлетворяющих условию."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        """Применяет функцию к каждому элементу и возвращает список результатов."""
        return [transform(item) for item in self._items]