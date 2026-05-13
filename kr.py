# # --- теория ---
# # Вопрос 1
# # 1. Наследование использует связь is-a, а композиция - has-a
# # 2. Для того чтобы избежать сложную иерархию
# # 3. Бейсболист - это Игрок - наследование(is-a),
# # Машина имеет Двигатель - композиция(has-a)

# # is-a:
# class Player():
#     def __init__(self, name):
#         self._name = name

# class BaseBaller(Player):
#     def __init__(self, name, team):
#         super().__init__(name)
#         self._team = team

# # has-a:
# class Engine:
#     def __init__(self, power):
#         self._power = power

# class Car:
#     def __init__(self, mark, power):
#         self._mark = mark
#         self.engine = Engine(power)
    
#     def __str__(self):
#         return f"{self._mark}, {self.engine._power}"



# print()
# car = Car("toyota chaser", "1000hp")
# print(car)

# print()
# print()
# print()

# # -- практика ---

# class Book:
#     def __init__(self, title: str, author: str, pages: int):
#         self._title = title
#         self._author = author
#         self._pages = pages


#     def get_info(self):
#         return f"\"{self._title}\" — {self._author}, {self._pages} стр."


#     def __str__(self):
#         return self.get_info()


# class Ebook(Book):
#     def __init__(self, title, author, pages, format_type):
#         super().__init__(title, author, pages)
#         self._format = format_type

#     def get_info(self):  
#         return f"\"{self._title}\" — {self._author}, {self._pages} стр." + f" [{self._format}]"
    
#     def get_download_link(self):
#         return f"https://books.com/{"-".join(self._title.split())}"


# book = Ebook("Lord Of the Rings", "Tolkien", "1000", "ebook")
# print(book.get_info())
# print(book.get_download_link())
# print()




#     # TODO: реализуйте get_download_link()
#     # Пример: "Война и мир" → "https://books.com/война-и-мир"


