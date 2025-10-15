Добавление двух книг(пример). - test_add_new_book_add_two_books
У новой книги жанр не установлен (пустая строка). - test_add_new_book_book_has_empty_genre_by_default
Книга с названием длиннее 40 символов не добавляется. - test_add_new_book_does_not_add_book_with_name_longer_than_40_chars
Не добавляется дубликат книги. - test_add_new_book_does_not_add_duplicate_book
Можно получить и установить корректный жанр из списка. - test_set_and_get_book_genre_valid_genres
Нельзя установить жанр, которого нет в списке. - test_set_book_genre_ignores_invalid_genre
Получение книг по жанру работает корректно. - test_get_books_with_specific_genre_returns_correct_books
Книги с жанрами 'Ужасы' и 'Детективы' не попадают в список для детей. - test_get_books_for_children_excludes_age_rating_genres
Добавление существующей книги в избранное. - test_add_book_in_favorites_adds_existing_book
Удаление книги из избранного. - test_delete_book_from_favorites_removes_book
