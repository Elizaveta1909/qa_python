from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


class TestBooksCollector:
    def test_add_new_book_add_a_book(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')
        book.add_new_book('Ежик и солнышко')
        assert 'Гордость и предубеждение и зомби' and 'Что делать, если ваш кот хочет вас убить' and 'Ежик и солнышко' in book.books_rating


class TestBooksCollector:

    def test_add_new_book_add_a_book(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        assert len(book.get_books_rating()) == 1

    def test_add_new_book_add_a_book_again(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        assert len(book.get_books_rating()) != 2


class TestBooksCollector:

    def test_add_new_book_add_a_book(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in book.books_rating

    def test_get_book_rating_set_rating(self):
        book = BooksCollector()
        book.get_book_rating('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' not in book.books_rating


class TestBooksCollector:
    def test_set_book_rating_set_rating(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert 'Гордость и предубеждение и зомби' not in book.get_books_with_specific_rating(0)


class TestBooksCollector:
    def test_set_book_rating_set_rating(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert 'Гордость и предубеждение и зомби' not in book.get_books_with_specific_rating(11)


class TestBooksCollector:
    def test_get_book_rating_get_rating(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.get_book_rating('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' not in book.get_books_with_specific_rating(1)


class TestBooksCollector:
    def test_add_book_in_favorites_add_book(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in book.favorites


class TestBooksCollector:
    def test_add_book_in_favorites_add_book(self):
        book = BooksCollector()
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in book.favorites


class TestBooksCollector:
    def test_add_book_in_favorites_add_book(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(book.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_book_again(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(book.get_list_of_favorites_books()) != 2

class TestBooksCollector:
    def test_delete_book_from_favorites_delete_book(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        book.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in book.favorites