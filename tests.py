from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    #     # создаем экземпляр (объект) класса BooksCollector
    #     collector = BooksCollector()

    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')

    #     # проверяем, что добавилось именно две
    #     # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #     assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    @pytest.fixture
    def collector(self):
        return BooksCollector()


    @pytest.mark.parametrize(
        "name, expected_present",
        [
            ("Книга", True),
            ("A" * 40, True),
            ("", False),
            ("A" * 41, False),
        ],
    )
    def test_add_new_book(collector, name, expected_present):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert (name in collector.books_genre) is expected_present
        if expected_present:
            assert collector.books_genre[name] == ""


    def test_add_new_book_does_not_overwrite_dublicate(collector):

        collector = BooksCollector()

        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")
        collector.add_new_book("Дюна")

        assert collector.get_books_genre() == {"Дюна": "Фантастика"}


    def test_set_book_genre(collector):
    
        collector = BooksCollector()
    
        collector.add_new_book("1984")
    
        collector.set_book_genre("1984", "Фантастика")
        assert collector.get_book_genre("1984") == "Фантастика"
    
        collector.set_book_genre("1984", "Нежанр")
        assert collector.get_book_genre("1984") == "Фантастика"
    
        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert "Неизвестная книга" not in collector.books_genre
    
    def test_get_book_genre(collector):

        collector = BooksCollector()
            
        collector.add_new_book("1984")
            
        assert collector.get_book_genre("1984") == ""
            
        collector.set_book_genre("1984", "Фантастика")
        assert collector.get_book_genre("1984") == "Фантастика"
            
        assert collector.get_book_genre("Нет такой книги") is None


    def test_get_books_with_specific_genre(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.set_book_genre("A", "Фантастика")

        collector.add_new_book("B")
        collector.set_book_genre("B", "Комедии")

        collector.add_new_book("C")
        collector.set_book_genre("C", "Фантастика")

        assert collector.get_books_with_specific_genre("Фантастика") == ["A", "C"]
        assert collector.get_books_with_specific_genre("Нежанр") == []


    def test_get_books_genre(collector):

        collector = BooksCollector()

        assert collector.get_books_genre() == {}

        collector.add_new_book("A")
        collector.set_book_genre("A", "Фантастика")

        assert collector.get_books_genre() == {"A": "Фантастика"}


    def test_get_books_for_children(collector):

        collector = BooksCollector()

        collector.add_new_book("Фантастика")
        collector.set_book_genre("Фантастика", "Фантастика")

        collector.add_new_book("Комедия")
        collector.set_book_genre("Комедия", "Комедии")

        collector.add_new_book("Ужас")
        collector.set_book_genre("Ужас", "Ужасы")

        collector.add_new_book("Детектив")
        collector.set_book_genre("Детектив", "Детективы")

        collector.add_new_book("Мультфильм")
        collector.set_book_genre("Мультфильм", "Мультфильмы")

        collector.add_new_book("Без жанра")

        assert collector.get_books_for_children() == [
            "Фантастика",
            "Комедия",
            "Мультфильм",
        ]


    def test_add_book_in_favorites(collector):

        collector = BooksCollector()

        collector.add_new_book("A")

        collector.add_book_in_favorites("A")
        assert collector.get_list_of_favorites_books() == ["A"]

        collector.add_book_in_favorites("A")
        collector.add_book_in_favorites("B")

        assert collector.get_list_of_favorites_books() == ["A"]


    def test_delete_book_from_favorites(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.add_book_in_favorites("A")

        collector.delete_book_from_favorites("A")
        assert collector.get_list_of_favorites_books() == []

        collector.delete_book_from_favorites("A")
        assert collector.get_list_of_favorites_books() == []


    def test_get_list_of_favorites_books(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.add_new_book("B")

        collector.add_book_in_favorites("A")
        collector.add_book_in_favorites("B")

        assert collector.get_list_of_favorites_books() == ["A", "B"]