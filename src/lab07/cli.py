from typing import Optional
from app import App
from src.lab03.models import Pitcher, Defensive
from exceptions import PlayerNotFoundError, DuplicatePlayerError, StorageError


class CLI:
    def __init__(self) -> None:
        self._app = App()
        print("игроков в коллекции:", self._app.count())

    def run(self) -> None:
        while True:
            self._print_menu()
            choice = self._input_int("Выберите пункт: ")
            if choice is None:
                continue
            if choice == 0:
                self._exit()
                break
            self._handle(choice)

    def _print_menu(self) -> None:
        print()
        print("MLB Player Manager")
        print()
        print("1. Показать всех игроков")
        print("2. Добавить питчера")
        print("3. Добавить защитника")
        print("4. Найти игрока по имени")
        print("5. Удалить игрока")
        print("6. Фильтрация")
        print("7. Сортировка")
        print("8. Статистика")
        print("0. Выход")
        print()

    def _handle(self, choice: int) -> None:
        handlers = {
            1: self._show_all,
            2: self._add_pitcher,
            3: self._add_defensive,
            4: self._find_player,
            5: self._remove_player,
            6: self._filter_menu,
            7: self._sort_menu,
            8: self._stats,
        }
        handler = handlers.get(choice)
        if handler:
            handler()
        else:
            print("введите число от 0 до 8")

    def _show_all(self) -> None:
        players = self._app.get_all()
        if not players:
            print("коллекция пуста")
            return
        print(f"всего игроков: {len(players)}")
        self._print_players(players)

    def _add_pitcher(self) -> None:
        print("добавить питчера")
        try:
            name = input("Имя: ").strip()
            age = self._input_int("Возраст: ")
            team = input("Команда: ").strip()
            batting_avg = self._input_float("Batting Average (0.0-1.0): ")
            home_runs = self._input_int("Home Runs: ")
            ERA = self._input_float("ERA: ")
            WHIP = self._input_float("WHIP: ")
            K_9 = self._input_int("K/9 (макс 27): ")

            if None in (age, batting_avg, home_runs, ERA, WHIP, K_9):
                print("некорректные данные")
                return

            player = self._app.add_pitcher(
                name=name, age=age, team=team, batting_avg=batting_avg,
                home_runs=home_runs, ERA=ERA, WHIP=WHIP, K_9=K_9
            )
            print(f"Питчер добавлен: {player}")

        except DuplicatePlayerError as e:
            print(f"{e}")
        except (ValueError, TypeError) as e:
            print(f"ошибка валидации: {e}")

    def _add_defensive(self) -> None:
        print("Добавить защитника")
        print("Позиции: C, 1B, 2B, 3B, SS, LF, CF, RF, DH")
        try:
            name = input("Имя: ").strip()
            age = self._input_int("Возраст: ")
            team = input("Команда: ").strip()
            batting_avg = self._input_float("Batting Average (0.0-1.0): ")
            home_runs = self._input_int("Home Runs: ")
            PO = self._input_int("Putouts (PO): ")
            A = self._input_int("Assists (A): ")
            DP = self._input_int("Double Plays (DP): ")
            position = input("Позиция: ").strip().upper()

            if None in (age, batting_avg, home_runs, PO, A, DP):
                print("некорректные данные")
                return

            player = self._app.add_defensive(
                name=name, age=age, team=team, batting_avg=batting_avg,
                home_runs=home_runs, PO=PO, A=A, DP=DP, position=position
            )
            print(f"защитник добавлен: {player}")

        except DuplicatePlayerError as e:
            print(f"{e}")
        except (ValueError, TypeError) as e:
            print(f"ошибка валидации: {e}")

    def _find_player(self) -> None:
        name = input("Введите имя игрока: ").strip()
        try:
            player = self._app.find_by_name(name)
            print(f"найден:")
            self._print_player(player)
        except PlayerNotFoundError as e:
            print(f"{e}")

    def _remove_player(self) -> None:
        name = input("Введите имя игрока для удаления: ").strip()
        try:
            player = self._app.find_by_name(name)
            confirm = input(f'Удалить "{player.name}"? (y/n): ').strip().lower()
            if confirm == "y":
                self._app.remove(name)
                print(f"игрок '{name}' удалён")
            else:
                print("Отменено.")
        except PlayerNotFoundError as e:
            print(f"{e}")

    def _filter_menu(self) -> None:
        print("Фильтрация")
        print("1. Только питчеры")
        print("2. Только защитники")
        print("3. Только активные игроки")
        print("4. По команде")
        print("5. По минимальному batting average")
        choice = self._input_int("Выберите: ")

        if choice == 1:
            self._print_players(self._app.get_pitchers())
        elif choice == 2:
            self._print_players(self._app.get_defensive())
        elif choice == 3:
            self._print_players(self._app.get_active())
        elif choice == 4:
            team = input("Команда: ").strip()
            self._print_players(self._app.filter_by_team(team))
        elif choice == 5:
            avg = self._input_float("Минимальный BA: ")
            if avg is not None:
                self._print_players(self._app.filter_by_batting_avg(avg))
        else:
            print("неверный пункт")


    def _sort_menu(self) -> None:
        print("\n── Сортировка ──")
        print("1. По имени")
        print("2. По batting average (убывание)")
        print("3. По возрасту")
        choice = self._input_int("Выберите стратегию: ")

        if choice == 1:
            self._print_players(self._app.sort_by_name())
        elif choice == 2:
            self._print_players(self._app.sort_by_batting_avg())
        elif choice == 3:
            self._print_players(self._app.sort_by_age())
        else:
            print("неверный пункт")

    def _stats(self) -> None:
        players = self._app.get_all()
        pitchers = self._app.get_pitchers()
        defensive = self._app.get_defensive()
        active = self._app.get_active()

        print("Статистика")
        print(f"Всего игроков:   {len(players)}")
        print(f"Питчеров:        {len(pitchers)}")
        print(f"Защитников:      {len(defensive)}")
        print(f"Активных:        {len(active)}")

        if players:
            top = max(players, key=lambda p: p.batting_avg)
            print(f"Лучший BA: {top.name} ({top.batting_avg:.3f})")

    def _exit(self) -> None:
        try:
            self._app.save()
            print("Данные сохранены")
        except StorageError as e:
            print(f"Ошибка сохранения: {e}")

    def _input_int(self, prompt: str) -> Optional[int]:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число")
            return None

    def _input_float(self, prompt: str) -> Optional[float]:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число")
            return None

    def _print_players(self, players: list) -> None:
        if not players:
            print("Список пуст")
            return
        print(f"\n{'#':<4} {'Имя':<20} {'Позиция':<8} {'Команда':<25} {'BA':<7} {'HR':<6} {'Статус'}")
        print()
        for i, p in enumerate(players, 1):
            print(f"{i:<4} {p.name:<20} {p.position:<8} {p.team:<25} {p.batting_avg:<7.3f} {p.home_runs:<6} {p.status}")
        print()

    def _print_player(self, player) -> None:
        print(f"{player}")
        if isinstance(player, Pitcher):
            print(f"ERA: {player.ERA} WHIP: {player.WHIP} K/9: {player.K_9}")
            print(f"ERA Grade: {player.ERA_grade()}")
        elif isinstance(player, Defensive):
            print(f"PO: {player.PO} A: {player.A} DP: {player.DP}")
            print(f"Defensive Rating: {player.defensive_rating()}")