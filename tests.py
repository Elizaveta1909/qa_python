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

    def test_add_new_book_add_books_return_books_in_books_rating(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Что делать, если ваш кот хочет вас убить')
        book.add_new_book('Ежик и солнышко')
        assert 'Гордость и предубеждение и зомби' in book.books_rating
        assert 'Что делать, если ваш кот хочет вас убить' in book.books_rating
        assert 'Ежик и солнышко' in book.books_rating

    def test_add_new_book_add_same_book_in_books_rating_return_len_1(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Гордость и предубеждение и зомби')
        assert len(book.get_books_rating()) == 1

    def test_get_books_rating_add_books_in_books_rating_return_len_2(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Ежик и солнышко')
        assert len(book.books_rating) == 2

    def test_get_book_rating_get_rating_of_missing_book_return_None(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        rating = book.get_book_rating('Что делать, если ваш кот хочет вас убить')
        assert rating is None

    def test_get_books_with_specific_rating_rating_does_not_exist_return_len_0(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        assert len(book.get_books_with_specific_rating(3)) == 0

    def test_set_book_rating_set_rating_not_less_then_1_return_None(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        rating_0 = book.set_book_rating('Гордость и предубеждение и зомби', 0)
        assert rating_0 is None

    def test_set_book_rating_set_rating_no_more_then_10_return_None(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        rating_11 = book.set_book_rating('Гордость и предубеждение и зомби', 11)
        assert rating_11 is None

    def test_set_book_rating_book_does_not_exist_rating_is_None(self):
        book = BooksCollector()
        rating_5 = book.set_book_rating('Что делать, если ваш кот хочет вас убить', 5)
        assert rating_5 is None

    def test_add_book_in_favorites_add_book_return_book_is_in_favorites(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in book.favorites

    def test_add_book_in_favorites_add_book_not_from_books_rating_return_book_not_in_favorites(self):
        book = BooksCollector()
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in book.favorites

    def test_add_book_in_favorites_add_same_book_in_favorites_return_len_1(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(book.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_get_list_of_2_books_return_len_2(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_new_book('Ежик и солнышко')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Ежик и солнышко')
        assert len(book.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_delete_book_return_book_not_in_favorites(self):
        book = BooksCollector()
        book.add_new_book('Гордость и предубеждение и зомби')
        book.add_book_in_favorites('Гордость и предубеждение и зомби')
        book.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in book.favorites
