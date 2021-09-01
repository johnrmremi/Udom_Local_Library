from django.test import TestCase

from catalog.models import Author, Genre,Book, Language

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')
    
    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEqual(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEqual(str(author), expected_object_name)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')

    
class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(name='comic')

    def test_genre_name_label(self):
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_object_name_is_name(self):
        genre = Genre.objects.get(id=1)
        expected_object_name = f'{genre.name}'
        self.assertEqual(str(genre), expected_object_name)


class BookModelTest(TestCase):
    """ Note: I failed here, Much work need to be done in the other rounds of learning.
        The error was due to manytomany author field in the Book model. 
        I am not able to write setUpTestData function below because of errornous genre 
        arrtribute during the book object
    
    """
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        testAuthor = Author.objects.create(first_name='Jakaya', last_name='Mjomba')
        testLang = Language.objects.create(name='English')
        testGenre = Genre.objects.create(name='novel')
        testBook = Book.objects.create(title='Mrs Dalloway', author=testAuthor, language=testLang, summary='Mrs Dalloway is a novel by Virginia Woolf that details a day in the life of Clarissa Dalloway, a fictional high-society woman in post–First World War England. It is one of Woolfs best-known novels', isbn='9780192839701')
        testBook.genre.set([testGenre])

    def test_book_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_book_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_book_author_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_book_language_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('language').verbose_name
        self.assertEqual(field_label, 'language')

    def test_book_summary_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEqual(field_label, 'summary')

    def test_book_summary_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('summary').max_length
        self.assertEqual(max_length, 1000)

    def test_book_summary_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field('summary').help_text
        self.assertEqual(help_text, 'Enter a brief description of the book')

    def test_book_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_book_isbn_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('isbn').max_length
        self.assertEqual(max_length, 13)

    def test_book_isbn_unique_true(self):
        book = Book.objects.get(id=1)
        unique = book._meta.get_field('isbn').unique
        self.assertTrue(unique)

    def test_book_isbn_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field('isbn').help_text
        self.assertEqual(help_text, '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    def test_book_genre_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEqual(field_label, 'genre')

    def test_book_genre_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field('genre').help_text
        self.assertEqual(help_text, 'Select a genre for this book')

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(book.get_absolute_url(), '/catalog/book/1')

    def test_object_name_is_book_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.title}'
        self.assertEqual(str(book), expected_object_name)

    def test_display_genre_is_genre_name_s(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.display_genre(), 'novel')