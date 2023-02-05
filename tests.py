from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):  # Проверяем что добавились две книги
        collection = BooksCollector()
        collection.add_new_book('Дорога')
        collection.add_new_book('Старикам тут не место')
        assert len(collection.get_books_rating()) == 2

    def test_add_new_book_cannot_be_added_twice(self):  # Проверяем что не можем добавить две одинаковых книги
        collection = BooksCollector()
        collection.add_new_book("Хранитель сада")
        collection.add_new_book("Хранитель сада")
        assert len(collection.get_books_rating()) == 1

    def test_set_book_rating_book_not_in_collection(self):  # Проверяем что не можем добавить рейтинг книге если ее нет
        collection = BooksCollector()
        collection.add_new_book('Пассажир')
        collection.set_book_rating('Содом и Гоморра', 6)
        assert collection.get_book_rating('Содом и Гоморра') == None

    def test_add_new_book_default_rating(self):  # Проверяем что при добавлении книги ей устанавливается по умолчанию
        collection = BooksCollector()
        collection.add_new_book('Сын садовника')
        assert collection.get_books_rating()['Сын садовника'] == 1

    def test_adding_book_in_favorites_add_book(self):  # Проверяем что можем добавить книгу в избранное
        collection = BooksCollector()
        collection.add_new_book('Саттри')
        collection.add_book_in_favorites('Саттри')
        assert 'Саттри' in collection.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book(self):  # Проверяем что можем удалить книгу из избранного
        collection = BooksCollector()
        collection.add_new_book('Тьма снаружи')
        collection.add_book_in_favorites('Тьма снаружи')
        collection.delete_book_from_favorites('Тьма снаружи')
        assert len(collection.get_list_of_favorites_books()) == 0

    def test_set_book_rating_rating_not_over_than_one(self):  # Проверяем что книге невозможно установить рейтинг ниже 1
        collection = BooksCollector()
        collection.add_new_book('Стелла Марис')
        collection.set_book_rating('Стелла Марис', 0)
        assert collection.get_book_rating('Стелла Марис') == 1

    def test_set_book_rating_rating_no_more_than_ten(self):  # Проверяем что книге невозможно установить рейтинг выше 10
        collection = BooksCollector()
        collection.add_new_book('Кровавый меридиан')
        collection.set_book_rating('Кровавый меридиан', 11)
        assert collection.get_books_rating()['Кровавый меридиан'] == 1

    def test_favorites_books_is_list(self):  # Проверяем что favorites это список
        collection = BooksCollector()
        assert collection.favorites == []

    def test_books_rating_is_dictionary(self):  # Проверяем что books_raiting это словарь
        collection = BooksCollector()
        assert collection.books_rating == {}
