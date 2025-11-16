#Класс Book с атрибутами класса
class Book:
    material = "paper"
    cover = "paperback"
    all_books = []
# доступ к атрибутам класса через имя класса
print("Атрибуты класса через Book:")
print(Book.material)  # "paper"
print(Book.cover)  # "paperback"
print(Book.all_books)  # []

# экземпляр класса Book
my_book = Book()

# доступ к атрибутам класса через экземпляр
print("Атрибуты класса через экземпляр:")
print(my_book.material)  # "paper"
print(my_book.cover)  # "paperback"
print(my_book.all_books)  # []
