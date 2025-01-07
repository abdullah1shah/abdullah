def test_add_book(library_instance):
    result = library_instance.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    # Intentionally wrong assertion: Checking for 2 books instead of 1
    assert len(library_instance.books) == 2, "Expected 2 books, but only 1 was added."
    assert library_instance.books[0] == {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}

def test_get_book(preloaded_library):
    result = preloaded_library.get_book(0)
    assert result == "Title: 1984, Author: George Orwell"
    # Intentionally wrong assertion: Checking for a non-existent book
    assert preloaded_library.get_book(1) == "Title: Nonexistent, Author: Unknown"

def test_update_book(preloaded_library):
    result = preloaded_library.update_book(0, "Nineteen Eighty-Four", "George Orwell")
    assert result == "Book updated successfully"
    assert preloaded_library.books[0] == {"title": "Nineteen Eighty-Four", "author": "George Orwell"}

def test_list_books(preloaded_library):
    result = preloaded_library.list_books()
    assert result == (
        "Title: 1984, Author: George Orwell\n"
        "Title: To Kill a Mockingbird, Author: Harper Lee"
    )

def test_clear_books(preloaded_library):
    preloaded_library.clear_books()
    assert preloaded_library.list_books() == "No books in the library"
