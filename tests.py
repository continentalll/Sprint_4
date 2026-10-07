from main import BooksCollector
import pytest



class TestBooksCollector:

    @pytest.mark.parametrize("name", 
    [
        "Книга",
        "К",
        "К" * 40,
    ])
    def test_add_new_valid_book(collector, name):

        collector = BooksCollector()

        collector.add_new_book(name)
        assert name in collector.books_genre


    @pytest.mark.parametrize("name", 
    [
        "",
        "К" * 41,
    ])
    def test_add_new_invalid_book(collector, name):

        collector = BooksCollector()

        collector.add_new_book(name)
        assert name not in collector.books_genre


    def test_add_new_book_does_not_overwrite_dublicate(collector):

        collector = BooksCollector()

        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")
        collector.add_new_book("Дюна")

        assert collector.get_books_genre() == {"Дюна": "Фантастика"}


    def test_set_genre_for_existing_book(collector):

        collector = BooksCollector()
        
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")

        assert collector.get_book_genre("1984") == "Фантастика"


    def test_set_genre_not_overwrite_existing_genre(collector):

        collector = BooksCollector()

        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
        collector.set_book_genre("1984", "Нежанр")

        assert collector.get_book_genre("1984") == "Фантастика"


    def test_set_genre_do_not_add_unknown_book(collector):

        collector = BooksCollector()

        collector.set_book_genre("Недобавленная книга", "Фантастика")

        assert "Недобавленная книга" not in collector.books_genre


    def test_get_genre_return_after_set(collector):

        collector = BooksCollector()
            
        collector.add_new_book("1984")
        collector.set_book_genre("1984", "Фантастика")
                    
        assert collector.get_book_genre("1984") == "Фантастика"
    
    def test_get_genre_return_empty_string_for_book_without_genre(collector):

        collector = BooksCollector()

        collector.add_new_book("1984")

        assert collector.get_book_genre("1984") == ""


    def test_get_book_genre_return_none_for_unknown_book(collector):
        collector = BooksCollector()

        assert collector.get_book_genre("Неизвестная книга") is None


    def test_get_books_with_specific_genre_return_matching_books(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.set_book_genre("A", "Фантастика")
        collector.add_new_book("B")
        collector.set_book_genre("B", "Комедии")
        collector.add_new_book("C")
        collector.set_book_genre("C", "Фантастика")

        assert collector.get_books_with_specific_genre("Фантастика") == ["A", "C"]


    def test_get_books_with_specific_genre_return_empty_list_for_unknown_genre(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.set_book_genre("A", "Фантастика")

        assert collector.get_books_with_specific_genre("Нежанр") == []


    def test_get_books_genre_return_empty_dictionary(collector):

        collector = BooksCollector()

        assert collector.get_books_genre() == {}


    def test_get_books_genre_return_dictionary_with_added_books(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.set_book_genre("A", "Фантастика")

        assert collector.get_books_genre() == {"A": "Фантастика"}


    def test_get_books_for_children_return_only_children_genre(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.set_book_genre("A", "Фантастика")

        collector.add_new_book("B")
        collector.set_book_genre("B", "Комедии")

        collector.add_new_book("C")
        collector.set_book_genre("C", "Ужасы")

        collector.add_new_book("D")
        collector.set_book_genre("D", "Детективы")

        collector.add_new_book("E")
        collector.set_book_genre("E", "Мультфильмы")

        collector.add_new_book("F")

        assert collector.get_books_for_children() == ["A", "B", "E"]


    def test_add_book_in_favorites_book(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.add_book_in_favorites("A")

        assert collector.get_list_of_favorites_books() == ["A"]


    def test_add_book_in_favorites_does_not_add_dublicate(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.add_book_in_favorites("A")
        collector.add_book_in_favorites("A")

        assert collector.get_list_of_favorites_books() == ["A"]


    def test_add_book_in_favorites_does_not_add_unknown_book(collector):
        collector = BooksCollector()

        collector.add_book_in_favorites("B")

        assert collector.get_list_of_favorites_books() == []


    def test_delete_book_from_favorites_removes_book(collector):
        collector = BooksCollector()

        collector.add_new_book("A")
        collector.add_book_in_favorites("A")
        collector.delete_book_from_favorites("A")

        assert collector.get_list_of_favorites_books() == []


    def test_delete_book_from_favorites_do_nothing_for_not_favorite(collector):
        collector = BooksCollector()

        collector.add_new_book("A")
        collector.delete_book_from_favorites("A")

        assert collector.get_list_of_favorites_books() == []


    def test_get_list_of_favorites_books_return_all_favorites(collector):

        collector = BooksCollector()

        collector.add_new_book("A")
        collector.add_book_in_favorites("A")

        collector.add_new_book("B")
        collector.add_book_in_favorites("B")

        assert collector.get_list_of_favorites_books() == ["A", "B"]