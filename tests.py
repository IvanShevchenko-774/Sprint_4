import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_book_has_empty_genre_by_default(self):
        collector = BooksCollector()
        collector.add_new_book('Новая книга')
        assert collector.get_book_genre('Новая книга') == ''

    def test_add_new_book_does_not_add_book_with_name_longer_than_40_chars(self):
        collector = BooksCollector()
        long_name = 'A' * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_add_new_book_does_not_add_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дубль')
        collector.add_new_book('Дубль')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("book_name", [
        "A",
        "A" * 40,
        "Обычное название"
    ])
    def test_add_new_book_accepts_valid_name_lengths(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name", [
        "",
        "A" * 41,
        "A" * 100
    ])
    def test_add_new_book_rejects_invalid_name_lengths(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_set_book_genre_ignores_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Тайна')
        collector.set_book_genre('Тайна', 'Биография')  # такого жанра нет
        assert collector.get_book_genre('Тайна') == ''

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Звёзды')
        collector.add_new_book('Смех')
        collector.set_book_genre('Звёзды', 'Фантастика')
        collector.set_book_genre('Смех', 'Комедии')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Звёзды']

    def test_get_books_for_children_excludes_books_in_age_rating_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert 'Оно' not in collector.get_books_for_children()

    def test_get_books_for_children_includes_books_in_child_friendly_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Тачки')
        collector.set_book_genre('Тачки', 'Мультфильмы')
        assert 'Тачки' in collector.get_books_for_children()

    def test_add_book_in_favorites_adds_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая')
        collector.add_book_in_favorites('Любимая')
        assert 'Любимая' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Удаляемая')
        collector.add_book_in_favorites('Удаляемая')
        collector.delete_book_from_favorites('Удаляемая')
        assert 'Удаляемая' not in collector.get_list_of_favorites_books()