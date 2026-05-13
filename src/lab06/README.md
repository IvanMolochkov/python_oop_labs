# Лабораторная работа №6
*Generics и typing*

## Цель работы
- Освоить систему аннотаций типов в Python (`typing`)
- Научиться создавать обобщённые (generic) классы с помощью `TypeVar` и `Generic`
- Понять концепцию структурной типизации через `typing.Protocol`

---

## Описание реализованных типов и контейнеров

### `TypedCollection[T]` (`container.py`)

Generic-версия коллекции из ЛР-2. Повторяет её интерфейс, но теперь знает какой тип хранится внутри. Тип указывается при создании:

```python
players: TypedCollection[Pitcher] = TypedCollection()
numbers: TypedCollection[int] = TypedCollection()
```

| Метод | Сигнатура | Описание |
|---|---|---|
| `add` | `(item: T) -> None` | Добавляет элемент, проверяет дубликат |
| `remove` | `(item: T) -> None` | Удаляет элемент |
| `get_all` | `() -> list[T]` | Возвращает все элементы |
| `find` | `(predicate: Callable[[T], bool]) -> Optional[T]` | Первый подходящий элемент или `None` |
| `filter` | `(predicate: Callable[[T], bool]) -> list[T]` | Все подходящие элементы |
| `map` | `(transform: Callable[[T], R]) -> list[R]` | Преобразует элементы, тип результата может быть другим |
| `sort_by` | `(key_func: Callable[[T], any]) -> TypedCollection[T]` | Сортировка по функции, возвращает новую коллекцию |
| `filter_by` | `(predicate: Callable[[T], bool]) -> TypedCollection[T]` | Фильтрация, возвращает новую коллекцию |
| `apply` | `(func: Callable[[T], T]) -> TypedCollection[T]` | Применяет функцию ко всем элементам |

### TypeVar

| TypeVar | Описание |
|---|---|
| `T` | Основной тип элементов коллекции |
| `R` | Тип результата в `map()` — может отличаться от `T` |
| `D = TypeVar('D', bound=Displayable)` | Только объекты с методом `display()` |
| `S = TypeVar('S', bound=Scorable)` | Только объекты с методом `score()` |

### Протоколы (`container.py`)

Протокол описывает что должен уметь объект — **без наследования**, просто по наличию нужных методов (структурная типизация).

**`Displayable`** — требует метод `display() -> str`

**`Scorable`** — требует метод `score() -> float`

Классы `Pitcher` и `Defensive` из ЛР-3 **не наследуются** от этих протоколов, но у обоих есть методы `display()` и `score()` — значит оба им соответствуют.

---

## Демонстрация работы

### Базовая демонстрация `TypedCollection`
Создание типизированной коллекции, добавление объектов, получение по индексу, валидация дубликата:
```
Длина коллекции: 2
Элемент по индексу [0]: Gerrit Cole

Попытка добавить дубликат:
TypeError: Нельзя добавлять дубликат
```

### `find()`, `filter()`, `map()`

`find()` — найден и не найден:
```
find() — найден: Aaron Judge
find() — не найден: None
```

`filter()` — только питчеры с ERA < 3.0:
```
Gerrit Cole: ERA 2.17
```

`map()` меняет тип результата — одна коллекция, разные типы вывода:
```python
# list[str]
mixed.map(lambda p: p._name)
# → ['Gerrit Cole', 'Shohei Ohtani', 'Aaron Judge', 'Mookie Betts']

# list[float]
mixed.map(lambda p: p._batting_avg)
# → [0.28, 0.304, 0.331, 0.307]
```

### Сценарий 1 — `TypedCollection[D]` через Protocol `Displayable`
`Pitcher` и `Defensive` не наследуются от `Displayable`, но у обоих есть `display()` — оба попадают в коллекцию:
```
Питчер Gerrit Cole | Команда: New York Yankees | ERA: 2.17 | WHIP: 1.28 | K/9: 22
Питчер Shohei Ohtani | Команда: Los Angeles Dodgers | ERA: 3.14 | WHIP: 1.06 | K/9: 11
RF Aaron Judge | Команда: New York Yankees | PO: 1346 | A: 39 | DP: 8
RF Mookie Betts | Команда: Los Angeles Dodgers | PO: 280 | A: 10 | DP: 2

find() — первый у кого 'Yankees': Gerrit Cole
filter() — только 'Dodgers': Shohei Ohtani, Mookie Betts
```

### Сценарий 2 — `TypedCollection[S]` через Protocol `Scorable`
Тот же класс `TypedCollection`, другое ограничение — объекты с методом `score()`:
```
Gerrit Cole: 8.48
Shohei Ohtani: 5.07
Aaron Judge: 1385.0
Mookie Betts: 290.0

find() — наивысший score(): Aaron Judge: 1385.0

sort_by() через score():
Aaron Judge: 1385.0
Mookie Betts: 290.0
Gerrit Cole: 8.48
Shohei Ohtani: 5.07
```