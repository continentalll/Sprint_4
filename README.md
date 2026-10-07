test_add_new_valid_book - проверка добавления новой валидной книги

test_add_new_invalid_book - проверка добавления новой невалидной книги

test_add_new_book_does_not_overwrite_dublicate - проверка добавления новой книги с одинаковым названием не затирает дубликат

test_set_genre_for_existing_book - проверка установки жанра существующей книге
    
test_set_genre_not_overwrite_existing_genre - проверка, что повторная установка жанра существующей книге не перезаписывает жанр

test_set_genre_do_not_add_unknown_book - проверка, что жанр не устанавливается для недобавленной книги

test_get_genre_return_after_set - проверка возвращения установленного жанра

test_get_genre_return_empty_string_for_book_without_genre - проверка, что у добавленной книги пустой жанр

test_get_book_genre_return_none_for_unknown_book - проверка, что книги не существует, жанр не указывается

test_get_books_with_specific_genre_return_matching_books - проверка возвращения книг только с указанным жанром

test_get_books_with_specific_genre_return_empty_list_for_unknown_genre - проверка, что для неизвестного жанра возвращается пустой список 

test_get_books_genre_return_empty_dictionary - проверка пустого словаря на старте

test_get_books_genre_return_dictionary_with_added_books - проверка заполненного словаря книгой

test_get_books_for_children_return_only_children_genre - проверка, что в результат попали только книги детстких жанров

test_add_book_in_favorites_book - проверка добавления книги в избранное

test_add_book_in_favorites_does_not_add_dublicate - проверка, что повторное добавление книги в избранное не создает дубликат

test_add_book_in_favorites_does_not_add_unknown_book - проверка добавления несуществующей книги в избранное

test_delete_book_from_favorites_removes_book - проверка удаления книги из избранного

test_delete_book_from_favorites_do_nothing_for_not_favorite - проверка удаления несуществующей книги из избранного

test_get_list_of_favorites_books_return_all_favorites - проверка возвращения всех книг из избранного