import pytest
from library import Library

@pytest.fixture
def library_instance():
    return Library()

@pytest.fixture
def preloaded_library():
    lib = Library()
    lib.add_book("1984", "George Orwell")
    lib.add_book("To Kill a Mockingbird", "Harper Lee")
    return lib





